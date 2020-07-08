
import win32gui
import win32con
import win32api

#from config.py import character_name

gameWindow = 'Tibia - ' + 'Sabe Quem Eh'

def send_key(key):

    handle = win32gui.FindWindow(None, gameWindow)

    # TODO: make it work with non-character messages as well
    win32api.PostMessage(handle, win32con.WM_CHAR, ord(key))