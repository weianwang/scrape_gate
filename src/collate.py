'''
Created on May 31, 2014

@author: weian
'''
 
#walk down the google list of articles and collate the data with the Gate website article information
 
import csv

from extract_articles import google_articles
from articles_sort_date import articles_list as gate_articles

#default settings if article not found
def print_default(gate_art, writer):
    writer.writerow([art.title, art.category, art.date, art.url, 
                    str(0), str(0), str(0),
                    str(0), str(0), str(0)])
    return

with open('data/[collated]google_pagedata + gate.csv', 'w') as f:
    
    collate_writer = csv.writer(f)
    collate_writer.writerow(['Article Title', 'Category', 'Date', 'URL', 
                             'Pageviews', 'Unique Pageviews', 'Average Time (s)', 
                             'Entrances', 'Bounce Rate', 'Exit Rate'])
    #for art in gate_articles:   
    #check to see if there is google page analytics data about that article
    #i.e. compare by url
    for art in gate_articles:
        for google_art in google_articles:
            default_bool = False
            if google_art.date > art.date:
                default_bool = True
                break #leave the for loop because you have searched too far and the article does not exist
            elif google_art.date < art.date:
                continue
            elif google_art.url == art.url:
                #write the information to the collated file
                title = art.title
                category = art.category
                date = art.date #maybe change to standardized format
                url = art.url
                pviews = google_art.pviews
                unique_pview = google_art.unique_pview
                avgtime = google_art.avgtime
                entrance = google_art.entrance
                bounce = google_art.bounce
                exit_rate = google_art.exit_rate
                collate_writer.writerow([title, category, date, url, pviews, 
                                         unique_pview, avgtime, entrance,
                                         bounce, exit_rate])
                break
        if (default_bool):
            print_default(art, collate_writer)
    f.close
        
    