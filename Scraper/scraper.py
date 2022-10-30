import requests 
from bs4 import BeautifulSoup
import re
import string
import sys
import argparse

parser = argparse.ArgumentParser(description='Scrape entrepreneurship\'s articles !')
parser.add_argument('--tag', type=int,
                    default=0,
                    help='choosing what category of articles')

args = parser.parse_args()

print(args.tag)


File = "articles.txt"


f = open(File, 'w+', encoding="utf-8")

def ScrapePoems (URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find('article')
    #job_elements = results.find_all("div", class_="card-content")
    Poems = results.find("div", {'class':'cs-entry__outer'}).find("div", {'class':'cs-entry__inner cs-entry__content'}).find_all("h2")

    '''
    for poem in Poems:
        f.write(poem.text.strip()+'\n')
    Poems = results.find_all("h4")
    '''
    for poem in Poems:
        #f.write(poem.text.strip()+'\n')
        print(poem.text)

BaseURL = "https://startupnation.com/category/start-your-business"
AuthURL = "https://startupnation.com/category/start-your-business/get-inspired/"
page = requests.get(AuthURL)
soup = BeautifulSoup(page.content, "html.parser")
allTab = soup.find_all("div", class_="record col-12")
for tab in allTab:
    htmlUrl = tab.find("a", class_="float-right")['href']
    print(htmlUrl)
    ScrapePoems(BaseURL+htmlUrl)

f.close()



f = open(File, 'r', encoding="utf-8")
dataset = f.read()
cleaned = open(poets[poet_number]+'-clean.txt', 'w+',encoding="utf-8")
cleaned.write(dataset)
f.close()
cleaned.close()