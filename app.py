from flask import Flask, request, jsonify
from scraper import get_news
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def index():
    return "This is the index of the news api"

@app.route('/get-news')
@cross_origin()
def send_news():
    news_number = int(request.args.get('number'))
    news = get_news()
    return jsonify(news[5*(news_number-1): news_number*5])


if __name__ == "__main__":
    app.run(debug=True)
    