import win32gui
import pyautogui
import time

anki_window_handle = win32gui.FindWindow(None, "Browse (1 of 1000 notes selected)")
win32gui.SetForegroundWindow(anki_window_handle)


pyautogui.hotkey('ctrl', 'shift', 'l')

for x in range(1):
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'x')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'x')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('ctrl', 'shift', 'l')
    pyautogui.hotkey('down')
    time.sleep(.3)
