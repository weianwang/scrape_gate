'''
Created on May 31, 2014

@author: weian
'''

#extracts the articles from the google page data
#all article urls begin with '/[year]/[month]/[date]
#extracts date from article urls
#then sorts the articles by date
import csv
from articles_sort_date import qsort as qsort
from Definitions import getDate as getDate
from Definitions import getAge as getAge
from Definitions import INPUT_FILE_NAME, OUTPUT_FILE_NAME, EVENTS_INPUT_FILE, EVENTS_ARTICLES, EVENTS_OTHER
import datetime

#write string of '[number]%' as decimal

def stringPercentStrip(percent):
    return float(percent.strip('%')) / 100.0

#change date in format '#:##:##' into number of sections
def extractSeconds(date):
    return 3600*int(date[0]) + 60*int(date[3:5]) + int(date[6:])
    
class AnalyticsElement:
    url= ''
    date = 0
    age = 0
    pviews = 0
    unique_pview= 0
    avgtime = ''
    entrace = 0
    bounce = 0
    exit_rate = 0

def make_new_element(url, date, pageviews, unique_pview, avgtime, 
                     entrance, bounce, exit_rate):
    elem = AnalyticsElement()
    elem.url = url
    elem.date = date
    elem.age = getAge(date)
    elem.pviews = pageviews
    elem.unique_pview = unique_pview
    elem.avgtime = avgtime
    elem.entrance = entrance
    elem.bounce = bounce
    elem.exit_rate = exit_rate
    return elem

google_articles = []
#read elements into list of articles of object 
with open(INPUT_FILE_NAME, 'r') as f:
    google_read = csv.reader(f)
    #read file into google_articles list
    for row in google_read:
        if not row or not(row[0].startswith('/20')) or row[0].__len__() < 13 or '?' in row[0]: 
            #<13 means not long enough to be article url
            continue
        else:
            url = row[0]
            #date = extract_date(url)
            date = getDate(url)
            pviews = int(row[1].replace(',', ''))
            unique_pview = int(row[2].replace(',', ''))
            avgtime = extractSeconds(row[3])
            entrance = int(row[4].replace(',', ''))
            bounce = stringPercentStrip(row[5])
            exit_rate = stringPercentStrip(row[6])
            elem = make_new_element(url, date, pviews, unique_pview, 
                                    avgtime, entrance,bounce,exit_rate)
            google_articles.append(elem)
                
    f.close

google_articles = qsort(google_articles)
                  
with open (OUTPUT_FILE_NAME, 'w') as g:
    filter_write = csv.writer(g)
    #write the header
    filter_write.writerow(['Article URL', 'Date', 'Age (days)', 'Pageviews', 'Unique Pageviews',
                           'Average Time', 'Entrances', 'Bounce Rate', 'Exit Rate'])
    
    #write each element of sorted list of articles into filtered page data csv file
    for art in google_articles:
        filter_write.writerow([art.url, art.date.isoformat(), str(art.age), 
                               art.pviews, art.unique_pview, art.avgtime, 
                               art.entrance, art.bounce, art.exit_rate])
        
g.close
    
#extract articles for the event pages data 
#literally the same script with some modifications

def isArticle(url):
    return (url.startswith('/20')) and url.__len__() > 12 and (not ('?' in url))

#define lists for articles in events data and other pages in events data
events_articles = []
events_other = []

#define new events_element object which represents one entry in the events page data

class EventsElement:
    url = ''
    date = ''
    age = 0
    total_events = 0

def make_new_event(url, total_events, date, age):
    ev = EventsElement()
    ev.url = url
    ev.total_events = total_events
    ev.date = date
    ev.age = age
    return ev

with open(EVENTS_INPUT_FILE, 'r') as f: 
    events_read = csv.reader(f)
    for row in events_read:
        if not row or not row[0].startswith('/'):
            continue
        else:
            url = row[0]
            total_events = int(row[1])
            if not isArticle(row[0]):
                date = 0
                age = 0
                ev = make_new_event(url, total_events, date, age)
                events_other.append(ev)
            else:
                date = getDate(url)
                age = getAge(date)
                ev = make_new_event(url, total_events, date, age)
                events_articles.append(ev)
f.close
        
with open(EVENTS_OTHER, 'w') as g:
    other_write = csv.writer(g)
    other_write.writerow(['Page', 'Number of Events'])
    for entry in events_other:
        other_write.writerow([entry.url, str(entry.total_events)])
g.close

with open(EVENTS_ARTICLES, 'w') as a:
    articles_write = csv.writer(a)
    articles_write.writerow(['Article Page', 'Date of Publication', 'Number of Events'])
    for entry in events_articles:
        articles_write.writerow([entry.url, entry.date.isoformat(), str(entry.total_events)])
a.close

events_articles = qsort(events_articles)
        