from flask import Flask, request, json, render_template
import pandas as pd
#from flask_cors import CORS
import sys
import ast
import pickle
sys.path.append('../asset_classification/scripts')
sys.path.append('../asset_classification/utils')
from pre_process import pre_process
import config
import numpy as np 
import predict_lstm
from continuous_learning_script import retrain_when_user_prompts
from correction_of_asset_class_after_predict import pre_process_and_append_to_dataset



app = Flask(__name__)


@app.route('/')
def index():   
    return render_template('app.html')

@app.route('/prediction/', methods= ["GET","POST"])
def prediction():
    if request.method == 'GET':
        argument_dict={}
        dict_tmp =  request.args.to_dict()
        for key in dict_tmp.keys():
            argument_dict = ast.literal_eval(key)

        order = argument_dict['orderTitle']
        desc = argument_dict['description']
        
        text_string = order+" "+desc
        pre_processed_str = pre_process(text_string)
        df_dict = predict_lstm.main(order, desc)

        l1= list(df_dict.keys())
        l2 = list(df_dict.values())

        res ={}
        for key in l1:
            for value in l2:
                res[key]=value
                l2.remove(value)
                break

        result=[]
        for key, value in res.items():
            t={}
            t['Prediction']=key
            t['Confidence']= value
            result.append(t)

        return json.dumps(result)


@app.route('/predictII/', methods = ["GET","POST"])
def predictII():
    if request.method == "GET":
        print("hi")
        argument_dict={}
        dict_tmp = request.args.to_dict()
        for key in dict_tmp.keys():
            argument_dict = ast.literal_eval(key)

        order = argument_dict['orderTitle']
        desc = argument_dict['description']
        asset_class = argument_dict['asset_class']
    
        result_correct = pre_process_and_append_to_dataset(order, desc, asset_class)
       
        return json.dumps(result_correct)

@app.route('/continuouslearning/',methods=["GET","POST"])
def continuous_learning():
    if request.method == 'GET':
        accuracy, precision, recall, f1score = retrain_when_user_prompts()
        result = []
        metric = ['Accuracy', 'Precision', 'Recall', 'F1-score']
        value = [accuracy, precision, recall, f1score]
        for i in range(0, 4):
            t = {}
            t['Metrics'] = metric[i]
            t['Values'] = value[i]
            result.append(t)
        
        print(result)
        return json.dumps(result)


@app.route('/importantfeatures/', methods=["GET", "POST"])
def imp_features():
    if request.method == 'GET':
         
        data = dict()
        df_important = pd.read_csv(config.important_features)
        data['importance'] = list(df_important['indices'])
        data['features'] = list(df_important['features'])
        return json.dumps(data)

@app.route('/performancemetrics/', methods=["GET", "POST"])
def pm():
    print("say")
    if request.method == 'GET':
            df_shallow = pd.read_csv(config.performance)
            df_dl = pd.read_csv(config.performance_for_all_DL_models)
            accuracy, precision, recall, F1_score = list(df_shallow['accuracy']), list(df_shallow['precision']), list(df_shallow['recall']), list(df_shallow['F1-score'])
            accuracydl, precisiondl, recalldl, F1_scoredl = list(df_dl['accuracy']), list(df_dl['precision']), list(df_dl['recall']), list(df_dl['f1_score'])
            data_1 = dict()
            data_1['model'] = ["Naives Bayes","KNN","Decision Tree", "Random Forest","LSTM","Bi-LSTM","RNN","GRU","Bi-GRU"]
            data_1['metrics'] = [accuracy[0],accuracy[1],accuracy[2],accuracy[3],accuracydl[0],accuracydl[1],accuracydl[2],accuracydl[3],accuracydl[4],accuracydl[5]]

            print(data_1)
            data_2 = dict()
            data_2['model'] = ["Naives Bayes","KNN","Decision Tree", "Random Forest","LSTM","Bi-LSTM","RNN","GRU","Bi-GRU"]     
            data_2['metrics'] = [recall[0],recall[1],recall[2],recall[3],recalldl[0],recalldl[1],recalldl[2],recalldl[3],recalldl[4],recalldl[5]]  

            data_3 = dict()
            data_3['model'] =  ["Naives Bayes","KNN","Decision Tree", "Random Forest","LSTM","Bi-LSTM","RNN","GRU","Bi-GRU"]          
            data_3['metrics'] = [precision[0],precision[1],precision[2],precision[3],precisiondl[0],precisiondl[1],precisiondl[2],precisiondl[3],precisiondl[4],precisiondl[5]]  

            data_4 = dict()
            data_4['model'] =  ["Naives Bayes","KNN","Decision Tree", "Random Forest","LSTM","Bi-LSTM","RNN","GRU","Bi-GRU"]          
            data_4['metrics'] = [F1_score[0],F1_score[1],F1_score[2],F1_score[3],F1_scoredl[0],F1_scoredl[1],F1_scoredl[2],F1_scoredl[3],F1_scoredl[4],F1_scoredl[5]]  
            
            data = dict()
            data['data_1'] = data_1
            data['data_2'] = data_2
            data['data_3'] = data_3
            data['data_4'] = data_4
    
            print(data)

            return json.dumps(data)

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods','GET,POST')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 8005, debug=True)
