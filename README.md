# The Gate Web Scraper

Author: Weian Wang

Work in progress. 
Lacks portability, but suffices to collect data for The Gate project with Data Analysts for Social Good at UChicago. 
The Gate is a publication at the University of Chicago (uchicagogate.com).
Data included is relevant as of June 02, 2014.

## Contains: 
* Definitions.py
This defines the sections of the website to scrape from.
* Spider.py
This is the actual scraper that extracts the data and writes to .csv file in specific format. 
* extract_articles.py
This extracts the data for Gate articles from the Google Analytics Page Data from May 24, 2013 to June 02, 2014. Also, uses quicksort to sort the articles by date in increasing order.
* articles_sort_date.py
Uses quicksort algorithm to sort the Gate articles in gate_articles.csv
* collate.py
Collates data from gates_articles_datesort.csv and the filtered google page data ([filtered]google_pagedata_complete.csv).

## Additions and Future Plans:
Now we add age! 

## How to Use:
Generally, to read a CSV file, you can use Excel, go to Data tab on the header ribbon, go to Get External Data, click From Text. Open the CSV file, then set the Delimiter to 'Comma'. 
