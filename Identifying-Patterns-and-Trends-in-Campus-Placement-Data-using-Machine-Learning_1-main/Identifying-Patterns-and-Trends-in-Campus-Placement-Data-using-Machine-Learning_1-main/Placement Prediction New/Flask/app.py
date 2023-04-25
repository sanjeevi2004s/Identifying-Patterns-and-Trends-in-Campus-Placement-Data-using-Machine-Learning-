from flask import Flask, render_template, request
import pickle
import sklearn
import joblib


app = Flask(__name__)

model = pickle.load(open('placement.pkl', 'rb'))


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict')
def predict():
    return render_template("predict.html")


@app.route('/Register', methods=["POST", "GET"])
def result():
    if request.method == "POST":
        a = request.form.get('age')
        g = request.form.get('gender')
        s = request.form.get('stream')
        i = request.form.get('internships')
        c = request.form.get('cgpa')
        n = request.form.get('no_of_backlog')
        prediction = [[int(a), int(g), int(s), int(i), int(c), int(n)]]

        print(prediction)

        prediction = model.predict[[int(a), int(g), int(s), int(i), int(c), int(n)]]

        if prediction == 0:
            output = "Not-Placed"
        else:
            output = "Placed"

        return render_template("output.html", y=output)


if __name__ == '__main__':
    app.run(debug=True)