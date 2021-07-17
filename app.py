from flask import Flask, request, jsonify
from scraper import get_news

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def index():
    return "This is the index of the news api"

@app.route('/get-news')
def send_news():
    news_number = int(request.args.get('number'))
    news = get_news()
    response = jsonify(news[5*(news_number-1): news_number*5])
    response.headers.add("Access-Control-Allow-Origin", "*");
    return response


if __name__ == "__main__":
    app.run(debug=True)
