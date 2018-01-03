import requests
import re
import xbmc
import time
from ..scraper import Scraper
from ..common import clean_title,clean_search,random_agent

  
class tubitv(Scraper):
    domains = ['tubitv.com']
    name = "TubiTv"
    sources = []

    def __init__(self):
        self.base_link = 'https://tubitv.com'
        self.start_time = time.time()                                                   # start the timer for the script


    def scrape_movie(self, title, year, imdb, debrid = False):
        try:
            search_id = clean_search(title.lower())                                     # use 'clean_search' to get clean title 
                                                                                        #(movie name keeping spaces removing excess characters)

            start_url = '%s/search/%s' %(self.base_link,search_id.replace(' ','%20'))         # construct search url attributes using site url
            #print '::::::::::::: START URL '+start_url                                  # print to log to confirm 
            
            headers={'User-Agent':random_agent()}
            html = requests.get(start_url,headers=headers,timeout=5).content            # open start_url
            #print html
            match = re.compile('"@type":"Movie","name":"(.+?)","url":"(.+?)".+?"dateCreated":"(.+?)"',re.DOTALL).findall(html) # Regex info on results page
            for name ,item_url, rel in match:
                #print 'item_url>>>>>>>>>>>>>> '+item_url                                # use print statments to confirm grabs check log
                #print 'name>>>>>>>>>>>>>> '+name
                if year in rel:                                                        # confirm year if available in results sometines in name grab/or regex elsewhere
                    
                    if clean_title(search_id).lower() == clean_title(name).lower():     # confirm name use 'clean_title' this will remove all unwanted
                                                                                        # incuding spaces to get both in same format to match if correct
                        #print 'Send this URL> ' + item_url                              # confirm in log correct url(s) sent to get_source
                        self.get_source(item_url)                                       # send url to next stage
            return self.sources
        except:
            pass
            return[]

            
    def get_source(self,item_url):
        try:
            headers={'User-Agent':random_agent()}
            OPEN = requests.get(item_url,headers=headers,timeout=5).content             # open page passed

            Endlinks = re.compile('"video":.+?"url":"(.+?)"',re.DOTALL).findall(OPEN)      # regex to links
            for link in Endlinks:
                link = 'https:'+link.replace('\u002F','/')
                if '1080' in link:
                    label = '1080p'
                elif '720' in link:
                    label = '720p'
                else:
                    label = 'HD'
                #hostname = # this will be diff deppending on site not needed if nameself i.e.'Google' or 'Directlink'
                self.sources.append({'source': 'TubiTv', 'quality': label, 'scraper': self.name, 'url': link,'direct': True}) #this line will depend what sent
            end_time = time.time()  # stops the timer
            total_time = end_time - self.start_time   # finds the total time the scraper ran
            print (repr(total_time))+"<<<<<<<<<<<<<<<<<<<<<<<<<"+self.name+">>>>>>>>>>>>>>>>>>>>>>>>>total_time"  # prints total time to the log         
        except:
            pass
#tubitv().scrape_movie('bullet boy', '2005','') 
# you will need to regex/split or rename to get host name if required from link unless available on page it self 