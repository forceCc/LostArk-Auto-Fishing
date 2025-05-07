import subprocess
from random import randint
import pyautogui
import time
import random
from pathlib import Path


def consume():
    count = 0
    while True:
        if count % 3 == 0:
            pyautogui.press("1", interval=random.uniform(1.9, 2.0))
            pyautogui.press("4", interval=random.uniform(1.9, 2.0))
            pyautogui.press("3", interval=random.uniform(1.9, 2.0))
            pyautogui.press("2", interval=random.uniform(4.4, 4.5))
        else:
            pyautogui.press("1", interval=random.uniform(10.1, 10.2))
        count += 1


def refine(count=100, delay=(0.1, 0.2)):
    pyautogui.moveTo(randint(930, 1000), randint(750, 770))
    for _ in range(count):
        pyautogui.leftClick()
        time.sleep(random.uniform(*delay))


def click(x, y, delay_range=(0.5, 0.6)):
    pyautogui.moveTo(x, y)
    pyautogui.leftClick()
    pyautogui.click()
    time.sleep(random.uniform(*delay_range))


def recruit():
    for _ in range(10):
        steps = [
            (570, 480),
            (730, 490),
            (1380, 840),
            (760, 590),
            (1360, 752),
            (760, 590),
            (1700, 170),
        ]

        for x, y in steps:
            click(x, y)

        time.sleep(random.uniform(4.0, 4.5))
        click(570, 480)


def adb_tap(x, y, clicks=1, interval=0.0):
    for _ in range(clicks):
        cmd = f"adb shell input tap {x} {y}"
        subprocess.run(cmd, shell=True)
        interval = float(interval)
        time.sleep(interval)


def adb_swipe(x1, y1, x2, y2, duration=500):
    cmd = f"adb shell input swipe {x1} {y1} {x2} {y2} {duration}"
    subprocess.run(cmd, shell=True)


def rename(fp):
    folder_path = Path(fp)
    files = folder_path.iterdir()
    for index, file_path in enumerate(files, start=0):
        new_filename = f"template{index}{file_path.suffix}"
        new_file_path = folder_path / new_filename
        file_path.rename(new_file_path)


if __name__ == "__main__":
    rename("datasets/images/train")
