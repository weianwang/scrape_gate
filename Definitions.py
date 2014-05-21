'''
Created on May 21, 2014

@author: weian
'''

#File containing the data structure definitions and hash map definition

'''
Creates hash table corresponding to maximum number of pages in each section
for now, the maximum number of pages in each section is manually entered. 
will be updating with better method
Relevant as of May 21, 2014
'''
    
'''
Topic() is a data structure that contains the maximum number of pages per topic and the associated url extension
''' 
    
class Topic:
    max_pages = 0
    url = ""
    
def make_new_topic(max_pages, url):
    top = Topic()
    top.max_pages = max_pages
    top.url = url
    return top

#working on making this more portable
#will be hard-coded, because small dataset
def makeHash():
#defining topics
#difficult to make, because url and subject are not standardized (i.e. "US" and "national/") 
    hashTopics = {}
    hashTopics["US"] = make_new_topic(10, "national/")
    hashTopics["World"] = make_new_topic(14, "world/")   
    hashTopics["Chicago"] = make_new_topic(9, "chicago/")  
    hashTopics["Opinions"] = make_new_topic(5, "opinion/")
    hashTopics["Interviews"] = make_new_topic(5, "interviews/")
    hashTopics["Arts & Culture"] = make_new_topic(5, "culture/")
    
    #blog topics
    hashTopics["Column: Rxeform"] = make_new_topic(5, "columns/rxeform/")
    hashTopics["Column: Shatter Zones"] = make_new_topic(3, "columns/shatterzones/")
    hashTopics["Column: Supreme Court Spotlight"] = make_new_topic(4, "columns/supremecourtspotlight/")
    hashTopics["Column: UCPU"] = make_new_topic(2, "columns/ucpu/")
    hashTopics["Column: Cartoons"] = make_new_topic(2, "columns/cartoons/")
    return hashTopics