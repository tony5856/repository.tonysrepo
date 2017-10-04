# -*- coding: utf-8 -*-
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: Hema addon
# Author: Tony H

#----------------------------------------------------------------


import os          
import urlparse     
import xbmc         
import xbmcaddon    
import xbmcgui      
import xbmcplugin   
import koding       
import nanscrapers  
from koding import Add_Dir  
from koding import route, Run 
from koding import route, Addon_Setting, Add_Dir, Find_In_Text, Open_URL, OK_Dialog
from koding import Open_Settings, Play_Video, Run, Text_File


#----------------------------------------------------------------


addon_id     = xbmcaddon.Addon().getAddonInfo('id') 
dialog       = xbmcgui.Dialog()                     
home_folder  = xbmc.translatePath('special://home/')
addon_folder = os.path.join(home_folder,'addons')   
art_path     = os.path.join(addon_folder,addon_id)  
debug        = koding.Addon_Setting('debug')        

#-----------------------------------------------------------------
BASE  = "plugin://plugin.video.youtube/playlist/"
BASE2 = "plugin://plugin.video.youtube/channel/"
BASE3 = "play/?video_id="

#-----------------------------------------------------------------
YOUTUBE_CHANNEL_ID_1 = "PLMUtS78ZxryOMRve8RkM0vcrIKPH3hGvW"
YOUTUBE_CHANNEL_ID_2 = "PLEuh65T7K4AtWpLiGJA5oCYtzk1udvYFu"
YOUTUBE_CHANNEL_ID_3 = "PL5HYPAzXbpa_lgPhgIxbyVdhN8lXpCHj2"
YOUTUBE_CHANNEL_ID_4 = "PLF3F2054F1887973C"
YOUTUBE_CHANNEL_ID_5 = "PL83FE40331F44D000"
YOUTUBE_CHANNEL_ID_6 = "PLdWDeIG3CteI22hccYUlxJ4zbnf4mofhh"
YOUTUBE_CHANNEL_ID_7 = "PL0rZ1wLYkmlA0U8iEWuuMhuRAXAcCLkmH"
YOUTUBE_CHANNEL_ID_8 = "PL2209B3BD07634DAE"
YOUTUBE_CHANNEL_ID_9 = "PLvRHYcOclO35UIqjjmVbBpS0paGM97XTf"
YOUTUBE_CHANNEL_ID_10 = "PLd2h238qtqK0AM1h8655rRADSNHuh9Gnw"
YOUTUBE_CHANNEL_ID_11 = "PL5084576A549E4F11"
YOUTUBE_CHANNEL_ID_12 = "PLfy02e1QKKX1XMeXDVXexl5dTSNXnnr78"
YOUTUBE_CHANNEL_ID_13 = "PLyRss2jWg0xUrTDiP-xP6a8V0p3gbzAXZ"
YOUTUBE_CHANNEL_ID_14 = "PLplqGmqDeEOjZhij_Ao7uZgS34ivKUTdz"
YOUTUBE_CHANNEL_ID_15 = "PLMUtS78ZxryNYFe-Z4jV_KxQ2sQaevrUz"
YOUTUBE_CHANNEL_ID_16 = "PLgRb6yZYwVwtlLbKxx0lkw1r9RTOmigqb"
YOUTUBE_CHANNEL_ID_17 = "PLcAQ0Ggu3vX7YFB8wYnxl1_fxelPo9L_0"
YOUTUBE_CHANNEL_ID_18 = "PLVB84gy7xLgps5DLLvwWqTwAESyUVYsdH"
YOUTUBE_CHANNEL_ID_19 = "PLt9EEb18Gpa1KrDxdH-LHddplbbGqcPMo"
YOUTUBE_CHANNEL_ID_20 = "PLV0B7A11Iz73DKi5jRltdtjV6ywwrE-dL"
YOUTUBE_CHANNEL_ID_21 = "PLd7_5iapCCKNlpRsT7rd-flK_HcYvwel5"
YOUTUBE_CHANNEL_ID_22 = "PLNL0GGBxaNGEUkvyYKuFGJ6N2NsRdAi2s"
YOUTUBE_CHANNEL_ID_23 = ""

#----------------------------------------------------------------

