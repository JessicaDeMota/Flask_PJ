from flask import Flask, render_template, url_for
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def web_scrape(url):
    searching = requests.get(url)
    soup = BeautifulSoup(searching.text)
    #a_tags = soup.findAll('a')
    # Do some extraction magic here
    return date, views, likes, dislikes


@app.route('/')
def home():
    
    views,likes,tables  = web_scrape("https://www.youtube.com/watch?v=IyTl5avi3eM")
    views = s.find("span", class ="watch-title").text.replace("\n"," ")
    likes = s.find("spam", class = "like-button-renderer").span.button.text 
    return render_template("home.html", date=date, views=views, likes=likes, dislikes=dislikes)
    # data = web_scrape()



class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

if __name__ == '__main__':
    app.run(debug=True)