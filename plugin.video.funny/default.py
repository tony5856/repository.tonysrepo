# -*- coding: utf-8 -*-
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: Funny Addon
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

YOUTUBE_CHANNEL_ID_1 = "UC67f2Qf7FYhtoUIF4Sf29cA"
YOUTUBE_CHANNEL_ID_2 = "UCZ30YNIcUWuSz8eVJZtLEjw"
YOUTUBE_CHANNEL_ID_3 = ""
YOUTUBE_CHANNEL_ID_4 = ""
YOUTUBE_CHANNEL_ID_5 = ""
YOUTUBE_CHANNEL_ID_6 = ""
YOUTUBE_CHANNEL_ID_7 = "LL67f2Qf7FYhtoUIF4Sf29cA"
YOUTUBE_CHANNEL_ID_8 = "PLjncHZSg0GNGVX7LatYAz4EZXzGbkorTk"
YOUTUBE_CHANNEL_ID_9 = "PLKMjqoaBW16XWbIyJxb8DDDZnj6fP1MZV"
YOUTUBE_CHANNEL_ID_10 = "PLXd9aCB0yKuhzjovs87Kh9znvQBynJRJ9"
YOUTUBE_CHANNEL_ID_11 = "PLQn122p5FtqKWAKseY3k3zdU7Bo6hQjy1"
YOUTUBE_CHANNEL_ID_12 = "PLvBh3WamFgYL6dGMTL7ye7KRops1WEZnY"
YOUTUBE_CHANNEL_ID_13 = "PLyS6MFeQdZRJTHkURkqlOiHuXCviG8yTY"
YOUTUBE_CHANNEL_ID_14 = "PL9WV4cAlomwGWd6lN2fk6A0zzD0EO_hb1"
YOUTUBE_CHANNEL_ID_15 = "PLyXor-IbFvGTkxUPzJlIoLN1Mo7ChGyq3"
YOUTUBE_CHANNEL_ID_16 = "UCraZuY2kjbsiRNBIHuUQQRg"
YOUTUBE_CHANNEL_ID_17 = "UCi8e0iOVk1fEOogdfu4YgfA"
YOUTUBE_CHANNEL_ID_18 = "UCuaFvcY4MhZY3U43mMt1dYQ"
YOUTUBE_CHANNEL_ID_19 = "UCkR0GY0ue02aMyM-oxwgg9g"
YOUTUBE_CHANNEL_ID_20 = "UCPDis9pjXuqyI7RYLJ-TTSA"
YOUTUBE_CHANNEL_ID_21 = "UCsVXjNRWJMyXViNLM2pyMfg"
YOUTUBE_CHANNEL_ID_22 = "UCONQ53-nTMwqiRhj3sRaiAQ"
YOUTUBE_CHANNEL_ID_23 = "PLcLKHnbDqCOafKc2h6ryuXP8__fGZx7wW"
YOUTUBE_CHANNEL_ID_24 = "UCeZe0VwwhEf8KTI2FHfJtTg"
YOUTUBE_CHANNEL_ID_25 = "UCYK1TyKyMxyDQU8c6zF8ltg"
YOUTUBE_CHANNEL_ID_26 = "ZBvG9hd5kQA"
YOUTUBE_CHANNEL_ID_27 = ""