@route(mode="main")
def Main_Menu():

    Add_Dir(name='Traing Videos', url='', mode='open_folder', folder=True, icon="http://tonyh.net/backgrounds/hema%20images/icon3.png", fanart="http://tonyh.net/backgrounds/hema%20images/be3c602b82ff4db87f6317a8794a7777.jpg")
    Add_Dir(name='Fighting Videos', url='', mode='open_folder2', folder=True, icon="http://tonyh.net/backgrounds/hema%20images/icon12.png.jpg", fanart="http://tonyh.net/backgrounds/hema%20images/be3c602b82ff4db87f6317a8794a7777.jpg")
    Add_Dir(name='Equipment', url='', mode='open_folder3', folder=True, icon="http://tonyh.net/backgrounds/hema%20images/icon12.png.jpg", fanart="http://tonyh.net/backgrounds/hema%20images/be3c602b82ff4db87f6317a8794a7777.jpg")
    Add_Dir(name='M1 Medieval Fighting', url='', mode='open_folder4', folder=True, icon="http://tonyh.net/backgrounds/hema%20images/icon12.png.jpg", fanart="http://tonyh.net/backgrounds/hema%20images/be3c602b82ff4db87f6317a8794a7777.jpg")

#-----------------------------------------------------------------

@route(mode="open_folder", args=["url"])
def Test_Folder(url):

       
        Add_Dir( 
        name="Sword Fighting", url=BASE+YOUTUBE_CHANNEL_ID_1+"/", folder=True,
        icon="http://tonyh.net/backgrounds/hema%20images/icon2.png", fanart="http://tonyh.net/backgrounds/hema%20images/be3c602b82ff4db87f6317a8794a7777.jpg")
       
        Add_Dir( 
        name="Turorials", url=BASE+YOUTUBE_CHANNEL_ID_2+"/", folder=True,
        icon="http://tonyh.net/backgrounds/hema%20images/icon5.png", fanart="http://tonyh.net/backgrounds/hema%20images/be3c602b82ff4db87f6317a8794a7777.jpg")
       
        Add_Dir( 
        name="Training Exercises", url=BASE+YOUTUBE_CHANNEL_ID_3+"/", folder=True,
        icon="http://tonyh.net/backgrounds/hema%20images/icon9.png.jpg", fanart="http://tonyh.net/backgrounds/hema%20images/be3c602b82ff4db87f6317a8794a7777.jpg")

        Add_Dir( 
        name="More Training Exercises", url=BASE+YOUTUBE_CHANNEL_ID_4+"/", folder=True,
        icon="http://tonyh.net/backgrounds/hema%20images/icon8.png.jpg", fanart="http://tonyh.net/backgrounds/hema%20images/be3c602b82ff4db87f6317a8794a7777.jpg")

        Add_Dir( 
        name="More Training Exercises 2", url=BASE+YOUTUBE_CHANNEL_ID_5+"/", folder=True,
        icon="http://tonyh.net/backgrounds/hema%20images/icon7.png.jpg", fanart="http://tonyh.net/backgrounds/hema%20images/be3c602b82ff4db87f6317a8794a7777.jpg")

        Add_Dir( 
        name="Sword and Shield sparring", url=BASE+YOUTUBE_CHANNEL_ID_13+"/", folder=True,
        icon="http://tonyh.net/backgrounds/hema%20images/icon7.png.jpg", fanart="http://tonyh.net/backgrounds/hema%20images/be3c602b82ff4db87f6317a8794a7777.jpg")





@route(mode="open_folder2", args=["url"])
def Test_Folder(url):

        
        Add_Dir( 
        name="HEMA Matches", url=BASE+YOUTUBE_CHANNEL_ID_6+"/", folder=True,
        icon="http://tonyh.net/backgrounds/hema%20images/icon11.png.jpg", fanart="http://tonyh.net/backgrounds/hema%20images/maxresdefault.jpg")

        Add_Dir( 
        name="Tournaments and Training", url=BASE+YOUTUBE_CHANNEL_ID_7+"/", folder=True,
        icon="http://tonyh.net/backgrounds/hema%20images/icon11.png.jpg", fanart="http://tonyh.net/backgrounds/hema%20images/maxresdefault.jpg")

        Add_Dir( 
        name="Tournament Fights", url=BASE+YOUTUBE_CHANNEL_ID_8+"/", folder=True,
        icon="http://tonyh.net/backgrounds/hema%20images/icon11.png.jpg", fanart="http://tonyh.net/backgrounds/hema%20images/maxresdefault.jpg")

        Add_Dir( 
        name="War in the West 2016", url=BASE+YOUTUBE_CHANNEL_ID_9+"/", folder=True,
        icon="http://tonyh.net/backgrounds/hema%20images/icon11.png.jpg", fanart="http://tonyh.net/backgrounds/hema%20images/maxresdefault.jpg")

        Add_Dir( 
        name="ILHG 2017 Tournament", url=BASE+YOUTUBE_CHANNEL_ID_10+"/", folder=True,
        icon="http://tonyh.net/backgrounds/hema%20images/icon11.png.jpg", fanart="http://tonyh.net/backgrounds/hema%20images/maxresdefault.jpg")

        Add_Dir( 
        name="PNWG12 Longsword", url=BASE+YOUTUBE_CHANNEL_ID_11+"/", folder=True,
        icon="http://tonyh.net/backgrounds/hema%20images/icon11.png.jpg", fanart="http://tonyh.net/backgrounds/hema%20images/maxresdefault.jpg")

        Add_Dir( 
        name="Sonora Celtic Faire 2014", url=BASE+YOUTUBE_CHANNEL_ID_12+"/", folder=True,
        icon="http://tonyh.net/backgrounds/hema%20images/icon11.png.jpg", fanart="http://tonyh.net/backgrounds/hema%20images/maxresdefault.jpg")

