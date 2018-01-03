import re
import requests
import xbmc,time
import urllib
from ..scraper import Scraper
from ..common import clean_title,clean_search

User_Agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4'


class uwatchfree(Scraper):
    domains = ['https://www.uwatchfree.to']
    name = "uwatchfree"
    sources = []

    def __init__(self):
        self.base_link = 'https://www.uwatchfree.to/'
        self.sources = []
        self.start_time = time.time()

    def scrape_movie(self, title, year, imdb, debrid=False):
        try:
            search_id = clean_search(title.lower())
            start_url = '%s?s=%s' %(self.base_link,search_id.replace(' ','+'))
            headers = {'User_Agent':User_Agent}
            html = requests.get(start_url,headers=headers,timeout=5).content
            Regex = re.compile('class="entry-title"><a href="(.+?)".+?rel="bookmark">(.+?)</a>',re.DOTALL).findall(html)
            for item_url,name in Regex:
                if 'Dubbed' not in name:
                    if clean_title(title).lower() == clean_title(name).lower():
                        if year in name:
                            movie_link = item_url
                            self.get_source(movie_link)
                
            return self.sources
        except Exception, argument:
            return self.sources

    def scrape_episode(self,title, show_year, year, season, episode, imdb, tvdb, debrid = False):
        try:
            search_id = clean_search(title.lower())
            season_get = '0%s' %season if len(season) <2 else season
            episode_get = '0%s' %episode if len(episode) <2 else episode
            s_ep = 's%se%s' %(season_get,episode_get)
            start_url = '%s?s=%s+%s' %(self.base_link,search_id.replace(' ','+'),s_ep)
            headers = {'User_Agent':User_Agent}
            html = requests.get(start_url,headers=headers,timeout=5).content
            Regex = re.compile('class="entry-title"><a href="(.+?)".+?rel="bookmark">(.+?)</a>',re.DOTALL).findall(html)
            for item_url,name in Regex:
                if 'Dubbed' not in name:
                    if clean_title(title).lower() in clean_title(name).lower():
                        show_link = item_url
                        self.get_source(show_link)
                
            return self.sources
        except Exception, argument:
            return self.sources

    def get_source(self,movie_link):
        try:
            html = requests.get(movie_link).content
            sources = re.compile('style="text-align:center".+?href="(.+?)"',re.DOTALL).findall(html)
            for link in sources:
                if 'openload' in link:                   
                    try:
                        headers = {'User_Agent':User_Agent}
                        get_res=requests.get(link,headers=headers,timeout=5).content
                        rez = re.compile('description" content="(.+?)"',re.DOTALL).findall(get_res)[0]
                        if '1080p' in rez:
                            qual = '1080p'
                        elif '720p' in rez:
                            qual='720p'
                        else:
                            qual='DVD'
                    except: qual='DVD'        
                    self.sources.append({'source': 'Openload','quality': qual,'scraper': self.name,'url': link,'direct': False})
                    end_time = time.time()
                    total_time = end_time - self.start_time
                    print (repr(total_time))+"<<<<<<<<<<<<<<<<<<<<<<<<<"+self.name+">>>>>>>>>>>>>>>>>>>>>>>>>total_time"
                else: 
                    qual = 'DVD'
                    host = link.split('//')[1].replace('www.','')
                    host = host.split('/')[0].split('.')[0].title()
                    self.sources.append({'source': host,'quality': qual,'scraper': self.name,'url': link,'direct': False})
                    end_time = time.time()
                    total_time = end_time - self.start_time
                    print (repr(total_time))+"<<<<<<<<<<<<<<<<<<<<<<<<<"+self.name+">>>>>>>>>>>>>>>>>>>>>>>>>total_time"
        except:
            pass

