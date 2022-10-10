# Machine Learning Engineering Zoomcamp 2022
## Week 5 Homework

## Question 1

* Install Pipenv
* What's the version of pipenv you installed?
* Use `--version` to find out

> The version is 
```terminal
pipenv, version 2022.10.4
```  

## Question 2

* Use Pipenv to install Scikit-Learn version 1.0.2
* What's the first hash for scikit-learn you get in Pipfile.lock?

Note: you should create an empty folder for homework
and do it there. 

> The first hash is: 

  ```terminal
  "sha256:08ef968f6b72033c16c479c966bf37ccd49b06ea91b765e1cc27afefe723920b"
  ```  

## Models

We've prepared a dictionary vectorizer and a model.

They were trained (roughly) using this code:

```python
features = ['reports', 'share', 'expenditure', 'owner']
dicts = df[features].to_dict(orient='records')

dv = DictVectorizer(sparse=False)
X = dv.fit_transform(dicts)

model = LogisticRegression(solver='liblinear').fit(X, y)
```

> **Note**: You don't need to train the model. This code is just for your reference.

And then saved with Pickle. Download them:

* [DictVectorizer](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/cohorts/2022/05-deployment/homework/dv.bin?raw=true)
* [LogisticRegression](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/cohorts/2022/05-deployment/homework/model1.bin?raw=true)

With `wget`:

  ```bash
  PREFIX=https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/course-zoomcamp/cohorts/2022/05-deployment/homework
  wget $PREFIX/model1.bin
  wget $PREFIX/dv.bin
  ```
  
Question 3
Let's use these models!

Write a script for loading these models with pickle
Score this client:
{"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}
What's the probability that this client will get a credit card?

0.162
0.391
0.601
0.993

> The answer is 0.162

  
Question 4
Now let's serve this model as a web service

Install Flask and gunicorn (or waitress, if you're on Windows)
Write Flask code for serving the model
Now score this client using requests:
url = "YOUR_URL"
client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}
requests.post(url, json=client).json()
What's the probability that this client will get a credit card?

0.274
0.484
0.698
0.928





















# Machine Learning Engineering Zoomcamp 2022

✅: 1 - [x] Introduction to Machine Learning  
✅: 2 - [x] Machine Learning for Regression  
✅: 3 - [x] Machine Learning for Classification  
✅: 4 - x[] Evaluation Metrics for Classification  
5 - [] Deploying Machine Learning Models  
6 - [] Bento ML  
7 - [] Decision Trees and Ensemble Learning  
8 - [] Midterm Project  
9 - [] Midterm Project Evaluation  
10 - [] Neural Networks and Deep Learning  
11 - [] Serverless Deep Learning  
12 - [] Kubernetes and TensorFlow-Serving  
13 - [] Kubeflow and KFServing  
14 - [] Capstone Project  
15 - [] Capstone Project Evaluation  
16 - [] The third Project  
17 - [] The third Project Evaluation  
18 - [] Article  

Collapsible List idea:
https://gist.github.com/pierrejoubert73/902cc94d79424356a8d20be2b382e1ab

<details>
  <summary>Introduction to Machine Learning</summary>
    1. Topic 1
  2. Topic 2
     * Sub-Topic 1
     * Sub-Topic 2

  ### Some Code
  ```js
  function logSomething(something) {
    console.log('Something', something);
  }
  ```
</details>
