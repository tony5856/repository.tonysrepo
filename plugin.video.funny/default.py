# -*- coding: utf-8 -*-

""" ^ SECTION 1:
    This should be at the top of your code to declare the type of text
    format you're using. Without this you may find some text editors save
    it in an incompatible format and this can make bug tracking extremely
    confusing! More info here: https://www.python.org/dev/peps/pep-0263/
"""

#----------------------------------------------------------------

"""
    SECTION 2:
    This is where you'd put your license details, the GPL3 license 
    is the most common to use as it makes it easy for others to fork
    and improve upon your code. If you're re-using others code ALWAYS
    check the license first, removal of licenses is NOT allowed and you
    generally have to keep to the same license used in the original work
    (check license details as some do differ).

    Although not all licenses require it (some do, some don't),
    you should always give credit to the original author(s). Someone may have spent
    months if not years on the code so really it's the very least you can do if
    you choose to use their work as a base for your own.
"""
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: Funny Addon
# Author: TonyH

#----------------------------------------------------------------

"""
    SECTION 3:
    This is your global imports, any modules you need to import code from
    are added here. You'll see a handful of the more common imports below.
"""
import os           # access operating system commands
import urlparse     # splits up the directory path - much easier importing this than coding it up ourselves
import xbmc         # the base xbmc functions, pretty much every add-on is going to need at least one function from here
import xbmcaddon    # pull addon specific information such as settings, id, fanart etc.
import xbmcgui      # gui based functions, contains things like creating dialog pop-up windows
import xbmcplugin   # contains functions required for creating directory structure style add-ons (plugins)

# (*) = These modules require the noobsandnerds repo to be installed
import koding       # (*) a framework for easy add-on development, this template is to be used in conjunction with this module.
import nanscrapers  # (*) if you want to easily grab video links the hard work is done for you with this module.

from koding import Add_Dir  # By importing something like this we don't need to use <module>.<function> to call it,
                            # instead you can just use the function name - in this case Add_Dir().

from koding import route, Run # These are essential imports which allow us to open directories and navigate through the add-on.
from koding import route, Addon_Setting, Add_Dir, Find_In_Text, Open_URL, OK_Dialog
from koding import Open_Settings, Play_Video, Run, Text_File




#----------------------------------------------------------------

"""
    SECTION 4:
    These are our global variables, anything we set here can be accessed by any of
    our functions later on. Please bare in mind though that if you change the value
    of a global variable from inside a function the value will revert back to the
    value set here once that function has completed.
"""
addon_id     = xbmcaddon.Addon().getAddonInfo('id') # Grab our add-on id
dialog       = xbmcgui.Dialog()                     # A basic dialog message command
home_folder  = xbmc.translatePath('special://home/')# Convert the special path of Kodi home folder to the physical path
addon_folder = os.path.join(home_folder,'addons')   # Join our folder above with 'addons' so we have a link to our addons folder
art_path     = os.path.join(addon_folder,addon_id)  # Join addons folder with the addon_id, we'll use this as a basic art folder
debug        = koding.Addon_Setting('debug')        # Grab the setting of our debug mode in add-on settings

# Set the base plugin url you want to hook into
BASE  = "plugin://plugin.video.youtube/playlist/"
BASE2 = "plugin://plugin.video.youtube/channel/"
BASE3 = "play/?video_id="


# Set each of your YouTube playlist id's
YOUTUBE_CHANNEL_ID_1 = "UC67f2Qf7FYhtoUIF4Sf29cA"
YOUTUBE_CHANNEL_ID_2 = "UCZ30YNIcUWuSz8eVJZtLEjw"
YOUTUBE_CHANNEL_ID_3 = "90rMGa5WjCc"
YOUTUBE_CHANNEL_ID_4 = "y60wDzZt8yg"
YOUTUBE_CHANNEL_ID_5 = "K_6mqVcUwzg"
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
YOUTUBE_CHANNEL_ID_27 = "Iwvfig-fXk0"




