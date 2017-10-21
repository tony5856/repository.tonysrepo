# -*- coding: utf-8 -*-
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: Flintstones addon
# Author: TonyH
#-----------------------------

import os, sys
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import urllib2
from BeautifulSoup import BeautifulSoup

#-----------------------------

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'movies')
icon1 = "https://orig00.deviantart.net/efd2/f/2016/216/f/1/the_flintstones_folder_icon_by_dahlia069-daclome.png"
fanart1 = "http://rcartoons.com/wp-content/uploads/2017/09/The-Flintstones-HD-Images.jpg"
#-----------------------------

def addDir(url, title, icon):
	li = xbmcgui.ListItem(title, iconImage=icon)
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li,)


pre = "http://archive.org"
page = urllib2.urlopen("https://archive.org/details/The_Flintstones_Series")
soup = BeautifulSoup(page)
page.close()
containers = soup.findAll("div", {"class":"quickdown"})
container = containers[2]
links = container.findAll("a")

for link in links:
    href = link["href"]
    name = link.text
    final_name = name.replace('.mp4download', '')
    addDir(title=final_name, url=(pre + href), icon="icon1")








xbmcplugin.endOfDirectory(addon_handle)










#xbmc.log(str(containers))










#xbmc.log(soup.prettify())






