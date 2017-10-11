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
YOUTUBE_CHANNEL_ID_10 = "-FHbf8-lywc"
YOUTUBE_CHANNEL_ID_11 = "ncw4ISEU5ik"
YOUTUBE_CHANNEL_ID_12 = "XLBwToelXSM"
YOUTUBE_CHANNEL_ID_13 = "JZf9TUDYmME"
YOUTUBE_CHANNEL_ID_14 = "6ZPGT0rN9bI"
YOUTUBE_CHANNEL_ID_15 = "gG6-9wDnNKE"
YOUTUBE_CHANNEL_ID_16 = "tmWV5ZnKOAg"
YOUTUBE_CHANNEL_ID_17 = "ULMw5ritC3M"
YOUTUBE_CHANNEL_ID_18 = "vPFK54f6_CU"
YOUTUBE_CHANNEL_ID_19 = "0iVpUpn6I6U"
YOUTUBE_CHANNEL_ID_20 = "ps9jq6XS5Sc"
YOUTUBE_CHANNEL_ID_21 = "g_1oiJqE3OI"
YOUTUBE_CHANNEL_ID_22 = "XVG8exRLJJk"
YOUTUBE_CHANNEL_ID_23 = "NQQi_OH7m08"
YOUTUBE_CHANNEL_ID_24 = "WcPljgtrlNE"
YOUTUBE_CHANNEL_ID_25 = "Z-URygHoE_o"
YOUTUBE_CHANNEL_ID_26 = "oEorCX1I8CM"
YOUTUBE_CHANNEL_ID_27 = "SRrG9WC0Ebo"
YOUTUBE_CHANNEL_ID_28 = ""
YOUTUBE_CHANNEL_ID_29 = ""
YOUTUBE_CHANNEL_ID_30 = ""
YOUTUBE_CHANNEL_ID_31 = ""
YOUTUBE_CHANNEL_ID_32 = ""


#-----------------------------------------------------------

@route(mode="main")
def Main_Menu():


    Add_Dir(name='Short Clip Playlists updated Daily', url='', mode='open_folder', folder=True, icon="http://tonyh.net/icons/nat%20geo/short%20clips.png", fanart="https://i.ytimg.com/vi/Fs3IQXKGC5o/maxresdefault.jpg")
    Add_Dir(name='Special Playlists', url='', mode='open_folder2', folder=True, icon="http://tonyh.net/icons/nat%20geo/live.png", fanart="https://i.ytimg.com/vi/Fs3IQXKGC5o/maxresdefault.jpg")
    Add_Dir(name='Space Documentaries', url='', mode='open_folder3', folder=True, icon="http://tonyh.net/icons/nat%20geo/space.png", fanart="https://i.ytimg.com/vi/Fs3IQXKGC5o/maxresdefault.jpg")
    Add_Dir(name='Science and Tech Documentaries', url='', mode='open_folder4', folder=True, icon="http://tonyh.net/icons/nat%20geo/science%20and%20tech.png", fanart="https://i.ytimg.com/vi/Fs3IQXKGC5o/maxresdefault.jpg")
    Add_Dir(name='Nature and Enviroment Documentaries', url='', mode='open_folder5', folder=True, icon="http://tonyh.net/icons/nat%20geo/nature.png", fanart="https://i.ytimg.com/vi/Fs3IQXKGC5o/maxresdefault.jpg")



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

