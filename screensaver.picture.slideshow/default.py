import os, sys
import xbmc, xbmcaddon

ADDON    = xbmcaddon.Addon()
ADDONID  = ADDON.getAddonInfo('id')
CWD      = ADDON.getAddonInfo('path').decode("utf-8")
LANGUAGE = ADDON.getLocalizedString
RESOURCE = xbmc.translatePath( os.path.join( CWD, 'resources', 'lib' ).encode("utf-8") ).decode("utf-8")

sys.path.append(RESOURCE)

from utils import *

if __name__ == '__main__':
    import gui
    screensaver_gui = gui.Screensaver('script-python-slideshow.xml', CWD, 'default')
    screensaver_gui.doModal()
    del screensaver_gui
