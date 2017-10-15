# -*- coding: utf-8 -*-
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: My Test xml adddon
# Author: TonyH
#-----------------------------

import __builtin__

# change these to suit your addons
root_xml_url = "http://tonyh.net/xml%20files/video.xml"  # url of the root xml file
__builtin__.tvdb_api_key = ""  # tvdb api key
__builtin__.tmdb_api_key = ""  # tmdb api key
__builtin__.trakt_client_id = ""  # trakt client id
__builtin__.trakt_client_secret = ""  # trakt client secret

import os
import sys

import koding
import koding.router as router
import resources.lib.sources
import resources.lib.testings
import resources.lib.util.info
import xbmc
import xbmcaddon
import xbmcplugin
from koding import Add_Dir  
from koding import route, Run 
from koding import route, Addon_Setting, Add_Dir, Find_In_Text, Open_URL, OK_Dialog
from koding import Open_Settings, Play_Video, Run, Text_File
from resources.lib.util.xml import JenList, display_list
import resources.lib.util.views

#----------------------------

# Addon Variables
addon_id = xbmcaddon.Addon().getAddonInfo('id')
addon_name = xbmcaddon.Addon().getAddonInfo('name')
home_folder = xbmc.translatePath('special://home/')
addon_folder = os.path.join(home_folder, 'addons')
art_path = os.path.join(addon_folder, addon_id)
content_type = "files"

#----------------------------

@route("main")
def root():
    """root menu of the addon"""
    base = "http://tonyh.net/xml%20files/nat_geo_xmls/opening_xml.xml"
    if not get_list(base):
        koding.Add_Dir(
            name="Message",
            url="Sorry, server is down",
            mode="message",
            folder=True,
            icon=xbmcaddon.Addon().getAddonInfo("icon"),
            fanart=xbmcaddon.Addon().getAddonInfo("fanart"),
            content_type="")
        koding.Add_Dir(
            name="Testings",
            url='{"file_name":"testings.xml"}',
            mode="Testings",
            folder=True,
            icon=xbmcaddon.Addon().getAddonInfo("icon"),
            fanart=xbmcaddon.Addon().getAddonInfo("fanart"),
            content_type="")

#----------------------------

@route(mode="get_list", args=["url"])
def get_list(url):
    """display jen list"""
    global content_type
    jen_list = JenList(url)
    items = jen_list.get_list()
    content = jen_list.get_content_type()
    if items == []:
        return False
    if content:
        content_type = content
    display_list(items, content_type)
    return True

#----------------------------

def get_addon_url(mode, url=""):
    import urllib
    result = sys.argv[0] + "?mode=%s" % mode

    if url:
        result += "&url=%s" % urllib.quote_plus(url)
    return result


if xbmc.getInfoLabel("Container.FolderName") == "":
    __builtin__.JEN_WIDGET = True
else:
    __builtin__.JEN_WIDGET = False

router.Run()

xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=False)
if not xbmcaddon.Addon().getSetting("first_run") == "true":
    resources.lib.util.views.set_list_view_mode(content_type)