#-----------------------------------------------------------
@route(mode="main")
def Main_Menu():


    Add_Dir(name='Bad Lip Reading', url='', mode='open_folder', folder=True, icon="http://cdn.marketplaceimages.windowsphone.com/v8/images/b1d4b19a-8711-41d0-8885-01bc32b4c701?imageType=ws_icon_medium", fanart="http://tonyh.net/backgrounds/funny%20addon/stand-up-comedy-video-wall.jpg")
    Add_Dir(name='Commercials', url='', mode='open_folder2', folder=True, icon="http://www.arffinancial.com/wp-content/uploads/2014/04/tv.png", fanart="http://tonyh.net/backgrounds/funny%20addon/stand-up-comedy-video-wall.jpg")
    Add_Dir(name='Real Life Lore', url='', mode='open_folder3', folder=True, icon="https://pbs.twimg.com/profile_images/884565411156475904/Ih43VQxG.jpg", fanart="http://tonyh.net/backgrounds/funny%20addon/stand-up-comedy-video-wall.jpg")
    Add_Dir(name='Trailers', url='', mode='open_folder4', folder=True, icon="https://lh4.ggpht.com/YU-xk1IG8ZfG_4GSX2LUrfC7keaLC1ilxcV5maHxWBPSSYmhda7BJAAehaiTyHDvWbH-=w300", fanart="http://tonyh.net/backgrounds/funny%20addon/stand-up-comedy-video-wall.jpg")
    Add_Dir(name='Fail Videos', url='', mode='open_folder5', folder=True, icon="http://matthewhopkinsnews.com/wp-content/uploads/2014/06/FailStamp.jpg", fanart="http://tonyh.net/backgrounds/funny%20addon/stand-up-comedy-video-wall.jpg")
    Add_Dir(name='My Collection', url='', mode='open_folder6', folder=True, icon="http://cdn.mysitemyway.com/etc-mysitemyway/icons/legacy-previews/icons/matte-blue-and-white-square-icons-sports-hobbies/118110-matte-blue-and-white-square-icon-sports-hobbies-film-clapper1-sc44.png", fanart="http://tonyh.net/backgrounds/funny%20addon/stand-up-comedy-video-wall.jpg")
    Add_Dir(name='Funny Pet Videos', url='', mode='open_folder7', folder=True, icon="https://i.pinimg.com/236x/fa/3a/0f/fa3a0f6344d2ca877482e358dee55516--video-chat-photo-cat.jpg", fanart="http://tonyh.net/backgrounds/funny%20addon/stand-up-comedy-video-wall.jpg")


#-----------------------------
@route(mode="open_folder", args=["url"])
def Test_Folder(url):

        Add_Dir( 
        name="Bad Lip Reading Channel", url=BASE2+YOUTUBE_CHANNEL_ID_1+"/", folder=True,
        icon="http://cdn.marketplaceimages.windowsphone.com/v8/images/b1d4b19a-8711-41d0-8885-01bc32b4c701?imageType=ws_icon_medium", fanart="http://tonyh.net/backgrounds/hema%20images/bad_lip_reading.jpg")

        Add_Dir( 
        name="Jaboody Dubs Channel", url=BASE2+YOUTUBE_CHANNEL_ID_2+"/", folder=True,
        icon="https://pbs.twimg.com/profile_images/3567275418/997d6030558d12e18c9f5cd64fefe8bf_400x400.jpeg", fanart="http://cdn.akamai.steamstatic.com/steamcommunity/public/images/items/504490/2b9e8527b861652126a4b7261f43fd197bff8974.jpg")




