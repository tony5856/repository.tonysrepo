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
# Addon: My Python Koding Add-on
# Author: Add your name here

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
#------------------------------------------------
# Set the base plugin url you want to hook into
BASE  = "plugin://plugin.video.youtube/playlist/"
BASE2 = "plugin://plugin.video.youtube/channel/"
BASE3 = "play/?video_id="


#------------------------------------------------

# Set each of your YouTube playlist id's
YOUTUBE_CHANNEL_ID_1 = "UCuuTGIE9NAeYuwDbpmSm4eg"
YOUTUBE_CHANNEL_ID_2 = "PLWXrpnvUkPwmmpyisk1y603H9W_HCo3i2"
YOUTUBE_CHANNEL_ID_3 = "PLEsPf9ZJCbKFtgEKYqBjYxbgq6SCOmZqi"
YOUTUBE_CHANNEL_ID_4 = "PL_KA9gR6zLeFFjbODQ6zngUaGIE49jAH9"
YOUTUBE_CHANNEL_ID_5 = "PLVdcJOUQZucfSYnHAjwB2HNgEOzKxIwHz"
YOUTUBE_CHANNEL_ID_6 = "PLkmgZrfE21jwV9e7q-bkGDp_mzjiW1A6_"
YOUTUBE_CHANNEL_ID_7 = "PLUl4u3cNGP61-9PEhRognw5vryrSEVLPr"
YOUTUBE_CHANNEL_ID_8 = "PLE73E48C4D227E053"
YOUTUBE_CHANNEL_ID_9 = "PLkyBCj4JhHt_pz8HUG7rbMeKFsStae10k"
YOUTUBE_CHANNEL_ID_10 = "PLKQ6Y3lMA4BbaYDvdEU1Pz_wmeYpUfqeD"
YOUTUBE_CHANNEL_ID_11 = "PLc3yDgjpoPtFwk2YJQWAQy_3ZWrm8EBp7"
YOUTUBE_CHANNEL_ID_12 = "PLowYwBwSCQXWnznaU5d0KXA2rz4vkHgsY"
YOUTUBE_CHANNEL_ID_13 = "PL_srx7JT55wiMyflDoQip3HsHaDXZmVQS"
YOUTUBE_CHANNEL_ID_14 = "UCMFsHceLUJNkXMiCMFNnvkA"
YOUTUBE_CHANNEL_ID_15 = "UCP5tjEmvPItGyLhmjdwP7Ww"
YOUTUBE_CHANNEL_ID_16 = "UCuSlFJbBUIj1zfJLRnGXSow"
YOUTUBE_CHANNEL_ID_17 = "UCp68_FLety0O-n9QU6phsgw"
YOUTUBE_CHANNEL_ID_18 = "UCkCuSXCy9PzV2XDl5dE1iPg"
YOUTUBE_CHANNEL_ID_19 = "UC6H07z6zAwbHRl4Lbl0GSsw"
YOUTUBE_CHANNEL_ID_20 = "UCkEKLTfO0PP_Y9tYBTAoRuQ"
YOUTUBE_CHANNEL_ID_21 = "UCtcsKTmGKo1UCT24OaGxEtw"
YOUTUBE_CHANNEL_ID_22 = "UCWrXlzhIENTJrAuKVuPgdEA"
YOUTUBE_CHANNEL_ID_23 = "UCrX_2JCBvW6k2KKjSV7dIdQ"
YOUTUBE_CHANNEL_ID_24 = "UC1mIxTEk1Q9IMIPwV67JSdQ"
YOUTUBE_CHANNEL_ID_25 = "UC_OVsoKcD3jxHgxjQirLq-A"
YOUTUBE_CHANNEL_ID_26 = "UC4QZ_LsYcvcq7qOsOhpAX4A"
YOUTUBE_CHANNEL_ID_27 = "DtRrvraDkLI"
YOUTUBE_CHANNEL_ID_28 = "-FHbf8-lywc"
YOUTUBE_CHANNEL_ID_29 = "5OeerYNLV5A"
YOUTUBE_CHANNEL_ID_30 = "ZidPzP0wchg"
YOUTUBE_CHANNEL_ID_31 = "0iVpUpn6I6U"
YOUTUBE_CHANNEL_ID_32 = "8QSWP56J8DA"
YOUTUBE_CHANNEL_ID_33 = "aEbxdE-QDhY"
YOUTUBE_CHANNEL_ID_34 = "v983wZ-yNyo"
YOUTUBE_CHANNEL_ID_35 = "x2pvvvook34"
YOUTUBE_CHANNEL_ID_36 = "T27q1Z6D4ko"
YOUTUBE_CHANNEL_ID_37 = "i5U1io0PB88"
YOUTUBE_CHANNEL_ID_38 = "jEORjBWY-t4"
YOUTUBE_CHANNEL_ID_39 = "WWllXaMod1c"
YOUTUBE_CHANNEL_ID_40 = "MlbKlRGlyCQ"
YOUTUBE_CHANNEL_ID_41 = "2RAJFS5namo"
YOUTUBE_CHANNEL_ID_42 = "PLyNTTx_4gF9smBxRsJA-YDjHDIfPo0RCQ"
YOUTUBE_CHANNEL_ID_43 = "x-sf19f_QRE"
YOUTUBE_CHANNEL_ID_44 = ""
YOUTUBE_CHANNEL_ID_45 = ""
YOUTUBE_CHANNEL_ID_46 = ""
YOUTUBE_CHANNEL_ID_47 = ""
YOUTUBE_CHANNEL_ID_48 = ""
YOUTUBE_CHANNEL_ID_49 = ""

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
# EDIT THIS MAIN_MENU() FUNCTION - THIS IS FUN TO PLAY WITH!
#-----------------------------------------------------------
@route(mode="main")
def Main_Menu():


    Add_Dir(name='Space Travel', url='', mode='open_folder', folder=True, icon="http://icons.iconarchive.com/icons/aha-soft/space/256/Galaxy-icon.png", fanart="http://tonyh.net/backgrounds/tech/tech2.jpg.png")
    Add_Dir(name='Quantum Physics', url='', mode='open_folder2', folder=True, icon="https://cf3e497594.site.internapcdn.net/tmpl/v5/img/phys_308px.png", fanart="http://tonyh.net/backgrounds/tech/tech2.jpg.png")
    Add_Dir(name='Real Life Lore', url='', mode='open_folder3', folder=True, icon="https://pbs.twimg.com/profile_images/884565411156475904/Ih43VQxG.jpg", fanart="http://tonyh.net/backgrounds/tech/tech2.jpg.png")
    Add_Dir(name='Theory of Relativity', url='', mode='open_folder4', folder=True, icon="https://cdn4.iconfinder.com/data/icons/education-volume-7/48/329-512.png", fanart="http://tonyh.net/backgrounds/tech/tech2.jpg.png")
    Add_Dir(name='Hubble Space Telescope', url='', mode='open_folder5', folder=True, icon="https://universegrowth.files.wordpress.com/2010/12/hubble.png", fanart="http://tonyh.net/backgrounds/tech/tech2.jpg.png")
    Add_Dir(name='Fusion Power', url='', mode='open_folder6', folder=True, icon="https://cdn4.iconfinder.com/data/icons/iron-man-icons/512/Reactor.png", fanart="http://tonyh.net/backgrounds/tech/tech2.jpg.png")
    Add_Dir(name='Inventions', url='', mode='open_folder7', folder=True, icon="https://inventionaday.com/wp-content/uploads/2016/09/Invention_a_day_logo.png", fanart="http://tonyh.net/backgrounds/tech/tech2.jpg.png")
    Add_Dir(name='Space in General', url='', mode='open_folder8', folder=True, icon="http://www.santeriaytarot.com/images/jupiter.png", fanart="http://tonyh.net/backgrounds/tech/tech2.jpg.png")
    Add_Dir(name='Documentary Channels/Playlists', url='', mode='open_folder9', folder=True, icon="http://www.thehtpc.net/wp-content/gallery/imagesbyname/xz_genre_preview.png", fanart="http://tonyh.net/backgrounds/tech/tech2.jpg.png")
    Add_Dir(name='Single Documentaries', url='', mode='open_folder10', folder=True, icon="http://www.thehtpc.net/wp-content/gallery/imagesbyname/xz_genre_preview.png", fanart="http://tonyh.net/backgrounds/tech/tech2.jpg.png")
    Add_Dir(name='Plants', url='', mode='open_folder11', folder=True, icon="https://i.pinimg.com/736x/7c/77/8e/7c778e14faa71ef6838cd81ec02196c5--succulent-terrarium-terrariums.jpg", fanart="http://tonyh.net/backgrounds/tech/tech2.jpg.png")



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
        name="Warp Drive", url=BASE2+YOUTUBE_CHANNEL_ID_1+"/", folder=True,
        icon="http://www.dailygalaxy.com/photos/uncategorized/2008/07/29/warp_drive_2.jpg", fanart="http://tonyh.net/backgrounds/tech/wallpapers%20authors%20ps3%20space%20themes%20desktop%20backgrounds%20....jpg")
       
        Add_Dir( 
        name="Warp Drive 2", url=BASE+YOUTUBE_CHANNEL_ID_2+"/", folder=True,
        icon="http://www.dailygalaxy.com/photos/uncategorized/2008/07/29/warp_drive_2.jpg", fanart="http://tonyh.net/backgrounds/tech/wallpapers%20authors%20ps3%20space%20themes%20desktop%20backgrounds%20....jpg")
       
        Add_Dir( 
        name="Warp Drive 3", url=BASE+YOUTUBE_CHANNEL_ID_3+"/", folder=True,
        icon="http://www.dailygalaxy.com/photos/uncategorized/2008/07/29/warp_drive_2.jpg", fanart="http://tonyh.net/backgrounds/tech/wallpapers%20authors%20ps3%20space%20themes%20desktop%20backgrounds%20....jpg")

        Add_Dir( 
        name="EM Drive", url=BASE+YOUTUBE_CHANNEL_ID_4+"/", folder=True,
        icon="http://www.dailygalaxy.com/photos/uncategorized/2008/07/29/warp_drive_2.jpg", fanart="http://tonyh.net/backgrounds/tech/wallpapers%20authors%20ps3%20space%20themes%20desktop%20backgrounds%20....jpg")

        Add_Dir( 
        name="EM Drive 2", url=BASE+YOUTUBE_CHANNEL_ID_5+"/", folder=True,
        icon="http://www.dailygalaxy.com/photos/uncategorized/2008/07/29/warp_drive_2.jpg", fanart="http://tonyh.net/backgrounds/tech/wallpapers%20authors%20ps3%20space%20themes%20desktop%20backgrounds%20....jpg")

        Add_Dir( 
        name="Space Travel", url=BASE+YOUTUBE_CHANNEL_ID_6+"/", folder=True,
        icon="http://www.dailygalaxy.com/photos/uncategorized/2008/07/29/warp_drive_2.jpg", fanart="http://tonyh.net/backgrounds/tech/wallpapers%20authors%20ps3%20space%20themes%20desktop%20backgrounds%20....jpg")