@route(mode="open_folder3", args=["url"])
def Test_Folder(url):
        
        Add_Dir( 
        name="Gravity", url=BASE3+YOUTUBE_CHANNEL_ID_10, folder=False, mode='play_yt',
        icon="http://www.fondos7.net/thumbs/1189_2.jpg", fanart="https://i.pinimg.com/originals/5c/e1/44/5ce144f88cc4c2327279b97f14a5b486.jpg")

        Add_Dir( 
        name="How the Universe Works", url=BASE3+YOUTUBE_CHANNEL_ID_15, folder=False, mode='play_yt',
        icon="http://www.fondos7.net/thumbs/1189_2.jpg", fanart="https://i.pinimg.com/originals/5c/e1/44/5ce144f88cc4c2327279b97f14a5b486.jpg")

        Add_Dir( 
        name="Journey to the edge of the Universe", url=BASE3+YOUTUBE_CHANNEL_ID_16, folder=False, mode='play_yt',
        icon="http://www.fondos7.net/thumbs/1189_2.jpg", fanart="https://i.pinimg.com/originals/5c/e1/44/5ce144f88cc4c2327279b97f14a5b486.jpg")

        Add_Dir( 
        name="Found the second Earth", url=BASE3+YOUTUBE_CHANNEL_ID_17, folder=False, mode='play_yt',
        icon="http://www.fondos7.net/thumbs/1189_2.jpg", fanart="https://i.pinimg.com/originals/5c/e1/44/5ce144f88cc4c2327279b97f14a5b486.jpg")

        Add_Dir( 
        name="Astrobiology & Space Travel", url=BASE3+YOUTUBE_CHANNEL_ID_24, folder=False, mode='play_yt',
        icon="http://www.fondos7.net/thumbs/1189_2.jpg", fanart="https://i.pinimg.com/originals/5c/e1/44/5ce144f88cc4c2327279b97f14a5b486.jpg")

#-----------------------------        

@route(mode="open_folder4", args=["url"])
def Test_Folder(url):
        
        Add_Dir( 
        name="Tesla Motors", url=BASE3+YOUTUBE_CHANNEL_ID_11, folder=False, mode='play_yt',
        icon="http://www.zincnyx.com/wp-content/uploads/2015/05/ThinkstockPhotos-482461333-Globe-Hand.jpg", fanart="https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/YqGSkmb/videoblocks-seamless-loop-of-a-3d-human-brain-being-formed-by-points-brain-neuron-and-dna-chain-being-scanned-by-hud-interface-medical-futuristic-science-and-technology-motion-background-3d-rendering_seqh3a60e_thumbnail-full01.png")

        Add_Dir( 
        name="The World in 2050", url=BASE3+YOUTUBE_CHANNEL_ID_21, folder=False, mode='play_yt',
        icon="http://www.zincnyx.com/wp-content/uploads/2015/05/ThinkstockPhotos-482461333-Globe-Hand.jpg", fanart="https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/YqGSkmb/videoblocks-seamless-loop-of-a-3d-human-brain-being-formed-by-points-brain-neuron-and-dna-chain-being-scanned-by-hud-interface-medical-futuristic-science-and-technology-motion-background-3d-rendering_seqh3a60e_thumbnail-full01.png")

        Add_Dir( 
        name="Fabric of the Cosmos - What is Space", url=BASE3+YOUTUBE_CHANNEL_ID_22, folder=False, mode='play_yt',
        icon="http://www.zincnyx.com/wp-content/uploads/2015/05/ThinkstockPhotos-482461333-Globe-Hand.jpg", fanart="https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/YqGSkmb/videoblocks-seamless-loop-of-a-3d-human-brain-being-formed-by-points-brain-neuron-and-dna-chain-being-scanned-by-hud-interface-medical-futuristic-science-and-technology-motion-background-3d-rendering_seqh3a60e_thumbnail-full01.png")

        Add_Dir( 
        name="Fabric of the Cosmos - The Illusion of Time", url=BASE3+YOUTUBE_CHANNEL_ID_25, folder=False, mode='play_yt',
        icon="http://www.zincnyx.com/wp-content/uploads/2015/05/ThinkstockPhotos-482461333-Globe-Hand.jpg", fanart="https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/YqGSkmb/videoblocks-seamless-loop-of-a-3d-human-brain-being-formed-by-points-brain-neuron-and-dna-chain-being-scanned-by-hud-interface-medical-futuristic-science-and-technology-motion-background-3d-rendering_seqh3a60e_thumbnail-full01.png")

        Add_Dir( 
        name="Fabric of the Cosmos - Quantum Leap", url=BASE3+YOUTUBE_CHANNEL_ID_26, folder=False, mode='play_yt',
        icon="http://www.zincnyx.com/wp-content/uploads/2015/05/ThinkstockPhotos-482461333-Globe-Hand.jpg", fanart="https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/YqGSkmb/videoblocks-seamless-loop-of-a-3d-human-brain-being-formed-by-points-brain-neuron-and-dna-chain-being-scanned-by-hud-interface-medical-futuristic-science-and-technology-motion-background-3d-rendering_seqh3a60e_thumbnail-full01.png")

        Add_Dir( 
        name="Fabric of the Cosmos - Universe or Multiverse", url=BASE3+YOUTUBE_CHANNEL_ID_27, folder=False, mode='play_yt',
        icon="http://www.zincnyx.com/wp-content/uploads/2015/05/ThinkstockPhotos-482461333-Globe-Hand.jpg", fanart="https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/YqGSkmb/videoblocks-seamless-loop-of-a-3d-human-brain-being-formed-by-points-brain-neuron-and-dna-chain-being-scanned-by-hud-interface-medical-futuristic-science-and-technology-motion-background-3d-rendering_seqh3a60e_thumbnail-full01.png")

