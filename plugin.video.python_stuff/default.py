# -*- coding: utf-8 -*-
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: Python Stuff addon
# Author: TonyH

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

YOUTUBE_CHANNEL_ID_4 = "UCAu4RLzCTbhfEe3fh3KxnWQ"
YOUTUBE_CHANNEL_ID_5 = "PLv9sxo3G1kdQ-_HNcbwfcWCZAvDKpx3TQ"
YOUTUBE_CHANNEL_ID_6 = "PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_"
YOUTUBE_CHANNEL_ID_7 = "UCTj-2nCE8B_3AvEGAKVyn1g"
YOUTUBE_CHANNEL_ID_8 = "PL7hhhG5qUoXlpmIjqv2eEBukAeJSVNsdX"
YOUTUBE_CHANNEL_ID_9 = "PLSW3sa3BMObFm-KiN-ElXLObL96Jqve23"
YOUTUBE_CHANNEL_ID_10 = ""
YOUTUBE_CHANNEL_ID_11 = ""
YOUTUBE_CHANNEL_ID_12 = ""

#----------------------------------------------------------------

@route(mode='main')
def Main_Menu():

        
    Add_Dir( 
        name="Pipcan, kodi coding", url=BASE+YOUTUBE_CHANNEL_ID_5+"/", folder=True,
        icon="http://www.aftvnews.com/wp-content/uploads/2016/01/kodi_firetv_512x512.png")
       
    Add_Dir( 
        name="The new Boston, python how to", url=BASE+YOUTUBE_CHANNEL_ID_6+"/", folder=True,
        icon="http://orig09.deviantart.net/19a1/f/2012/341/2/7/python_os_x_icon_by_jivid321-d5nag4q.png")

    Add_Dir( 
        name="Total Revolution", url=BASE2+YOUTUBE_CHANNEL_ID_7+"/", folder=True,
        icon="http://orig09.deviantart.net/19a1/f/2012/341/2/7/python_os_x_icon_by_jivid321-d5nag4q.png")
    Add_Dir( 
        name="MBMantech, aftermath wizard tutrorials", url=BASE2+YOUTUBE_CHANNEL_ID_4+"/", folder=True,
        icon="http://orig09.deviantart.net/19a1/f/2012/341/2/7/python_os_x_icon_by_jivid321-d5nag4q.png")

    Add_Dir( 
        name="Napoleon Wilson", url=BASE+YOUTUBE_CHANNEL_ID_8+"/", folder=True,
        icon="http://orig09.deviantart.net/19a1/f/2012/341/2/7/python_os_x_icon_by_jivid321-d5nag4q.png")

    Add_Dir( 
        name="NAN Scrapers", url=BASE+YOUTUBE_CHANNEL_ID_9+"/", folder=True,
        icon="http://orig09.deviantart.net/19a1/f/2012/341/2/7/python_os_x_icon_by_jivid321-d5nag4q.png")    

#----------------------------------------------------------------
# Sample youtube single video
        #Add_Dir( 
        #name="World's Most Famous Botanical Gardens", url=BASE3+YOUTUBE_CHANNEL_ID_43, folder=False, mode='play_yt',
        #icon="https://i.pinimg.com/736x/7c/77/8e/7c778e14faa71ef6838cd81ec02196c5--succulent-terrarium-terrariums.jpg", fanart="https://wallpaperscraft.com/image/succulents_flowers_plant_110695_1920x1080.jpg")
#----------------------------------------------------------------

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