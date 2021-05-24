#! env python3
import requests
import urllib.request
import validators
import json
from html.parser import HTMLParser
from bs4 import BeautifulSoup as bs

#Comments: (?<=\<\!\-\-)(.*)(?=\-\-\!\>)

class Website:
    def __init__(self, url):
        self.websiteSyntax = json.load(open("./config/website.json", 'r'))

        self.isUrlValid = False
        for i in self.websiteSyntax["tryUrls"]:
            if validators.url(i + url):
                self.isUrlValid = True
                self.url = i+url
                break

    def getInterestingContent(self, source):
        soup = bs(source, 'html.parser')
        #print(soup) 
        for i in self.websiteSyntax["interestingTags"]:
            if i == "script":
                #print(i)
                for script in soup.find_all('script'):
                    print('Found javascript: ')
                    for j in self.websiteSyntax["interestingTags"][i]["content"]:
                        print(j,end="")
            if i == "a":
                for a in soup.find_all('a'):
                    print(' Link at = ' + a['href'])
    def getWebsite(self, url):
        response = urllib.request.urlopen(url)
        return response
        
    def analyse(self):
        source = self.getWebsite(self.url)
        #p = Parse(self.websiteSyntax)
        #p.feed(str(source))
        self.getInterestingContent(source)




































class Parse(HTMLParser):
    def __init__(self, websiteSyntax):
        super().__init__()
        self.reset()
        self.websiteSyntax = websiteSyntax

    def handle_starttag(self, tag, attrs):
        print(tag)
        for i in self.websiteSyntax["interestingTags"]:
            if tag == i:
                print(f"{i}: ", end="")
                for j in self.websiteSyntax["interestingTags"][i]["content"]:
                    if tag == "a":
                        for name,link in attrs:
                            if name == "href":# and link.startswith("http"):
                                print(link)
                                return
                    
                for h in attrs:
                    if j in h:
                        print(j,end="")

                print(" ")
                break

    def handle_data(self, data):
        pass

    def handle_endtag(self, tag):
        pass

