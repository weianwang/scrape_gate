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
from Definitions import extract_date as extract_date

#write string of '[number]%' as decimal

def stringPercentStrip(percent):
    return float(percent.strip('%')) / 100.0

#change date in format '#:##:##' into number of sections
def extractSeconds(date):
    return 3600*int(date[0]) + 60*int(date[3:5]) + int(date[6:])
    
class AnalyticsElement:
    url= ''
    date = 0
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
    elem.pviews = pageviews
    elem.unique_pview = unique_pview
    elem.avgtime = avgtime
    elem.entrance = entrance
    elem.bounce = bounce
    elem.exit_rate = exit_rate
    return elem

google_articles = []
#read elements into list of articles of object 
with open('data/[original]google_pagedata_0201-0531.csv', 'r') as f:
    google_read = csv.reader(f)
    #read file into google_articles list
    for row in google_read:
        if not row or not(row[0].startswith('/20')):
            continue
        else:
            url = row[0]
            date = extract_date(url)
            pviews = int(row[1])
            unique_pview = int(row[2])
            avgtime = extractSeconds(row[3])
            entrance = int(row[4])
            bounce = stringPercentStrip(row[5])
            exit_rate = stringPercentStrip(row[6])
            elem = make_new_element(url, date, pviews, unique_pview, 
                                    avgtime, entrance,bounce,exit_rate)
            google_articles.append(elem)
                
    f.close

google_articles = qsort(google_articles)
                  
with open ('data/[filtered]google_pagedata_0201-0531.csv', 'w') as g:
    filter_write = csv.writer(g)
    #write the header
    filter_write.writerow(['Article URL', 'Date', 'Pageviews', 'Unique Pageviews',
                           'Average Time', 'Entrances', 'Bounce Rate', 'Exit Rate'])
    
    #write each element of sorted list of articles into filtered page data csv file
    for art in google_articles:
        filter_write.writerow([art.url, art.date, art.pviews, art.unique_pview,
                               art.avgtime, art.entrance, art.bounce, art.exit_rate])
        
    g.close
    
