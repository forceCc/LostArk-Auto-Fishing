import numpy as np
import pyautogui
import cv2
from time import sleep
import random
import yaml
from PIL import Image


def loadConfig():
    with open("resources/config.yaml", mode="r", encoding="utf-8") as yamlfile:
        config = yaml.safe_load(yamlfile)
    return config


def init(config):
    global \
        template, \
        perfect_zone, \
        moving_arrow, \
        esc_btn, \
        fishing_region, \
        available_region, \
        game_bar_region, \
        esc_btn_region
    template = cv2.imread(config["fishing"]["image"]["template"], 0)
    perfect_zone = Image.open(config["miniGame"]["image"]["perfect_zone"])
    moving_arrow = Image.open(config["miniGame"]["image"]["moving_arrow"])
    esc_btn = Image.open(config["miniGame"]["image"]["esc_btn"])
    fishing_region = config["fishing"]["region"]
    available_region = config["miniGame"]["region"]["available"]
    game_bar_region = config["miniGame"]["region"]["game_bar"]
    esc_btn_region = config["miniGame"]["region"]["esc_btn"]
    print("🔧 初始化完成！")


def castFish(counter):
    print(f"🎣 抛竿中... 第 {counter} 次")
    pyautogui.press(config["fishing"]["key"], interval=random.uniform(5.5, 6.5))


def castNet():
    pyautogui.press(config["miniGame"]["key"], interval=random.uniform(6.5, 7.0))
    perfect_zone_loc = pyautogui.locateOnScreen(
        image=perfect_zone,
        region=game_bar_region,
        confidence=0.9,
    )
    y = perfect_zone_loc.top - 25
    while True:
        arrow_loc = pyautogui.locateOnScreen(
            image=moving_arrow,
            grayscale=True,
            region=game_bar_region,
            confidence=0.7,
        )
        if arrow_loc is not None and arrow_loc.top > y:
            pyautogui.press("space", 3, interval=random.uniform(0.1, 0.2))
        esc_loc = pyautogui.locateOnScreen(
            image=esc_btn,
            grayscale=True,
            region=esc_btn_region,
            confidence=0.9,
        )
        if esc_loc is None:
            sleep(random.uniform(5.5, 6.5))
            break


def startFishing():
    flag = 0
    counter = 0
    idletimer = 0
    while True:
        idletimer += 1

        if flag == 0:
            flag = 1
            counter += 1
            castFish(counter)

        screenshot = pyautogui.screenshot(region=fishing_region)
        image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)

        template_match = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
        template_loc = np.where(template_match >= 0.7)

        if len(template_loc[0]) > 0 and flag == 1:
            print("🐟 鱼上钩了！\n")
            flag = 0
            idletimer = 0
            sleep(random.uniform(0.1, 0.2))
            pyautogui.press(config["fishing"]["key"], interval=random.uniform(6.5, 7.5))

            screenshot = pyautogui.screenshot(region=available_region)
            image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
            if np.mean(image) > 100:
                castNet()

        if idletimer >= 500:
            print("⌛ 空闲时间过长，重新抛竿！\n")
            flag = 1
            idletimer = 0
            counter += 1
            castFish(counter)


def main():
    global config
    config = loadConfig()
    init(config)
    sec_timer = 3
    print(f"🟢 {sec_timer} 秒后启动钓鱼机器人\n")
    sleep(sec_timer)
    startFishing()


if __name__ == "__main__":
    main()