#-----------------------------
@route(mode="open_folder2", args=["url"])
def Test_Folder(url):

        
        Add_Dir( 
        name="2015 Super Bowl Commercials", url=BASE+YOUTUBE_CHANNEL_ID_9+"/", folder=True,
        icon="http://www.bestappspoint.com/wp-content/uploads/2012/02/Super-Ads-Super-Bowl-Commercials.jpg", fanart="https://www.ventureiconmedia.com/wp-content/uploads/2017/02/2.png")

        Add_Dir( 
        name="2016 Super Bowl Commercials", url=BASE+YOUTUBE_CHANNEL_ID_8+"/", folder=True,
        icon="http://www.bestappspoint.com/wp-content/uploads/2012/02/Super-Ads-Super-Bowl-Commercials.jpg", fanart="https://www.ventureiconmedia.com/wp-content/uploads/2017/02/2.png")

        Add_Dir( 
        name="2017 Super Bowl Commercials", url=BASE+YOUTUBE_CHANNEL_ID_10+"/", folder=True,
        icon="http://www.bestappspoint.com/wp-content/uploads/2012/02/Super-Ads-Super-Bowl-Commercials.jpg", fanart="https://www.ventureiconmedia.com/wp-content/uploads/2017/02/2.png")

        Add_Dir( 
        name="50 Best Super Bowl Commercials of all time", url=BASE+YOUTUBE_CHANNEL_ID_11+"/", folder=True,
        icon="http://www.bestappspoint.com/wp-content/uploads/2012/02/Super-Ads-Super-Bowl-Commercials.jpg", fanart="https://www.ventureiconmedia.com/wp-content/uploads/2017/02/2.png")

        Add_Dir( 
        name="Funny Commercials 1", url=BASE+YOUTUBE_CHANNEL_ID_12+"/", folder=True,
        icon="http://static.superbowlcommercials.co/2016/01/Emotional-chart-720x415.gif", fanart="https://www.ventureiconmedia.com/wp-content/uploads/2017/02/2.png")

        Add_Dir( 
        name="Funny Commercials 2", url=BASE+YOUTUBE_CHANNEL_ID_13+"/", folder=True,
        icon="http://static.superbowlcommercials.co/2016/01/Emotional-chart-720x415.gif", fanart="https://www.ventureiconmedia.com/wp-content/uploads/2017/02/2.png")

        Add_Dir( 
        name="Funny Commercials 3", url=BASE+YOUTUBE_CHANNEL_ID_14+"/", folder=True,
        icon="http://static.superbowlcommercials.co/2016/01/Emotional-chart-720x415.gif", fanart="https://www.ventureiconmedia.com/wp-content/uploads/2017/02/2.png")

#-----------------------------
@route(mode="open_folder3", args=["url"])
def Test_Folder(url):

        
        Add_Dir( 
        name="Real Life Lore", url=BASE+YOUTUBE_CHANNEL_ID_15+"/", folder=True,
        icon="https://pbs.twimg.com/profile_images/884565411156475904/Ih43VQxG.jpg", fanart="https://i.ytimg.com/vi/E39GIysMevQ/maxresdefault.jpg")
#-----------------------------
@route(mode="open_folder4", args=["url"])
def Test_Folder(url):

        Add_Dir( 
        name="Movie Trailers 199", url=BASE2+YOUTUBE_CHANNEL_ID_16+"/", folder=True,
        icon="https://lh4.ggpht.com/YU-xk1IG8ZfG_4GSX2LUrfC7keaLC1ilxcV5maHxWBPSSYmhda7BJAAehaiTyHDvWbH-=w300", fanart="http://az616578.vo.msecnd.net/files/2016/10/30/636134414566099044185438682_635950754841194176761107736_Movie_Trailer_Preview_Screen.jpg")

        Add_Dir( 
        name="Movieclips Trailers", url=BASE2+YOUTUBE_CHANNEL_ID_17+"/", folder=True,
        icon="https://lh4.ggpht.com/YU-xk1IG8ZfG_4GSX2LUrfC7keaLC1ilxcV5maHxWBPSSYmhda7BJAAehaiTyHDvWbH-=w300", fanart="http://az616578.vo.msecnd.net/files/2016/10/30/636134414566099044185438682_635950754841194176761107736_Movie_Trailer_Preview_Screen.jpg")

        Add_Dir( 
        name="Disney Movie Trailers", url=BASE2+YOUTUBE_CHANNEL_ID_18+"/", folder=True,
        icon="https://lh4.ggpht.com/YU-xk1IG8ZfG_4GSX2LUrfC7keaLC1ilxcV5maHxWBPSSYmhda7BJAAehaiTyHDvWbH-=w300", fanart="http://az616578.vo.msecnd.net/files/2016/10/30/636134414566099044185438682_635950754841194176761107736_Movie_Trailer_Preview_Screen.jpg")

        Add_Dir( 
        name="Movieclips Coming soon", url=BASE2+YOUTUBE_CHANNEL_ID_19+"/", folder=True,
        icon="https://lh4.ggpht.com/YU-xk1IG8ZfG_4GSX2LUrfC7keaLC1ilxcV5maHxWBPSSYmhda7BJAAehaiTyHDvWbH-=w300", fanart="http://az616578.vo.msecnd.net/files/2016/10/30/636134414566099044185438682_635950754841194176761107736_Movie_Trailer_Preview_Screen.jpg")

