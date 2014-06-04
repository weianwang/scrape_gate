'''
Created on May 20, 2014

@author: weian
'''
#Simple sorting after reading CSV will article titles by date 
#Should sort existing gate_articles csv file

import csv
from datetime import date
from Definitions import getDate
from Definitions import getAge

class Article:
    title = ''
    url = ''
    date = 0
    age = 0
    category = ''
    page_number = 0

def make_new_article(title, url, date, category, page_number):
    art = Article()
    art.title = title
    art.url = url
    art.date = date
    art.age = getAge(date)
    art.category = category
    art.page_number = page_number
    return art

articles_list = []
with open('data/gate_articles.csv', 'r') as f:
    gate_Reader = csv.reader(f)
    f.readline()
    for row in gate_Reader:
        title = row[0]
        url = row[1]
        date = getDate(url)
        age = row[3]
        category = row[4]
        page_number = row[5]
        article = make_new_article(title, url, date, category, page_number)
        articles_list.append(article)
f.close

#checking to make sure list is made of article opjects

#now implementing quicksort algorithm
#will sort Article objects in articles_list by their date

#qsort sorts a list of data objects that have the 'date' field
def qsort(lst):
    if len(lst) <= 1:
        return lst
    less = []
    equal = []
    greater = []
    
    pivot = lst[0]
    for art in lst:
        if art.age < pivot.age:
            less.append(art)
        elif art.age == pivot.age:
            equal.append(art)
        elif art.age > pivot.age:
            greater.append(art)
        
    return qsort(less) + equal + qsort(greater)
        
articles_list = qsort(articles_list)

#write sorted list to csv

with open('data/gate_articles_datesort.csv', 'w') as f:
    date_writer = csv.writer(f)
    date_writer.writerow(["Article Title", "Article Link", "Date", "Age (Days)", "Category", "Page Number"])
    for art in articles_list:
        title = art.title
        url = art.url
        date = art.date
        age = art.age
        category = art.category
        page_number = art.page_number
        date_writer.writerow([title, url, date.isoformat(), str(age), category, page_number])
    
f.close