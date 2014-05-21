'''
Created on May 20, 2014

@author: weian
'''

#File contains the webscraping script

'''
Web crawler to extract article title, url, and metadata for each article of The Gate, tagged by the six subject titles:
    US, World, Chicago, Opinion, Interviews, Arts & Culture
as well as the 5 blog subsections:
    Rxeform, ShatterZones, Supreme Court Spotlight, UCPU, Cartoons
'''

import Definitions
import csv
import urllib2
from bs4 import BeautifulSoup

with open('gate_articles.csv', 'wb') as csvfile:
    gatewrite = csv.writer(csvfile, dialect='excel')
    gatewrite.writerow(["Article Title", "Article Link", "Category", "Page Number"])
    
    hashMaxPages = Definitions.makeHash()
    #for each element of the hash map
    for topic in hashMaxPages:
        #page_max is maximum number of pages to look through given the topic
        page_max = hashMaxPages[topic].max_pages
        #looks through each page from 1 to page_max - 1
        for page in range(1, page_max):
            #url_extend is specific to the topic
            url_extend = "page/" + str(page)
        
            html_doc = urllib2.urlopen("http://uchicagogate.com/category/" + hashMaxPages[topic].url + url_extend)
            
            #parses html for web page
            soup = BeautifulSoup(html_doc)
            
            #finds the h2tags with attribute class of value "entry-title"
            for link in soup.find_all("h2", { "class" : "entry-title"}):
                #only looks for the first child
                children = link.findChildren(recursive=False)
                
                for child in children:
                    new_title = (child['title'].replace("Permalink to ", "")).encode('ascii', 'ignore')
                    new_link = child['href'].replace("http://uchicagogate.com", "")
                    gatewrite.writerow([new_title, new_link, topic, page])
            
        