#------------------------------

@route(mode="open_folder5", args=["url"])
def Test_Folder(url):
        
        Add_Dir( 
        name="Wild Amazon - The Perfect Paradise", url=BASE3+YOUTUBE_CHANNEL_ID_12, folder=False, mode='play_yt',
        icon="https://cdn3.iconfinder.com/data/icons/3d-printing-icon-set/512/Recycling.png", fanart="https://userscontent2.emaze.com/images/2219d736-6961-455b-bf1d-a32ab63950b0/977fabcded9eb4946dbf747ab8cd4dd4.jpg")

        Add_Dir( 
        name="Rare and Exotic Animalsy", url=BASE3+YOUTUBE_CHANNEL_ID_13, folder=False, mode='play_yt',
        icon="https://cdn3.iconfinder.com/data/icons/3d-printing-icon-set/512/Recycling.png", fanart="https://userscontent2.emaze.com/images/2219d736-6961-455b-bf1d-a32ab63950b0/977fabcded9eb4946dbf747ab8cd4dd4.jpg")

        Add_Dir( 
        name="Ocean of Giants", url=BASE3+YOUTUBE_CHANNEL_ID_14, folder=False, mode='play_yt',
        icon="https://cdn3.iconfinder.com/data/icons/3d-printing-icon-set/512/Recycling.png", fanart="https://userscontent2.emaze.com/images/2219d736-6961-455b-bf1d-a32ab63950b0/977fabcded9eb4946dbf747ab8cd4dd4.jpg")

        Add_Dir( 
        name="War of Insects", url=BASE3+YOUTUBE_CHANNEL_ID_18, folder=False, mode='play_yt',
        icon="https://cdn3.iconfinder.com/data/icons/3d-printing-icon-set/512/Recycling.png", fanart="https://userscontent2.emaze.com/images/2219d736-6961-455b-bf1d-a32ab63950b0/977fabcded9eb4946dbf747ab8cd4dd4.jpg")

        Add_Dir( 
        name="The Secret language of Plants", url=BASE3+YOUTUBE_CHANNEL_ID_19, folder=False, mode='play_yt',
        icon="https://cdn3.iconfinder.com/data/icons/3d-printing-icon-set/512/Recycling.png", fanart="https://userscontent2.emaze.com/images/2219d736-6961-455b-bf1d-a32ab63950b0/977fabcded9eb4946dbf747ab8cd4dd4.jpg")

        Add_Dir( 
        name="Top Ten Natural Disasters", url=BASE3+YOUTUBE_CHANNEL_ID_20, folder=False, mode='play_yt',
        icon="https://cdn3.iconfinder.com/data/icons/3d-printing-icon-set/512/Recycling.png", fanart="https://userscontent2.emaze.com/images/2219d736-6961-455b-bf1d-a32ab63950b0/977fabcded9eb4946dbf747ab8cd4dd4.jpg")

        Add_Dir( 
        name="Deadliest Diseases In Human History", url=BASE3+YOUTUBE_CHANNEL_ID_23, folder=False, mode='play_yt',
        icon="https://cdn3.iconfinder.com/data/icons/3d-printing-icon-set/512/Recycling.png", fanart="https://userscontent2.emaze.com/images/2219d736-6961-455b-bf1d-a32ab63950b0/977fabcded9eb4946dbf747ab8cd4dd4.jpg")

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