# -*- coding: utf-8 -*-
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: Tonys Toons addon
# Author: TonyH
#-----------------------------

import os, sys, re, requests
import urlparse
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import urllib2
from BeautifulSoup import BeautifulSoup
import urllib
#-----------------------------

player = xbmc.Player()
video1 = "http://archive.org/download/The_Flintstones_Series/The Flintstones - 5x20 - Moonlight And Maintenance.mp4"
flint_fanart = "http://rcartoons.com/wp-content/uploads/2017/09/The-Flintstones-HD-Images.jpg"
flint_icon = "https://orig00.deviantart.net/0a02/f/2015/161/c/8/the_flintstones_folder_icon_2_by_gterritory-d8wqbei.png"
main_fanart = "https://images4.alphacoders.com/194/thumb-1920-194984.jpg"
main_icon = "https://orig00.deviantart.net/4b17/f/2016/040/8/8/cartoon_icon_folder_by_mohandor-d9r5mry.png"
bugs_icon = ""
bugs_fanart = ""




#-----------------------------

addon_handle = int(sys.argv[1])

#-----------------------------

def addDir(dir_type, mode, url, name, iconimage, fanart):
    base_url = sys.argv[0]
    base_url += "?url="     + urllib.quote_plus(url)
    base_url += "&mode="    + str(mode)
    base_url += "&name="    + urllib.quote_plus(name)
    base_url += "&iconimage="   + urllib.quote_plus(iconimage)
    base_url += "fanrt"     + urllib.quote_plus(fanart)

    li = xbmcgui.ListItem(name, iconImage=iconimage)

    li.setInfo(type="Video", infoLabels={"Title": name})
    li.setProperty("Fanart_Image", fanart)

    if dir_type != '':
        link = xbmcplugin.addDirectoryItem(handle=addon_handle,url=base_url,listitem=li,isFolder=True)

    else:
        link = xbmcplugin.addDirectoryItem(handle=addon_handle,url=url,listitem=li,isFolder=False)

    return link                             

#-----------------------------

def Bugs_Bunny():
    
    _url_ = 'the-bugs-bunny-show/season/1'
    show = ('http://www.cartoonson.com/cartoons/view/id/' + (_url_))
    page = urllib2.urlopen(show)
    soup = BeautifulSoup(page)
    page.close()
    containers = soup.findAll("div", {"class":"col-sm-9 col-xs-10"})
    container = containers[0]
    links = container.findAll("a", {"class":"pull-right play-episode-btn btn btn-default"})


    for link in links:
        href = link["href"]
        final_href = href.replace('-preview', '')
        

    Links = container.findAll("a")

    for link in Links:
        name = link.text
        final_name = name.replace('&#039;', '')
        
    
    addDir('', '', final_href, final_name, bugs_icon, bugs_fanart)
#-----------------------------

def Flintstones():

    pre = "http://archive.org"
    page = urllib2.urlopen("https://archive.org/details/The_Flintstones_Series")
    soup = BeautifulSoup(page)
    page.close()
    containers = soup.findAll("div", {"class":"quickdown"})
    container = containers[2]
    links = container.findAll("a")

    for link in links:
        href = link["href"]
        fix_link = href.replace('+', '%20')
        final_link = (pre + fix_link)
        name = link.text
        fix_name = name.replace('.mp4download', '') 
        final_name = fix_name.replace('+', ' ')
        



        addDir('', '', final_link, final_name, flint_icon, flint_fanart)


#-----------------------------

def Main_Menu():
    addDir('folder', 'flintstones', '', 'The Flintstones', main_icon, main_fanart)
    addDir('folder', 'bugs_bunny', '', 'The Bugs Bunny Show', main_icon, main_fanart)

#-----------------------------

# def _show_(_url_):
#     show = ('http://www.cartoonson.com/cartoons/view/id/' + (_url_))
#     page = urllib2.urlopen(show)
#     soup = BeautifulSoup(page)
#     page.close()
#-----------------------------    

mode = None

args = sys.argv[2]

if len(args) > 0:
    mode = args.split('mode=')
    mode = mode[1].split('&')
    mode = mode[0]

if mode == None : Main_Menu()
elif mode == 'flintstones' : Flintstones()
elif mode == 'bugs_bunny' : Bugs_Bunny()

xbmcplugin.endOfDirectory(addon_handle)



