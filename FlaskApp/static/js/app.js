$("document").ready(function(){
    $('#button-addon1').click(function(){
        var order_title = $("#order").val();
	 console.log(order_title)
        var desc = $("#desc").val();
	    console.log(desc)
        $.ajax({
                url: "/prediction/",
		contentType:"application/json",
            	data: JSON.stringify({"orderTitle": order_title,"description":desc}),
                type: "GET",
                dataType: 'json',
		crossDomain: true,
                success: function(response){
                console.log(response)

		var list = response
                var col = [];
                for (var i = 0; i < list.length; i++) {
                    for (var key in list[i]) {
                        if (col.indexOf(key) === -1) {
                            col.push(key);
                        }
                    }
                }
                var table = document.createElement("table");
                var tr = table.insertRow(-1);

                for (var i = 0; i < col.length; i++) {
                    var th = document.createElement("th");
                    th.innerHTML = col[i];
                    tr.appendChild(th);
                }

                for (var i = 0; i < list.length; i++) {
                    tr = table.insertRow(-1);
                    for (var j = 0; j < col.length; j++) {
                        var tabCell = tr.insertCell(-1);
                        tabCell.innerHTML = list[i][col[j]];
                    }
                }
                var divContainer = document.getElementById("showData");
                divContainer.innerHTML = "";
                divContainer.appendChild(table);
                },
                error: function(error){
				console.log(error);
		
			}
        });
    });
    
    $('#btn').click(function(){
	    var input = $("#input").val();
	    $.ajax({
		    url:"/prediction/",
		    type: "POST",
		    data: JSON.stringify({"input":input}),
		    crossOrigin: true,
		    dataType: 'json',
		    contentType: "application/json",
		    success: function(response){
			    console.log(response);
			    document.getElementById("demo").innerHTML="Successfully appended";
		    }

	    });
    });
    		

 
    $('#btn_imp').click(function(){
        $.ajax({
	    url: "/importantfeatures/",
            type: "GET",
            contentType: "application/json",
            dataType: 'json',
            success: function(response){
                var data = {}
                data['x'] = response["importance"]
                data['y'] = response["features"]
                data['orientation'] = 'h'
                data['type'] = 'bar'

                var transforms = {}
                transforms['type'] = 'sort'
                transforms['target'] = 'x'
                transforms['order'] = 'ascending'

                data['transforms'] = [transforms]
	
              var layout ={
                title: {
                        text:'Feature Importance Plot generated by Random Forest Model on Dataset',
                        font: {
                          family: 'Arial',
                          size: 24
                        },
                       xref: 'paper',
                       x: 0.05,
                      },
                      xaxis: {
                        title: {
                          text: 'Relative Importance',
                          font: {
                            family: 'Arial',
                            size: 18,
                            color: '#7f7f7f'
                          }
                        },
                      },
                      yaxis: {
			dtick: 1,
                        title: {
                          text: 'Features',
                          font: {
                            family: 'Arial',
                            size: 18,
                            color: '#7f7f7f'
                          }
                        }
                      }
                }


                Plotly.newPlot('feature_imp_div',[data], layout)


            }
        });
    });
    $('#btn_pm').click(function(){
     $.ajax({
            url: "/performancemetrics/",
            type: "GET",
            contentType: "application/json",
            dataType: 'json',
            success: function(response){
		    var d1={}
		    var d2={}
		    var d3={}
		    var d4={}
		    console.log("hello")
		    for(i=0;i<Object.keys(response).length;i++){
			    t=Object.values(response)[i]
			    if(i==0){
				    d1['x'] = t["model"]
				    d1['y'] = t["metrics"]
				    d1['type'] = 'bar'
		            }
			    if(i==1){
				    d2['x'] =t["model"]
				    d2['y'] = t["metrics"]
				    d2['type'] = 'bar'
			    }
			    if(i==2){
				    d3['x'] = t["model"]
				    d3['y'] = t["metrics"]
				    d3['type'] = 'bar'
			    }
			  if(i==3){
				    d4['x']= t["model"]
				    d4['y'] = t["metrics"]
				    d4['type'] = 'bar'
			    }
		    }
		    
		   var layout1 = {
			     title: 'Accuracy',
			     font:{
				         family: 'Raleway, sans-serif'
				       },
			     showlegend: false,
			 
			     yaxis: {
				         zeroline: false,
				         gridwidth: 2
				       },
			     bargap :0.05
		   };
                    Plotly.newPlot('performance_metrics_1', [d1],layout1);
		    
		    var layout2 = {
			      title: 'Recall',
			      font:{
				          family: 'Raleway, sans-serif'
				        },
			      showlegend: false,
			 
			      yaxis: {
				          zeroline: false,
				          gridwidth: 2
				        },
			      bargap :0.05
		    };

		    Plotly.newPlot('performance_metrics_2', [d2],layout2); 
		    
		    var layout3 = {
			      title: 'Precision',
			      font:{
				          family: 'Raleway, sans-serif'
				        },
			      showlegend: false,
		
			      yaxis: {
				          zeroline: false,
				          gridwidth: 2
				        },
			      bargap :0.05
		    };

		    Plotly.newPlot('performance_metrics_3', [d3],layout3); 
		    
		    var layout4 = {
			      title: 'F1_score',
			      font:{
				          family: 'Raleway, sans-serif'
				        },
			      showlegend: false,
			   
			      yaxis: {
				          zeroline: false,
				          gridwidth: 2
				        },
			      bargap :0.05
		    };

		    Plotly.newPlot('performance_metrics_4', [d4],layout4);   
	   }
     


       });
    
    });

});




