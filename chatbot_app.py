from flask import Flask, render_template, request
import pandas as pd
from stock_chatbot import get_response

symbols = pd.read_csv("nasdaq_screener_1649871223347.csv").iloc[:,:2]

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/get")
def get_bot_response():
    req = request.args.get('msg')
    response = get_response(req,symbols)
    return response


if __name__ == "__main__":
    app.run(port=54321)