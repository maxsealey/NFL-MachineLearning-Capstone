from flask import Flask, render_template

app = Flask(__name__)
'''
To run debug server (better for ongoing development), navigate to app directory in CLI and run:
-> export FLASK_DEBUG=1
-> flask run

OR

-> export FLASK_APP=main.py
-> flask run

then open http://127.0.0.1:5000/ in your browser
'''
test_data = [
    {
        'first': 'max',
        'last': 'sealey'
    },
    {
        'first': 'george',
        'last': 'washington'
    },
    {
        'first': 'tom',
        'last': 'brady'
    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', test_data=test_data)


@app.route("/predict")
def predict():
    return "<h1>Predictor</h1>"


@app.route("/visualize")
def visuals():
    return "<h1>Visualize</h1>"


@app.route("/data")
def data():
    return "<h1>Data</h1>"


@app.route("/notfound")
def notfound():
    return "<h1>404</h1>"


# prevents side effects when file imported
if __name__ == '__main__':
    app.run(debug=True)
