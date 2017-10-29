# -*- coding: utf-8 -*-
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: Tonys Toons addon
# Author: TonyH
# some code from Danymedia, many thanks!
#-----------------------------

import os, sys, re, requests
import urlparse
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import urllib2
from BeautifulSoup import BeautifulSoup
import urllib
import urlresolver

#-----------------------------

player = xbmc.Player()
s = requests.session() 
User_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
BASEURL = 'http://www.cartoonson.com/'
BASEURL2= 'http://www.cartoonson.com'
addon_id='plugin.video.Tonys_Toons'
PATH = 'Tonys_Toons'
ADDON      = xbmcaddon.Addon()
VERSION = ADDON.getAddonInfo('version')
#-----------------------------

def Main_menu():
     addDir('[B][COLOR white]The Bugs Bunny Show[/COLOR][/B]',BASEURL + 'cartoons/view/id/the-bugs-bunny-show',2,BASEURL + '_resources/Cartoons/show/13/image/555x418/bugs-bunny-show.jpg',BASEURL + '_resources/Cartoons/show/13/image/555x418/bugs-bunny-show.jpg','')
     addDir('[B][COLOR white]Tom and Jerry[/COLOR][/B]',BASEURL + 'cartoons/view/id/tom-and-jerry-classic-collection',2,BASEURL + '_resources/Cartoons/show/12/image/555x418/Tom-and-Jerry-classic.jpg',BASEURL + '_resources/Cartoons/show/12/image/555x418/Tom-and-Jerry-classic.jpg','')
     addDir('[B][COLOR white]The Flintstones[/COLOR][/B]',BASEURL + 'cartoons/view/id/the-flintstones-tv-series',2,BASEURL + '_resources/Cartoons/show/14/image/555x418/The-Flintstone-TV-series.jpg',BASEURL + '_resources/Cartoons/show/14/image/555x418/The-Flintstone-TV-series.jpg','')
     addDir('[B][COLOR white]Courage the Cowardly Dog[/COLOR][/B]',BASEURL + 'cartoons/view/id/courage-the-cowardly-dog',2,BASEURL + '_resources/Cartoons/show/7/image/555x418/courage-the-cowardly-dog-show.jpg',BASEURL + '_resources/Cartoons/show/7/image/555x418/courage-the-cowardly-dog-show.jpg','')
     addDir('[B][COLOR white]Family Guy[/COLOR][/B]',BASEURL + 'cartoons/view/id/family-guy-tv-series',2,BASEURL + '_resources/Cartoons/show/18/image/555x418/family-guy.jpg',BASEURL + '_resources/Cartoons/show/18/image/555x418/family-guy.jpg','')
     addDir('[B][COLOR white]The Porky Pig Show (1964-1967)[/COLOR][/B]',BASEURL + 'cartoons/view/id/the-porky-pig-full-episodes',2,BASEURL + '_resources/Cartoons/show/80/image/555x418/porky_pig_wallpaper.jpg',BASEURL + '_resources/Cartoons/show/80/image/555x418/porky_pig_wallpaper.jpg','')
     addDir('[B][COLOR white]The Jetsons (1962-1963)[/COLOR][/B]',BASEURL + 'cartoons/view/id/the-jetsons-tv-series-1962-1963',2,BASEURL + '_resources/Cartoons/show/35/image/555x418/jetsons.jpg',BASEURL + '_resources/Cartoons/show/35/image/555x418/jetsons.jpg','')
     addDir('[B][COLOR white]Wile E. Coyote and The Road Runner[/COLOR][/B]',BASEURL + 'cartoons/view/id/wile-e-coyote-and-the-road-runner',2,BASEURL + '_resources/Cartoons/show/39/image/555x418/Wile_E._Coyote_and_The_Road_Runner.jpg',BASEURL + '_resources/Cartoons/show/39/image/555x418/Wile_E._Coyote_and_The_Road_Runner.jpg','')
     addDir('[B][COLOR white]Justice League (2001-2004)[/COLOR][/B]',BASEURL + 'cartoons/view/id/justice-league-tv-series-2001-2004',2,BASEURL + '_resources/Cartoons/show/28/image/555x418/Justice_League_TV_Series_20012004.jpg',BASEURL + '_resources/Cartoons/show/28/image/555x418/Justice_League_TV_Series_20012004.jpg','')
     addDir('[B][COLOR white]Rick and Morty[/COLOR][/B]',BASEURL + 'cartoons/view/id/rick-and-morty-tv-series',2,BASEURL + '_resources/Cartoons/show/25/image/555x418/rick-and-morty.jpg',BASEURL + '_resources/Cartoons/show/25/image/555x418/rick-and-morty.jpg','')

