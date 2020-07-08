
import win32gui, win32con, win32api
import configparser

#from config.py import character_name

cfg = configparser.ConfigParser()
cfg.read('config.ini')

characterName = cfg['Character']['name']

gameWindow = 'Tibia - ' + characterName

def send_key(key):

    handle = win32gui.FindWindow(None, gameWindow)

    # TODO: make it work with non-character messages as well
    win32api.PostMessage(handle, win32con.WM_CHAR, ord(key))

def send_char():
    pass

def send_vk():
    pass