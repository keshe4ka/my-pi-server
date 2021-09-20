from config import anecdote_url
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from time import sleep
import random


def get_joke():
    try:
        session = HTMLSession()
        response = session.get(f"{anecdote_url}{random.randint(1, 1142)}")
        sleep(2)
        BeautifulSoup(response.content, 'html.parser')
        soup = BeautifulSoup(response.content, 'html.parser')
        anecdote = soup.find('p').get_text()
        return anecdote
    except Exception as ex:
        return f"Никаких приколов... \n{ex}"
