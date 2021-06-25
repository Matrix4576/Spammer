import pyautogui
import time
time.sleep(5)
f = open('C:\\Users\\Agniva Roy\\PycharmProjects\\Spamer\\spam.txt', 'r')
for words in f:
    pyautogui.typewrite(words)
    pyautogui.press('enter')