#-----------------------------
@route(mode="open_folder2", args=["url"])
def Test_Folder(url):
        
        Add_Dir( 
        name="Quantum Physics Course", url=BASE+YOUTUBE_CHANNEL_ID_7+"/", folder=True,
        icon="https://cf3e497594.site.internapcdn.net/tmpl/v5/img/phys_308px.png", fanart="http://www.thejohnniechair.com/wp-content/uploads/2016/04/QuantumPhysics.jpg")

        Add_Dir( 
        name="Michio Kaku", url=BASE+YOUTUBE_CHANNEL_ID_8+"/", folder=True,
        icon="https://cf3e497594.site.internapcdn.net/tmpl/v5/img/phys_308px.png", fanart="http://www.thejohnniechair.com/wp-content/uploads/2016/04/QuantumPhysics.jpg")


#-----------------------------
@route(mode="open_folder3", args=["url"])
def Test_Folder(url):
        
        Add_Dir( 
        name="Real Life Lore", url=BASE2+YOUTUBE_CHANNEL_ID_15+"/", folder=True,
        icon="https://pbs.twimg.com/profile_images/884565411156475904/Ih43VQxG.jpg", fanart="https://i.ytimg.com/vi/E39GIysMevQ/maxresdefault.jpg")
#-----------------------------
@route(mode="open_folder4", args=["url"])
def Test_Folder(url):

        Add_Dir( 
        name="Theory of Relativity", url=BASE+YOUTUBE_CHANNEL_ID_9+"/", folder=True,
        icon="https://cdn4.iconfinder.com/data/icons/education-volume-7/48/329-512.png", fanart="https://previews.123rf.com/images/paulfleet/paulfleet0911/paulfleet091100011/5884777-Original-illustration-showing-the-link-between-space-time-and-gravity-Stock-Illustration.jpg")

        Add_Dir( 
        name="Theory of Relativity 2", url=BASE+YOUTUBE_CHANNEL_ID_10+"/", folder=True,
        icon="https://cdn4.iconfinder.com/data/icons/education-volume-7/48/329-512.png", fanart="https://previews.123rf.com/images/paulfleet/paulfleet0911/paulfleet091100011/5884777-Original-illustration-showing-the-link-between-space-time-and-gravity-Stock-Illustration.jpg")

        Add_Dir( 
        name="Theory of Relativity 3", url=BASE+YOUTUBE_CHANNEL_ID_11+"/", folder=True,
        icon="https://cdn4.iconfinder.com/data/icons/education-volume-7/48/329-512.png", fanart="https://previews.123rf.com/images/paulfleet/paulfleet0911/paulfleet091100011/5884777-Original-illustration-showing-the-link-between-space-time-and-gravity-Stock-Illustration.jpg")


