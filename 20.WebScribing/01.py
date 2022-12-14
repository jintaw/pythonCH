import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site
        
    def scrape(self):
        response = urllib.request.urlopen(self.site)
        html = response.read()
        parser = "html.parser"
        sp = BeautifulSoup(html , "html.parser")
        
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url and "article" in url:
                
                print("\n" + url)

news = "https://news.google.com/"
Scraper(news).scrape()