#----------------------------------------------------------------
"""
    SECTION 5:
    Add our custom functions in here, it's VERY important these go in this section
    as the code in section 6 relies on these functions. If that code tries to run
    before these functions are declared the add-on will fail.

    You'll notice each function in here has a decorator above it (an @route() line of code),
    this assigns a mode to the function so it can be called with Add_Dir and it also tells
    the code what paramaters to send through. For example you'll notice the Main_Menu() function
    we've assigned to the mode "main" - this means if we ever want to get Add_Dir to open that
    function we just use the mode "main". This particular function does not require any extra
    params to be sent through but if you look at the Testing() function you'll see we send through
    2 different paramaters (url and description), if you look at the Add_Dir function in Main_Menu()
    you'll see we've sent these through as a dictionary. Using that same format you can send through
    as many different params as you wish.
"""

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
    Add_Dir(name='News Channels', url='', mode='open_folder8', folder=True, icon="http://tonyh.net/backgrounds/funny%20addon/icon.png", fanart="http://tonyh.net/backgrounds/funny%20addon/stand-up-comedy-video-wall.jpg")


#-----------------------------
@route(mode="test_function", args=["test1","test2","test3"])
def Test_Function(test1, test2, test3):
# Example of sending multiple variables through the Add_Dir function
    xbmc.log(test1,2)
    xbmc.log(test2,2)
    xbmc.log(test3,2)
    dialog.ok('CHECK THE LOG','Take a look at your log, you should be able to see the 3 lines of example text we sent through.')
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
#----------------------------
@route(mode="open_folder8", args=["url"])
def Test_Folder(url):

           
        Add_Dir( 
        name="CNN Live", url=BASE3+YOUTUBE_CHANNEL_ID_27, folder=False, mode='play_yt',
        icon="https://lh4.ggpht.com/m05SBF4omSJbBy-EnPClGH_yAVvgAn6wr6KQwdtXhn6ATylzMYYJb6WaW-pNbtmqg5I=w300", fanart="https://1x5xwy14hylj3ylgel358cb1-wpengine.netdna-ssl.com/wp-content/uploads/2015/09/THUMBNAIL_BG_01.jpg")

        Add_Dir( 
        name="Fox News Live", url=BASE3+YOUTUBE_CHANNEL_ID_3, folder=False, mode='play_yt',
        icon="https://lh3.googleusercontent.com/l8woCU1YmtyKlkNOh2TNvQJj8P78Rm56JljLDUj-83YzD3OU6UCvqM-vzqpBOkOrW2Q=w300", fanart="https://1x5xwy14hylj3ylgel358cb1-wpengine.netdna-ssl.com/wp-content/uploads/2015/09/THUMBNAIL_BG_01.jpg")

        Add_Dir( 
        name="Sky News Live", url=BASE3+YOUTUBE_CHANNEL_ID_4, folder=False, mode='play_yt',
        icon="http://hollirubin.com/wp-content/uploads/2017/05/sky-news-logo.png", fanart="https://1x5xwy14hylj3ylgel358cb1-wpengine.netdna-ssl.com/wp-content/uploads/2015/09/THUMBNAIL_BG_01.jpg")

        Add_Dir( 
        name="Euro News Live", url=BASE3+YOUTUBE_CHANNEL_ID_5, folder=False, mode='play_yt',
        icon="http://s.apptoko.com/a//uploads/thumbnails/122015/euronews-live_icon.png", fanart="https://1x5xwy14hylj3ylgel358cb1-wpengine.netdna-ssl.com/wp-content/uploads/2015/09/THUMBNAIL_BG_01.jpg")

#----------------------------







#-----------------------------
@route(mode="bad_function")
def Bad_Function():
    if debug != 'true':
        dialog.ok('SET DEBUG TO TRUE','Go into your add-on settings and set debug mode to True then run this again. If debug is set to true we have proper error reporting in place to help your add-on development.')
        koding.Open_Settings(focus='1.1')
    xbmc.log(this_should_error)

#-----------------------------



"""
    SECTION 6:
    Essential if creating list items, this tells kodi we're done creating our list items.
    The list will not populate without this. In the run command you need to set default to
    whatever route you want to open into, in this example the 'main' route which opens the
    Main_Menu() function up at the top.
"""
#-----------------------------------
#Play a youtube video
@route(mode="play_yt", args=["url"])
def Play_YT(url):
    
    xbmc.executebuiltin('PlayMedia(plugin://plugin.video.youtube/%s)'%url)

#-----------------------------------


if __name__ == "__main__":
    Run(default='main')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


  