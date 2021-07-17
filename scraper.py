from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def html_to_dictionary(html):
    res = {
        "title": html.h2.get_text(),
        "date": html.time.get_text(),
        "description": html.p.get_text()
    }
    return res



def get_news():
    i = 1
    all_news = list()
    while(i <= 5):
        page = requests.get(
        f'https://economictimes.indiatimes.com/topic/farmers/{i}', headers=headers)
        soup = BeautifulSoup(page.content, features="html.parser")
        page_news = soup.find_all("div", {"class": "clr flt topicstry story_list"})
        for news in page_news:
            all_news.append(html_to_dictionary(news))
        i+= 1


    return all_news
