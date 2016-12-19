from bs4 import BeautifulSoup
import utils

class Author:
    def __init__(self, id):
        self.id = id

def createAuthorFromURL(url):
    return Author(url.split('/')[-1])


if __name__ == '__main__':
    author = createAuthorFromURL('https://social.msdn.microsoft.com/profile/DataPlatJP')
    print author.id