#-----------------------------
@route(mode="open_folder5", args=["url"])
def Test_Folder(url):

        Add_Dir( 
        name="Hubble Space Telescope", url=BASE+YOUTUBE_CHANNEL_ID_12+"/", folder=True,
        icon="https://universegrowth.files.wordpress.com/2010/12/hubble.png", fanart="https://thefulldomeblog.files.wordpress.com/2015/10/hubblemodule1.jpg")

        Add_Dir( 
        name="Deep Space TV", url=BASE+YOUTUBE_CHANNEL_ID_13+"/", folder=True,
        icon="https://universegrowth.files.wordpress.com/2010/12/hubble.png", fanart="https://thefulldomeblog.files.wordpress.com/2015/10/hubblemodule1.jpg")


#----------------------------
@route(mode="open_folder6", args=["url"])
def Test_Folder(url):

        Add_Dir( 
        name="MIT Plasma Science and Fusion Center", url=BASE2+YOUTUBE_CHANNEL_ID_14+"/", folder=True,
        icon="https://cdn4.iconfinder.com/data/icons/iron-man-icons/512/Reactor.png", fanart="https://vignette4.wikia.nocookie.net/steamtradingcards/images/4/4b/Cities_Skylines_Background_Fusion_Power_Plant.jpg/revision/latest?cb=20150314113414")

        Add_Dir( 
        name="Tokamak Energy", url=BASE2+YOUTUBE_CHANNEL_ID_16+"/", folder=True,
        icon="https://cdn4.iconfinder.com/data/icons/iron-man-icons/512/Reactor.png", fanart="https://vignette4.wikia.nocookie.net/steamtradingcards/images/4/4b/Cities_Skylines_Background_Fusion_Power_Plant.jpg/revision/latest?cb=20150314113414")



