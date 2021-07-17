from flask import Flask, request, jsonify
from scraper import get_news

app = Flask(__name__)

@app.route('/')
def index():
    return "This is the index of the news api"

@app.route('/get-news')
def send_news():
    news_number = int(request.args.get('number'))
    news = get_news()
    return jsonify(news[5*(news_number-1): news_number*5])

