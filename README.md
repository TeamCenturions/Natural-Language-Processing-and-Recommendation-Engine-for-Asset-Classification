## Natural Language Processing and Recommendation Engine For Asset Classification
> Sponsored - Accenture Federal Services

- [Description](#Description)
- [HowToUse](#How To Use)
- [License](#License)
- [AuthorInfo](#AuthorInfo)


<!-- toc -->
----
### Description

Accenture Federal Services manages the global supply chain system for a federal client that tracks the procurement, distribution, maintenance, and retirement of assets. To ensure flexibility, the users were allowed to enter freeform textual information when describing an order. As part of that process, the order would then be assigned an asset class by an expert manually since there was no automated system that would map the order details to asset classes. Over the years, this led to inconsistencies in data and resulted in poor data quality. To ensure data reliability in the future, the client wanted to automate the asset classification process. To address this problem, an Asset Classification Engine was developed which is a Web Application hosted on an AWS EC2 instance. To build this application, a Deep Learning based Long short-term memory (LSTM) model was trained to predict the asset classes based on Order Title and Line Description with an F1-score of 78%. To facilitate continuous learning and improvement, the model can be retrained with revised asset classes. Additionally, to identify the similar asset classes, an algorithm was developed that reduced their number by 92.76%. This algorithm and the model can provide maximum performance with large data and a balanced class distribution. To facilitate scalability and portability, a REST API was developed along with a Graphical User Interface (GUI) for server interactions. The developed system will automate the asset classification and recommendation process to further improve the global supply chain by generating correct asset class labels automatically.

----
### How To Use
Run the LSTM.py in the deeplearning folder to save the model and load the application using app.py in the FlaskApp folder to generate predictions.

----
### License
MIT License <br/>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

----
### AuthorInfo
Team Centurions - Chaithanya Pramodh Kasula, Varalakshmi Vakkalagadda, Ramya Sri Sonar, Aishwarya Varala<br/>
George Mason University<br/>
DAEN 690<br/>
Spring 2021<br/>
