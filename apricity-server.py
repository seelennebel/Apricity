# Apricity Flask application!

from flask import Flask, request
from flask import render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from word_cloud import Word_Cloud

app = Flask(__name__)
app.secret_key = "I am following you"

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/form/output")
def success():
    result = session['result']
    print(result)
    return render_template("success.html", result = result)

@app.route("/form", methods = ['GET','POST'])
def form_page():
    form = FlaskForm(meta = {'csrf': False})
    if form.is_submitted():
        r = request.form
        print(r.to_dict())
        result = Word_Cloud(r.to_dict())
        session['result'] = result
        return redirect(url_for('success'))
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)