@route(mode="open_folder3", args=["url"])
def Test_Folder(url):

        
        Add_Dir( 
        name="HEMA Equipment", url=BASE+YOUTUBE_CHANNEL_ID_14+"/", folder=True,
        icon="https://pbs.twimg.com/profile_images/744534448327143424/28bfiuHP.jpg", fanart="http://tonyh.net/backgrounds/hema%20images/offhand.jpg")

        Add_Dir( 
        name="HEMA Weapons and equipment", url=BASE+YOUTUBE_CHANNEL_ID_15+"/", folder=True,
        icon="https://cdn.shopify.com/s/files/1/0860/2834/collections/Rawlings_HEMA_Swords_grande.jpg?v=1434929549", fanart="http://tonyh.net/backgrounds/hema%20images/offhand.jpg")

        Add_Dir( 
        name="Equipment Reviews", url=BASE+YOUTUBE_CHANNEL_ID_16+"/", folder=True,
        icon="https://cdn.shopify.com/s/files/1/0860/2834/collections/Rawlings_HEMA_Swords_grande.jpg?v=1434929549", fanart="http://tonyh.net/backgrounds/hema%20images/offhand.jpg")

@route(mode="open_folder4", args=["url"])
def Test_Folder(url):

        
        Add_Dir( 
        name="M1 Medieval Combat", url=BASE+YOUTUBE_CHANNEL_ID_17+"/", folder=True,
        icon="https://pbs.twimg.com/profile_images/592392752446312448/NwUVIpcM.png", fanart="https://i.ytimg.com/vi/_DLLFx013QU/maxresdefault.jpg")

        Add_Dir( 
        name="M1 Global", url=BASE+YOUTUBE_CHANNEL_ID_18+"/", folder=True,
        icon="https://pbs.twimg.com/profile_images/592392752446312448/NwUVIpcM.png", fanart="https://i.ytimg.com/vi/_DLLFx013QU/maxresdefault.jpg")

        Add_Dir( 
        name="Medieval Combat", url=BASE+YOUTUBE_CHANNEL_ID_19+"/", folder=True,
        icon="https://pbs.twimg.com/profile_images/592392752446312448/NwUVIpcM.png", fanart="https://i.ytimg.com/vi/_DLLFx013QU/maxresdefault.jpg")

        Add_Dir( 
        name="World Championship 2015 plus other", url=BASE+YOUTUBE_CHANNEL_ID_20+"/", folder=True,
        icon="https://pbs.twimg.com/profile_images/592392752446312448/NwUVIpcM.png", fanart="https://i.ytimg.com/vi/_DLLFx013QU/maxresdefault.jpg")

        Add_Dir( 
        name="World Championship 2014 plus other", url=BASE+YOUTUBE_CHANNEL_ID_21+"/", folder=True,
        icon="https://pbs.twimg.com/profile_images/592392752446312448/NwUVIpcM.png", fanart="https://i.ytimg.com/vi/_DLLFx013QU/maxresdefault.jpg")

        Add_Dir( 
        name="2015-2017 Many Matches!", url=BASE+YOUTUBE_CHANNEL_ID_22+"/", folder=True,
        icon="https://pbs.twimg.com/profile_images/592392752446312448/NwUVIpcM.png", fanart="https://i.ytimg.com/vi/_DLLFx013QU/maxresdefault.jpg")

# Example single youtube video

        #Add_Dir( 
        #name="National Geographic | Colonizing Space", url=BASE3+YOUTUBE_CHANNEL_ID_30, folder=False, mode='play_yt',
        #icon="http://www.thehtpc.net/wp-content/gallery/imagesbyname/xz_genre_preview.png", fanart="https://i.pinimg.com/originals/5c/e1/44/5ce144f88cc4c2327279b97f14a5b486.jpg")


#----------------------------------------------------------------

#Play a youtube video
@route(mode="play_yt", args=["url"])
def Play_YT(url):
    
    xbmc.executebuiltin('PlayMedia(plugin://plugin.video.youtube/%s)'%url)
#------------------------------------------------------------------


if __name__ == "__main__":
    Run(default='main')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))