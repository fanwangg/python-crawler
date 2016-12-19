from bs4 import BeautifulSoup
import requests

def getPage(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text)

    return soup
