from flask import Flask, render_template, request
from inference import Abstract2Title


app=Flask(__name__)


@app.route('/')
def home():
    return render_template("Home.html")

@app.route('/about')
def about():
    return render_template("AboutTheProject.html")

@app.route('/predict')
def predict():
    return render_template("Predict.html")

@app.route('/examples')
def examples():
    return render_template("Examples.html")

@app.route('/',methods=['GET','POST'])
def getvalue():
    abstract=request.form['abstract']
    print(abstract)
    model = Abstract2Title(r'model')
    title = model(abstract)
    return render_template('result.html',abstract=abstract,title=title)

if __name__== "__main__":
    app.run(debug=True)