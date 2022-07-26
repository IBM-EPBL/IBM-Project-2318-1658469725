# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14IZpvoMVFe-SjH-G3b4iSTEGA-o1Fg6N
"""

def predict(data):
    try:
        col_name = ['id','cycle','set1','set2','set3','s1','s2','s3','s4','s5','s6','s7','s8']+['s9','s10','s11','s12','s13','s14','s14','s15','s16','s17','s18','s19','s20']
        test_dataset = pd.DataFrame([data],columns=col_name)
        rul=pd.DataFrame(test_dataset.groupby("id")['cycle'].max()).reset_index()
        rul.columns = ['id','max']
        truth_ds['rtf']=truth_ds['more']+rul["max"]
        truth_ds.head()
        truth_ds['rtf']=truth_ds['more']+rul["max"]
        test_dataset=test_dataset.merge(truth_ds, on= ['id'], how= "left")
        test_dataset[ 'ttf']=test_dataset['rtf'] - test_dataset['cycle']
        test_dataset.drop ('rtf', axis=1, inplace=True)
        df_test = test_dataset.copy()
        period = 30
        df_test['label_bc'] = df_test ['ttf'].apply(lambda x: 1 if x <= period else 0)
        df_test = df_test.dropna()
        if len(df_test.index) == 0 :
            return True
        x_test = df_test.iloc[ : , : -2].values
        y_pred = model.predict(x_test)
        return True if y_pred[0] else False
    except:
        return True

from flask import Flask, render_template
from flask import request
from flask_cors import CORS
import joblib

import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "uRaU-TjwldvnODMwaDakva7BY1NKMjg2n6OFsnMoFrXa"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token',data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('ibm.html')
@app.route('/pre', methods=['POST'])
def result():
    a="problem"
    b="not a failure"
    c="check the inputs"
    #try:
        #if request.method == 'POST':
    id1=float(request.form['id'])
    cyc=float(request.form['cycle'])
    set1=float(request.form['set1'])
    set2=float(request.form['set2'])
    set3=float(request.form['set3'])
    s1=float(request.form['s1'])
    s2=float(request.form['s2'])
    s3=float(request.form['s3'])
    s4=float(request.form['s4'])
    s5=float(request.form['s5'])
    s6=float(request.form['s6'])
    s7=float(request.form['s7'])
    s8=float(request.form['s8'])
    s9=float(request.form['s9'])
    s10=float(request.form['s10'])
    s11=float(request.form['s11'])
    s12=float(request.form['s12'])
    s13=float(request.form['s13'])
    s14=float(request.form['s14'])
    s15=float(request.form['s15'])
    s16=float(request.form['s16'])
    s17=float(request.form['s17'])
    s18=float(request.form['s18'])
    s19=float(request.form['s19'])
    s20=float(request.form['s20'])
    s21=float(request.form['s21'])
    last = predict([[id1,cyc,set1,set2,set3,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20]])
    l=[[id1,cyc,set1,set2,set3,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,last]]
    payload_scoring = {"input_data": [{"field": [['id1','cyc','set1','set2','set3','s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12','s13','s14','s15','s16','s17','s18','s19','s20','s21','last']],"values": l}]}
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/6b03fb5d-159d-4b31-bfc0-e51cd75e797a/predictions?version=2022-11-21', json=payload_scoring,headers={'Authorization': 'Bearer ' + mltoken})
    print(response_scoring)
    print(response_scoring.json())

    predictions=response_scoring.json()
    predict1=predictions['predictions'][0]['values'][0][0]
    print("Final Predictions:",predict1)
    
    if predict1:
        print(a)
        val =a
        #return a
    else:
        print(b)
        val =b
        #return b
    return render_template('result.html', ans=val)
if __name__ == "__main__":
  app.run(debug=False)
