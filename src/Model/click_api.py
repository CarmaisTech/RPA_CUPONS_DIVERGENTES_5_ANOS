import win32api, win32con
import time


def click2(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    #time.sleep(0.5) #click for 1 s. Too fast and click wont register
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
