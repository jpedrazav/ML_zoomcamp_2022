import pickle

model_file = 'model1.bin'
dv_file = 'dv.bin'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

with open(dv_file, 'rb') as f_in2:
    dv = pickle.load(f_in2)

customer = {
    "reports": 0, 
    "share": 0.001694, 
    "expenditure": 0.12, 
    "owner": "yes"
}

def predict_single(customer, dv, model):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[:, 1]
    return y_pred[0]

prediction = predict_single(customer, dv, model)

print('prediction', prediction)