#-----------------------------
@route(mode="open_folder7", args=["url"])
def Test_Folder(url):
           
        Add_Dir( 
        name="Colinfurze", url=BASE2+YOUTUBE_CHANNEL_ID_17+"/", folder=True,
        icon="https://inventionaday.com/wp-content/uploads/2016/09/Invention_a_day_logo.png", fanart="https://images3.alphacoders.com/278/27877.jpg")

        Add_Dir( 
        name="Zip HD", url=BASE2+YOUTUBE_CHANNEL_ID_18+"/", folder=True,
        icon="https://inventionaday.com/wp-content/uploads/2016/09/Invention_a_day_logo.png", fanart="https://images3.alphacoders.com/278/27877.jpg")

        Add_Dir( 
        name="Tech Zone", url=BASE2+YOUTUBE_CHANNEL_ID_19+"/", folder=True,
        icon="https://inventionaday.com/wp-content/uploads/2016/09/Invention_a_day_logo.png", fanart="https://images3.alphacoders.com/278/27877.jpg")
#-----------------------------
@route(mode="open_folder8", args=["url"])
def Test_Folder(url):

        Add_Dir( 
        name="Aerospace Engineering", url=BASE2+YOUTUBE_CHANNEL_ID_20+"/", folder=True,
        icon="http://www.santeriaytarot.com/images/jupiter.png", fanart="http://www.worldroom.org/wp-content/uploads/2017/07/Space-Background-1GK-room.jpg")

