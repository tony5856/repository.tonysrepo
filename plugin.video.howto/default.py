# -*- coding: utf-8 -*-

 #License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
 #Addon: How to
 #Author: Tony H

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

#------------------------------------------------------------

YOUTUBE_CHANNEL_ID_5 = "PLv9sxo3G1kdQ-_HNcbwfcWCZAvDKpx3TQ"
YOUTUBE_CHANNEL_ID_3 = "PLyEyQCZKWQAPXvRjA7_lWXSQ_V7LJUSez"

#----------------------------------------------------------------

@route(mode='main_menu')
def Main_Menu():


    Add_Dir( 
        name="Metalliq how to", url=BASE+YOUTUBE_CHANNEL_ID_3+"/", folder=True,
        icon="http://www.desinerd.co.in/wp-content/uploads/2017/06/Metalliq.jpg")    
    Add_Dir( 
        name="test channel", url="http://iptv.genius-stream.com:6204/live/online/tv/1688.m3u8"+"/", folder=True,
        icon="http://www.desinerd.co.in/wp-content/uploads/2017/06/Metalliq.jpg")    

#----------------------------------------------------------------

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