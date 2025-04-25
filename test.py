import random
import pyautogui
from time import sleep

count = 0
print("Start in 3s.")
sleep(3)
while True:
    if count % 3 == 0:
        pyautogui.press("1", interval=random.uniform(1.9, 2.0))
        pyautogui.press("4", interval=random.uniform(1.9, 2.0))
        pyautogui.press("3", interval=random.uniform(1.9, 2.0))
        pyautogui.press("2", interval=random.uniform(4.4, 4.5))
    else:
        pyautogui.press("1", interval=random.uniform(10.1, 10.2))
    count += 1
