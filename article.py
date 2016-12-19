from bs4 import BeautifulSoup
import utils

def getTags(soup):
    tags = soup.findAll('a',{ 'rel' : 'tag' })
    
    for tag in tags:
        print tag.text


def getArticle(url):
    soup = utils.getPage(url)
    getTags(soup)
    
    return


if __name__ == '__main__':
    getArticle('https://blogs.msdn.microsoft.com/azureedu/2016/12/14/changing-vm-sizes-in-azure/')