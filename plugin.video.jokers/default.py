# -*- coding: utf-8 -*-
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: Impractical Jokers addon
# Author: Tony H

#----------------------------------------------------------------


import os          
import xbmc         
import xbmcaddon    
import xbmcplugin   
import re          
import xbmcgui      
from koding import route, Addon_Setting, Add_Dir, Find_In_Text, Open_URL, OK_Dialog
from koding import Open_Settings, Play_Video, Run, Text_File

#------------------------------------------------------------


debug        = Addon_Setting(setting='debug')      
addon_id     = xbmcaddon.Addon().getAddonInfo('id') 

#------------------------------------------------------------
BASE  = "plugin://plugin.video.youtube/playlist/"
BASE2 = "plugin://plugin.video.youtube/channel/"
background = "https://fanart.tv/fanart/tv/254243/showbackground/impractical-jokers-50ef906642ae1.jpg"


#-------------------------------------------------------------
YOUTUBE_CHANNEL_ID_1 = "PLZxWJ6CTr63bBO4j-q1eYT6pTPT-OLyUb"
YOUTUBE_CHANNEL_ID_2 = "PLZxWJ6CTr63ZYobFiIbWvRUEdzsrWVxEO"
YOUTUBE_CHANNEL_ID_3 = "PLZxWJ6CTr63ZDZ7OWCqPfUHrFoTfffETD"
YOUTUBE_CHANNEL_ID_4 = "PLZxWJ6CTr63YbqQAiQ4B5DQTk5sbo6n-O"
YOUTUBE_CHANNEL_ID_5 = "PL6KOBsJbDMbXM8CXyGvU9PEbBzv2YWYx_"
YOUTUBE_CHANNEL_ID_6 = "PLZxWJ6CTr63Z1imTZyROqVQnjFOPxso0D"
YOUTUBE_CHANNEL_ID_7 = "PLAoFLEmiupTdb3n0teoy7oYsq_9KoIjLm"

#----------------------------------------------------------------

@route(mode='main_menu')
def Main_Menu():


    Add_Dir( 
        name="[COLOR orange]Q's Funniest Moments[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_1+"/", folder=True,
        icon="http://articlebio.com/uploads/bio/2016/11/22/brian-quinn.jpg",
        fanart=background)

    Add_Dir( 
        name="[COLOR orange]Sal's Funniest Moments[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_2+"/", folder=True,
        icon="https://www.famousbirthdays.com/headshots/sal-vulcano-2.jpg",
        fanart=background)

    Add_Dir( 
        name="[COLOR orange]Joe's Funniest Moments[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_3+"/", folder=True,
        icon="https://www.famousbirthdays.com/faces/gatto-joe-image.jpg",
        fanart=background)

    Add_Dir( 
        name="[COLOR orange]Murr's Funniest Moments[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_4+"/", folder=True,
        icon="https://www.famousbirthdays.com/faces/murr-james-image.jpg",
        fanart=background)

    Add_Dir( 
        name="[COLOR yellow][I]-------Punishments-------[/I][/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_5+"/", folder=True,
        icon="https://orig01.deviantart.net/0701/f/2015/097/4/0/impractical_jokers_folder_icon_by_ex6-d8otewo.png",
        fanart=background)

    Add_Dir( 
        name="[COLOR yellow][I]-------Deleted Scenes-------[/I][/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_6+"/", folder=True,
        icon="http://cdn.movieweb.com/img.news.tops/NEdmR3IHPoeEgm_1_b/Exclusive-Impractical-Jokers-Season-1-Dvd-Clip-Food.jpg",
        fanart=background)

    Add_Dir( 
        name="[COLOR yellow][I]-------Behind the Scenes-------[/I][/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_7+"/", folder=True,
        icon="http://www.dailydoseofemuna.com/wp-content/uploads/2017/03/behind-the-scenes.gif",
        fanart=background)


#---------------------------------------------------------------
@route(mode='koding_settings')
def Koding_Settings():
    Open_Settings()
#----------------------------------------------------------------

@route(mode='simple_dialog', args=['title','msg'])
def Simple_Dialog(title,msg):
    OK_Dialog(title, msg)
#----------------------------------------------------------------


if __name__ == "__main__":
    Run(default='main_menu')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))