#-----------------------------

@route(mode="open_folder9", args=["url"])
def Test_Folder(url):

        Add_Dir( 
        name="Advexon TV", url=BASE2+YOUTUBE_CHANNEL_ID_21+"/", folder=True,
        icon="http://www.thehtpc.net/wp-content/gallery/imagesbyname/xz_genre_preview.png", fanart="https://i.pinimg.com/originals/5c/e1/44/5ce144f88cc4c2327279b97f14a5b486.jpg")

        Add_Dir( 
        name="Wired UK", url=BASE2+YOUTUBE_CHANNEL_ID_22+"/", folder=True,
        icon="http://www.thehtpc.net/wp-content/gallery/imagesbyname/xz_genre_preview.png", fanart="https://i.pinimg.com/originals/5c/e1/44/5ce144f88cc4c2327279b97f14a5b486.jpg")

        Add_Dir( 
        name="HD Documentaries", url=BASE2+YOUTUBE_CHANNEL_ID_23+"/", folder=True,
        icon="http://www.thehtpc.net/wp-content/gallery/imagesbyname/xz_genre_preview.png", fanart="https://i.pinimg.com/originals/5c/e1/44/5ce144f88cc4c2327279b97f14a5b486.jpg")
       
        Add_Dir( 
        name="Natgeo Documentary HD", url=BASE2+YOUTUBE_CHANNEL_ID_24+"/", folder=True,
        icon="http://www.thehtpc.net/wp-content/gallery/imagesbyname/xz_genre_preview.png", fanart="https://i.pinimg.com/originals/5c/e1/44/5ce144f88cc4c2327279b97f14a5b486.jpg")

        Add_Dir( 
        name="Discovery Channel", url=BASE2+YOUTUBE_CHANNEL_ID_25+"/", folder=True,
        icon="http://www.thehtpc.net/wp-content/gallery/imagesbyname/xz_genre_preview.png", fanart="https://i.pinimg.com/originals/5c/e1/44/5ce144f88cc4c2327279b97f14a5b486.jpg")

        Add_Dir( 
        name="Cold Fusion TV", url=BASE2+YOUTUBE_CHANNEL_ID_26+"/", folder=True,
        icon="http://www.thehtpc.net/wp-content/gallery/imagesbyname/xz_genre_preview.png", fanart="https://i.pinimg.com/originals/5c/e1/44/5ce144f88cc4c2327279b97f14a5b486.jpg")



