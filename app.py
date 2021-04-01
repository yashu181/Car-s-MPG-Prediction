from flask import Flask, render_template, request
import pickle
import numpy as np

from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        HP=int(request.form['HP'])
        VOL=int(request.form['VOL'])
        SP=int(request.form['SP'])
        WT=int(request.form['WT'])
        
        prediction=model.predict([[HP,VOL,SP,WT]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry MPG is low")
        else:
            return render_template('index.html',prediction_text="MPG is {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)