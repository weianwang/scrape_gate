'''
Created on May 31, 2014

@author: weian
'''
 
#walk down the google list of articles and collate the data with the Gate website article information
 
import csv

from extract_articles import google_articles, events_articles
from articles_sort_date import articles_list as gate_articles
from Definitions import COLLATED_FILE
from Definitions import EVENTS_COLLATED
import datetime

#default settings if article not found
def print_default(gate_art, writer):
    writer.writerow([art.title, art.category, art.date.isoformat(), str(art.age), art.url, 
                    str(0), str(0), str(0),
                    str(0), str(0), str(0)])
    return

with open(COLLATED_FILE, 'w') as f:
    
    collate_writer = csv.writer(f)
    collate_writer.writerow(['Article Title', 'Category', 'Date', 'Age (days)', 'URL', 
                             'Pageviews', 'Unique Pageviews', 'Average Time (s)', 
                             'Entrances', 'Bounce Rate', 'Exit Rate'])
    #for art in gate_articles:   
    #check to see if there is google page analytics data about that article
    #i.e. compare by url
    for art in gate_articles:
        for google_art in google_articles:
            default_bool = False
            if google_art.age> art.age:
                default_bool = True
                break #leave the for loop because you have searched too far and the article does not exist
            elif google_art.age < art.age:
                continue
            elif google_art.url == art.url:
                #write the information to the collated file
                title = art.title
                category = art.category
                date = art.date
                url = art.url
                age = str(art.age)
                pviews = google_art.pviews
                unique_pview = google_art.unique_pview
                avgtime = google_art.avgtime
                entrance = google_art.entrance
                bounce = google_art.bounce
                exit_rate = google_art.exit_rate
                collate_writer.writerow([title, category, date.isoformat(), 
                                         str(age), url, pviews, 
                                         unique_pview, avgtime, entrance,
                                         bounce, exit_rate])
                break
            else:
                break
        if (default_bool):
            print_default(art, collate_writer)
f.close
        
# events data collating
with open(EVENTS_COLLATED, 'w') as c:
    events_writer = csv.writer(c)
    events_writer.writerow(['Url', 'Age (days)', 
                             'Total Events', 'Pageviews', 'Entrances'])
    for art in google_articles:
        for events_art in events_articles:
            if events_art.age > art.age:
                break
            elif events_art.age < art.age:
                continue
            elif events_art.url == art.url:
                events_writer.writerow([art.url, str(art.age), 
                                        str(events_art.total_events), art.pviews, art.entrance])
            else:
                break

c. close