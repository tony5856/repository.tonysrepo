# -*- coding: utf-8 -*-
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: National Geographic addon
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
#------------------------------------------------

BASE  = "plugin://plugin.video.youtube/playlist/"
BASE2 = "plugin://plugin.video.youtube/channel/"
BASE3 = "play/?video_id="
fanart1 = "https://wallpapercave.com/wp/1asM6jP.jpg"
fanart2 = "http://renatures.com/wp-content/uploads/2016/11/beaches-ocean-nature-skay-blue-beach-wallpaper-1920x1080.jpg"
#------------------------------------------------


YOUTUBE_CHANNEL_ID_1 = "PLivjPDlt6ApT5VT7oiz7riKmPzkl2sAe0"
YOUTUBE_CHANNEL_ID_2 = "PLivjPDlt6ApTqKN6DbR-GOM5omen0Xm2a"
YOUTUBE_CHANNEL_ID_3 = "PLivjPDlt6ApS5FeUq8c-I7WWPVx3W0blc"
YOUTUBE_CHANNEL_ID_4 = "PLivjPDlt6ApSV6IhEzPW2w60mwFVtXgNR"
YOUTUBE_CHANNEL_ID_5 = "PLivjPDlt6ApTjurXykShuUqp7LQcj9s8s"
YOUTUBE_CHANNEL_ID_6 = "PLivjPDlt6ApS90YoAu-T8VIj6awyflIym"
YOUTUBE_CHANNEL_ID_7 = "PLivjPDlt6ApQSSkIRRlEkpxMj-6V7Z5VM"
YOUTUBE_CHANNEL_ID_8 = "PLivjPDlt6ApTD6p2dgWr44nFi-J8xbIGe"
YOUTUBE_CHANNEL_ID_9 = "PLivjPDlt6ApRfrpHJMdcrhYjAEwa02AhY"
YOUTUBE_CHANNEL_ID_10 = ""
YOUTUBE_CHANNEL_ID_11 = ""
YOUTUBE_CHANNEL_ID_12 = ""
YOUTUBE_CHANNEL_ID_13 = ""
YOUTUBE_CHANNEL_ID_14 = ""
YOUTUBE_CHANNEL_ID_15 = ""
YOUTUBE_CHANNEL_ID_16 = ""
YOUTUBE_CHANNEL_ID_17 = ""
YOUTUBE_CHANNEL_ID_18 = ""
YOUTUBE_CHANNEL_ID_19 = ""
YOUTUBE_CHANNEL_ID_20 = ""



#-----------------------------------------------------------

@route(mode="main")
def Main_Menu():


    Add_Dir(name='Huge Playlists updated Daily', url='', mode='open_folder', folder=True, icon="http://www.thegsa.co.za/images/directory/national_geographic_explorer/nationalgeographiclogo_resized.png", fanart="https://i.ytimg.com/vi/Fs3IQXKGC5o/maxresdefault.jpg")
    Add_Dir(name='Special Playlists', url='', mode='open_folder2', folder=True, icon="http://the-door.net/cinema/wp-content/uploads/2012/12/National-Geographic-Live-Main-Image1.png", fanart="https://i.ytimg.com/vi/Fs3IQXKGC5o/maxresdefault.jpg")



#-----------------------------

@route(mode="open_folder", args=["url"])
def Test_Folder(url):
        
        Add_Dir( 
        name="Adventure & Survival", url=BASE+YOUTUBE_CHANNEL_ID_1+"/", folder=True,
        icon="http://tonyh.net/icons/nat%20geo/adventure.png", fanart=fanart1)
       
        Add_Dir( 
        name="Exploration", url=BASE+YOUTUBE_CHANNEL_ID_2+"/", folder=True,
        icon="http://tonyh.net/icons/nat%20geo/exploration.png", fanart=fanart1)
       
        Add_Dir( 
        name="Fun Facts", url=BASE+YOUTUBE_CHANNEL_ID_3+"/", folder=True,
        icon="http://tonyh.net/icons/nat%20geo/fun_facts.png", fanart=fanart1)

        Add_Dir( 
        name="History & Culture", url=BASE+YOUTUBE_CHANNEL_ID_4+"/", folder=True,
        icon="http://tonyh.net/icons/nat%20geo/history.png", fanart=fanart1)

        Add_Dir( 
        name="Nature & Enviroment", url=BASE+YOUTUBE_CHANNEL_ID_5+"/", folder=True,
        icon="http://tonyh.net/icons/nat%20geo/nature.png", fanart=fanart1)

        Add_Dir( 
        name="Science", url=BASE+YOUTUBE_CHANNEL_ID_6+"/", folder=True,
        icon="http://tonyh.net/icons/nat%20geo/science.png", fanart=fanart1)

#-----------------------------

@route(mode="open_folder2", args=["url"])
def Test_Folder(url):
        
        Add_Dir( 
        name="10 Days of Genius", url=BASE+YOUTUBE_CHANNEL_ID_7+"/", folder=True,
        icon="http://tonyh.net/icons/nat%20geo/10_days.png", fanart=fanart2)

        Add_Dir( 
        name="360 Degrees", url=BASE+YOUTUBE_CHANNEL_ID_8+"/", folder=True,
        icon="http://tonyh.net/icons/nat%20geo/360%20degrees.png", fanart=fanart2)

        Add_Dir( 
        name="#Safari Live", url=BASE+YOUTUBE_CHANNEL_ID_9+"/", folder=True,
        icon="http://tonyh.net/icons/nat%20geo/safari%20live.png", fanart=fanart2)

#-----------------------------

@route(mode="bad_function")
def Bad_Function():
    if debug != 'true':
        dialog.ok('SET DEBUG TO TRUE','Go into your add-on settings and set debug mode to True then run this again. If debug is set to true we have proper error reporting in place to help your add-on development.')
        koding.Open_Settings(focus='1.1')
    xbmc.log(this_should_error)

#-----------------------------

#Play a youtube video
@route(mode="play_yt", args=["url"])
def Play_YT(url):
    
    xbmc.executebuiltin('PlayMedia(plugin://plugin.video.youtube/%s)'%url)

#-----------------------------------


if __name__ == "__main__":
    Run(default='main')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))