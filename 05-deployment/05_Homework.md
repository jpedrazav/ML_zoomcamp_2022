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
  
## Question 3
Let's use these models!

Write a script for loading these models with pickle
Score this client:
{"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}
What's the probability that this client will get a credit card?

0.162
0.391
0.601
0.993

> The answer is 0.162 (check code predict.py)

  
## Question 4
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
> The answer is 0.928 (check codes flask_test.py for creation and 05_Q4_flask_web_service_request.ipynb for request)

