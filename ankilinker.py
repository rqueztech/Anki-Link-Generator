import win32gui
import pyautogui
import time

def findwindowbytitle(windowtitle):
    return win32gui.FindWindow(None, windowtitle)

def bringtoforefront(window_handle):
    return win32gui.SetForegroundWindow(window_handle)

def windowops():
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    bringtoforefront(powershell_handle)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    bringtoforefront(anki_handle)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v') 
    time.sleep(2)

def tabtimes(times):
    for x in range(times):
        pyautogui.press('tab')

powershell_handle = findwindowbytitle("Windows Powershell ISE (x86)")
anki_handle = findwindowbytitle("Browse (1 of 1000 notes selected)")

space_between_list = 6
space_between_first_link = 5

if anki_handle != None and powershell_handle != None:
    for x in range(600):
        bringtoforefront(anki_handle)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'shift', 'l')
        time.sleep(1)
        pyautogui.press('down')
        time.sleep(.2)
        tabtimes(space_between_list)
        windowops()
        tabtimes(space_between_first_link)
        windowops()

    