#-----------------------------

def Open_Url(url):
    headers = {}
    headers['User-Agent'] = User_Agent
    link = s.get(url, headers=headers).text
    link = link.encode('ascii', 'ignore')
    return link
#-----------------------------

def addDir(name,url,mode,iconimage,fanart,description):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={"Title": name,"Plot":description})
    liz.setProperty('fanart_image', fanart)
    if mode==100 or mode==150:
        liz.setProperty("IsPlayable","true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    else:
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok

#----------------------------- 

def resolve(name,url,iconimage,description):
    OPEN = Open_Url(url)
    try:
        url = re.compile('<source.+?src="(.+?)">',re.DOTALL).findall(OPEN)[0]
        if 'bit.ly' in url:
            headers = {'User-Agent': User_Agent}
            r = requests.get(url,headers=headers,allow_redirects=False)
            url = r.headers['location']
        elif 'blogspot' in url:
            liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
            liz.setInfo(type="Video", infoLabels={"Title": description})
            liz.setProperty("IsPlayable","true")
            liz.setPath(url)
            xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
        else:
            url=urlresolver.resolve(url)
    except:
        url = re.compile('<iframe.+?src="(.+?)">',re.DOTALL).findall(OPEN)[0]
        if 'bit.ly' in url:
            headers = {'User-Agent': User_Agent}
            r = requests.get(url,headers=headers,allow_redirects=False)
            url = r.headers['location']
        elif 'blogspot' in url:
            liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
            liz.setInfo(type="Video", infoLabels={"Title": description})
            liz.setProperty("IsPlayable","true")
            liz.setPath(url)
            xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
        else:
            url=urlresolver.resolve(url)
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": description})
    liz.setProperty("IsPlayable","true")
    liz.setPath(url)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)

#----------------------------    

def shows_Menu(url):
    OPEN = Open_Url(url)
    if '<h3><span>Seasons</span></h3>' in OPEN:
        holderpage = re.compile('<h3 class="text-center".+?href="(.+?)">(.+?)</a></h3>',re.DOTALL).findall(OPEN)
        for url,name in holderpage:
            addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,iconimage,iconimage,'')
    else:
        Regex = re.compile('data-parent=.+?href=".+?".+?href="(.+?)".+?<p>(.+?)</p>',re.DOTALL).findall(OPEN)
        for url,name, in Regex:
                url = url.replace('watch-preview','watch')
                name = name.replace('Watch ','').replace('- Cartoon for kids','').replace('online in HD','').replace('full movie','').replace('in awesome quality on any device.','').replace('in high quality','').replace('online ','').replace(' on all devices','').replace(' for free','')
                if 'Booba' in name:
                    addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,150,iconimage,iconimage,'')
                else:
                    addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,100,iconimage,iconimage,'')

#------------------------------                    
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2: 
                params=sys.argv[2] 
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}    
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param
        
params=get_params()
url=None
name=None
iconimage=None
mode=None
fanart=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
        
        
print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)
#########################################################
    
if mode == None: Main_menu()
elif mode == 2 : shows_Menu(url)
elif mode == 100 : resolve(name,url,iconimage,description)

xbmcplugin.endOfDirectory(int(sys.argv[1]))



