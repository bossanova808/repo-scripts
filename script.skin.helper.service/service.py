#!/usr/bin/python
# -*- coding: utf-8 -*-

import resources.lib.Utils as utils
from resources.lib.BackgroundsUpdater import BackgroundsUpdater
from resources.lib.ListItemMonitor import ListItemMonitor
from resources.lib.KodiMonitor import Kodi_Monitor
from resources.lib.WebService import WebService
import xbmc


class Main:
    
    def __init__(self):
        
        KodiMonitor = Kodi_Monitor()
        listItemMonitor = ListItemMonitor()
        backgroundsUpdater = BackgroundsUpdater()
        webService = WebService()
        lastSkin = None
                   
        #start the extra threads
        listItemMonitor.start()
        backgroundsUpdater.start()
        webService.start()
        
        while not KodiMonitor.abortRequested():
            
            #set skin info
            currentSkin = xbmc.getSkinDir()
            if lastSkin != currentSkin:
                utils.setSkinVersion()
                lastSkin = currentSkin
            
            KodiMonitor.waitForAbort(10)
        else:
            # Abort was requested while waiting. We should exit
            utils.logMsg('Shutdown requested !',0)
            #stop the extra threads
            backgroundsUpdater.stop()
            listItemMonitor.stop()
            webService.stop()

utils.logMsg('skin helper service version %s started' % utils.ADDON_VERSION,0)
Main()
utils.logMsg('skin helper service version %s stopped' % utils.ADDON_VERSION,0)