#----------------------------
@route(mode="open_folder10", args=["url"])
def Test_Folder(url):

        Add_Dir( 
        name="National Geographic | Bioluminescent Creatures", url=BASE3+YOUTUBE_CHANNEL_ID_27, folder=False, mode='play_yt',
        icon="http://www.thehtpc.net/wp-content/gallery/imagesbyname/xz_genre_preview.png", fanart="https://i.pinimg.com/originals/5c/e1/44/5ce144f88cc4c2327279b97f14a5b486.jpg")

        Add_Dir( 
        name="National Geographic | Gravity - Documentary", url=BASE3+YOUTUBE_CHANNEL_ID_28, folder=False, mode='play_yt',
        icon="http://www.thehtpc.net/wp-content/gallery/imagesbyname/xz_genre_preview.png", fanart="https://i.pinimg.com/originals/5c/e1/44/5ce144f88cc4c2327279b97f14a5b486.jpg")

        Add_Dir( 
        name="David Attenborough's - Natural History Museum Alive ", url=BASE3+YOUTUBE_CHANNEL_ID_29, folder=False, mode='play_yt',
        icon="http://www.thehtpc.net/wp-content/gallery/imagesbyname/xz_genre_preview.png", fanart="https://i.pinimg.com/originals/5c/e1/44/5ce144f88cc4c2327279b97f14a5b486.jpg")

        Add_Dir( 
        name="National Geographic | Colonizing Space", url=BASE3+YOUTUBE_CHANNEL_ID_30, folder=False, mode='play_yt',
        icon="http://www.thehtpc.net/wp-content/gallery/imagesbyname/xz_genre_preview.png", fanart="https://i.pinimg.com/originals/5c/e1/44/5ce144f88cc4c2327279b97f14a5b486.jpg")
