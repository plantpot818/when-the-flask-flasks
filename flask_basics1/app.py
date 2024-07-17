from flask import Flask, render_template
import random

app = Flask(__name__)
secret_text = "sussy among us"
secret_nums = [1111, 7722, 2, 991122334455667788]
lucky_num = random.choice(secret_nums)
secret_info = {"name": "impostor", "description": "kinda sus", "gender": "unknown"}


@app.route("/")
def home():
    return "<h1>Hello World!</h1>"

@app.route("/secret")
def secret():
    return render_template("secret.html", secret_text = secret_text, lucky_num = lucky_num, secret_info = secret_info)

@app.route("/best_subject")
def best_subject():
    return "<h1>Computing is the best subject</h1>"

@app.route("/h2comp")
def h2comp():
    return "<h1>Computing is a h2 subject</h1>"

@app.route("/computing")
def computing():
    return "<h1>What is computing?</h1>"

if __name__ == "__main__":
    app.run(debug = True, port = 1234)

