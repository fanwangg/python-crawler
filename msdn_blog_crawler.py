from bs4 import BeautifulSoup
import utils

START_PAGE = 'https://blogs.msdn.microsoft.com/'

def getNextPageLink(soup):
    next = soup.find('a', { 'class' : 'next' })
    return next['href'] if next is not None else None

def getList(url):
    soup = getArticle(url)

def main():
    url = START_PAGE
    while url is not None:
        soup = utils.getPage(url)
        for title in soup.findAll('h2', { "class" : "entry-title" }):
            print title.text
            #getArticle(title['href'])
        
        print getNextPageLink(soup)
        url = getNextPageLink(soup)
    
    print "Crawling finished!" 

if __name__ == '__main__':
    main()