#-----------------------------
@route(mode="open_folder11", args=["url"])
def Test_Folder(url):


        Add_Dir( 
        name="Lotusland [COLOR blue]Playlist[/COLOR]", url=BASE+YOUTUBE_CHANNEL_ID_42+"/", folder=True,
        icon="https://i.pinimg.com/736x/7c/77/8e/7c778e14faa71ef6838cd81ec02196c5--succulent-terrarium-terrariums.jpg", fanart="https://wallpaperscraft.com/image/succulents_flowers_plant_110695_1920x1080.jpg")

        Add_Dir( 
        name="The Secret Language Of Plants - National Geographic Documentary", url=BASE3+YOUTUBE_CHANNEL_ID_31, folder=False, mode='play_yt',
        icon="https://i.pinimg.com/736x/7c/77/8e/7c778e14faa71ef6838cd81ec02196c5--succulent-terrarium-terrariums.jpg", fanart="https://wallpaperscraft.com/image/succulents_flowers_plant_110695_1920x1080.jpg")

        Add_Dir( 
        name="The Secret World of the Plants", url=BASE3+YOUTUBE_CHANNEL_ID_32, folder=False, mode='play_yt',
        icon="https://i.pinimg.com/736x/7c/77/8e/7c778e14faa71ef6838cd81ec02196c5--succulent-terrarium-terrariums.jpg", fanart="https://wallpaperscraft.com/image/succulents_flowers_plant_110695_1920x1080.jpg")

        Add_Dir( 
        name="Top 10 Strangest Plants On Earth", url=BASE3+YOUTUBE_CHANNEL_ID_33, folder=False, mode='play_yt',
        icon="https://i.pinimg.com/736x/7c/77/8e/7c778e14faa71ef6838cd81ec02196c5--succulent-terrarium-terrariums.jpg", fanart="https://wallpaperscraft.com/image/succulents_flowers_plant_110695_1920x1080.jpg")

        Add_Dir( 
        name="10 Plants That Could Kill You", url=BASE3+YOUTUBE_CHANNEL_ID_34, folder=False, mode='play_yt',
        icon="https://i.pinimg.com/736x/7c/77/8e/7c778e14faa71ef6838cd81ec02196c5--succulent-terrarium-terrariums.jpg", fanart="https://wallpaperscraft.com/image/succulents_flowers_plant_110695_1920x1080.jpg")

        Add_Dir( 
        name="15 Georgeous Agave Plants", url=BASE3+YOUTUBE_CHANNEL_ID_35, folder=False, mode='play_yt',
        icon="https://i.pinimg.com/736x/7c/77/8e/7c778e14faa71ef6838cd81ec02196c5--succulent-terrarium-terrariums.jpg", fanart="https://wallpaperscraft.com/image/succulents_flowers_plant_110695_1920x1080.jpg")

        Add_Dir( 
        name="Attila's Garden", url=BASE3+YOUTUBE_CHANNEL_ID_36, folder=False, mode='play_yt',
        icon="https://i.pinimg.com/736x/7c/77/8e/7c778e14faa71ef6838cd81ec02196c5--succulent-terrarium-terrariums.jpg", fanart="https://wallpaperscraft.com/image/succulents_flowers_plant_110695_1920x1080.jpg")

        Add_Dir( 
        name="Collection at the National Botanic Gardens of Ireland", url=BASE3+YOUTUBE_CHANNEL_ID_37, folder=False, mode='play_yt',
        icon="https://i.pinimg.com/736x/7c/77/8e/7c778e14faa71ef6838cd81ec02196c5--succulent-terrarium-terrariums.jpg", fanart="https://wallpaperscraft.com/image/succulents_flowers_plant_110695_1920x1080.jpg")

        Add_Dir( 
        name="Some Rare and Unusual Cacti and Succulents", url=BASE3+YOUTUBE_CHANNEL_ID_38, folder=False, mode='play_yt',
        icon="https://i.pinimg.com/736x/7c/77/8e/7c778e14faa71ef6838cd81ec02196c5--succulent-terrarium-terrariums.jpg", fanart="https://wallpaperscraft.com/image/succulents_flowers_plant_110695_1920x1080.jpg")

        Add_Dir( 
        name="Arid Garden at the Royal Botanic Gardens Melbourne", url=BASE3+YOUTUBE_CHANNEL_ID_39, folder=False, mode='play_yt',
        icon="https://i.pinimg.com/736x/7c/77/8e/7c778e14faa71ef6838cd81ec02196c5--succulent-terrarium-terrariums.jpg", fanart="https://wallpaperscraft.com/image/succulents_flowers_plant_110695_1920x1080.jpg")

        Add_Dir( 
        name="Flying through Lotusland", url=BASE3+YOUTUBE_CHANNEL_ID_40, folder=False, mode='play_yt',
        icon="https://i.pinimg.com/736x/7c/77/8e/7c778e14faa71ef6838cd81ec02196c5--succulent-terrarium-terrariums.jpg", fanart="https://wallpaperscraft.com/image/succulents_flowers_plant_110695_1920x1080.jpg")

        Add_Dir( 
        name="Mysterious Lotusland", url=BASE3+YOUTUBE_CHANNEL_ID_41, folder=False, mode='play_yt',
        icon="https://i.pinimg.com/736x/7c/77/8e/7c778e14faa71ef6838cd81ec02196c5--succulent-terrarium-terrariums.jpg", fanart="https://wallpaperscraft.com/image/succulents_flowers_plant_110695_1920x1080.jpg")

        Add_Dir( 
        name="World's Most Famous Botanical Gardens", url=BASE3+YOUTUBE_CHANNEL_ID_43, folder=False, mode='play_yt',
        icon="https://i.pinimg.com/736x/7c/77/8e/7c778e14faa71ef6838cd81ec02196c5--succulent-terrarium-terrariums.jpg", fanart="https://wallpaperscraft.com/image/succulents_flowers_plant_110695_1920x1080.jpg")

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
@route(mode="video", args=["url"])
def Play_Video(url):
    
    xbmc.executebuiltin('PlayMedia(plugin://plugin.video.vimeo/video%s)'%url)

#-----------------------------------


if __name__ == "__main__":
    Run(default='main')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))