#-----------------------------
@route(mode="open_folder5", args=["url"])
def Test_Folder(url):


        Add_Dir( 
        name="Fail Army", url=BASE2+YOUTUBE_CHANNEL_ID_20+"/", folder=True,
        icon="http://matthewhopkinsnews.com/wp-content/uploads/2014/06/FailStamp.jpg", fanart="http://ak6.picdn.net/shutterstock/videos/9455603/thumb/5.jpg")

        Add_Dir( 
        name="Jukin Videos", url=BASE2+YOUTUBE_CHANNEL_ID_21+"/", folder=True,
        icon="http://matthewhopkinsnews.com/wp-content/uploads/2014/06/FailStamp.jpg", fanart="http://ak6.picdn.net/shutterstock/videos/9455603/thumb/5.jpg")

        Add_Dir( 
        name="Fail Blog", url=BASE2+YOUTUBE_CHANNEL_ID_22+"/", folder=True,
        icon="http://matthewhopkinsnews.com/wp-content/uploads/2014/06/FailStamp.jpg", fanart="http://ak6.picdn.net/shutterstock/videos/9455603/thumb/5.jpg")

#----------------------------
@route(mode="open_folder6", args=["url"])
def Test_Folder(url):


        Add_Dir( 
        name="Family Guy Star Wars", url=BASE+YOUTUBE_CHANNEL_ID_23+"/", folder=True,
        icon="http://cdn.mysitemyway.com/etc-mysitemyway/icons/legacy-previews/icons/matte-blue-and-white-square-icons-sports-hobbies/118110-matte-blue-and-white-square-icon-sports-hobbies-film-clapper1-sc44.png", fanart="https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/vfPFP3W/movie-theater-film-reel-background-in-seamless-loop_xk6ivnb9__F0000.png")

        Add_Dir( 
        name="Hulk Purple Pants", url=BASE3+YOUTUBE_CHANNEL_ID_26, folder=False, mode='play_yt',
        icon="http://cdn.mysitemyway.com/etc-mysitemyway/icons/legacy-previews/icons/matte-blue-and-white-square-icons-sports-hobbies/118110-matte-blue-and-white-square-icon-sports-hobbies-film-clapper1-sc44.png", fanart="https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/vfPFP3W/movie-theater-film-reel-background-in-seamless-loop_xk6ivnb9__F0000.png")




#-----------------------------
@route(mode="open_folder7", args=["url"])
def Test_Folder(url):

           
        Add_Dir( 
        name="Funny Pets", url=BASE2+YOUTUBE_CHANNEL_ID_24+"/", folder=True,
        icon="https://68.media.tumblr.com/eda338f26d06d5f4138094f3176929b8/tumblr_ou8hsigeJ21vs9ch6o1_400.png", fanart="http://funnypicture.org/wallpaper/2015/04/funny-animals-clips-3-background-wallpaper.jpg")

        Add_Dir( 
        name="Funny Pet Videos", url=BASE2+YOUTUBE_CHANNEL_ID_25+"/", folder=True,
        icon="https://68.media.tumblr.com/eda338f26d06d5f4138094f3176929b8/tumblr_ou8hsigeJ21vs9ch6o1_400.png", fanart="http://funnypicture.org/wallpaper/2015/04/funny-animals-clips-3-background-wallpaper.jpg")


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


  