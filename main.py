from flask import Flask

app=Flask(__name__)
@app.route("/")
def one():
    return "Welcome"

@app.route("/predict")
def predict():
    return "Prediction"
if __name__=='__main__':
    app.run(debug=True)