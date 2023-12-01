# -*- coding:utf-8 -*-
from pymouse import PyMouse
from pykeyboard import *
import win32gui
from PIL import ImageGrab, Image
import numpy as np
import operator
import time
import random
# import pyautogui

m = PyMouse()
k = PyKeyboard()

class GameAssist:
    def __init__(self, wdname, img):
        # 购买物品标准图片 32*32
        self.standard = np.array(img.convert('L')).flatten()

        # 取得窗口句柄
        self.hwnd = win32gui.FindWindow(0, wdname)
        if not self.hwnd:
            print('窗口找不到，请确认窗口句柄名称：【%s】' % wdname)

        # 窗口显示最前面
        win32gui.SetForegroundWindow(self.hwnd)

        # 主截图的左上角坐标和右下角坐标
        self.main = (447, 147)
        # self.scree_left_and_right_point = (800, 278, 1121, 502)
        # self.scree_left_and_right_point = (self.main[0]+353, self.main[1]+136, self.main[0]+674, self.main[1]+362)
        self.scree_left_and_right_point = (self.main[0]+382, self.main[1]+272, self.main[0]+641, self.main[1]+400)
        # self.scree_left_and_right_point = (337, 261, 656, 483)

        # 坐标
        self.xl_coordinate = [self.main[0]+983, self.main[1]+215]
        self.zb_coordinate = [self.main[0]+928, self.main[0]+960, self.main[1]+468]
        self.yd_coordinate = [self.main[0]+1000, self.main[1]+468]
        self.difu_coordinate = [self.main[0]+618, self.main[1]+371]
        self.mengpo_coordinate = [self.main[0]+935, self.main[1]+297]
        self.loulan_coordinate = [self.main[0]+70, self.main[1]+307]
        self.gaochang_coordinate = [self.main[0]+930, self.main[1]+372]
        self.migong_coordinate = [self.main[0]+930, self.main[1]+322]
        self.queding_coordinate = [self.main[0]+570, self.main[1]+387]
        self.zhenshou_coordinate = [self.main[0]+201, self.main[1]+753]
        self.xunlian_coordinate = [self.main[0]+141, self.main[1]+426]
        self.chuzhan_coordinate = [self.main[0]+140, self.main[1]+445]
        self.guanbi_coordinate = [self.main[0]+486, self.main[1]+114]
        self.zidong_coordinate = [self.main[0]+1004, self.main[1]+126]
        self.hys_coordinate = [self.main[0]+936, self.main[1]+302]
        self.zuoji_coordinate = [self.main[0]+1005, self.main[1]+509]

        # PyMouse对象，鼠标点击
        self.mouse = PyMouse()

        # 移动距离
        self.high = 38
        self.wide = 164.5

        # 图片大小
        self.size = 32

        self.flag = 1

    def screenshot(self):
        image = ImageGrab.grab(self.scree_left_and_right_point)

        return image

    def contrast(self, image):
        keep, k_mse = 0, 100
        image = np.array(image.convert('L')).flatten()
        mse = (((image - self.standard) ** 2) / len(self.standard)).sum()
        if mse < k_mse:
            keep = 1
        return keep

    def typing(self, message):
        k = PyKeyboard()
        self.move_click(self.xl_coordinate[0], self.xl_coordinate[1], 1, 2)
        time.sleep(1)
        self.move_click(self.zb_coordinate[0], self.zb_coordinate[2], 1, 2)
        time.sleep(1)
        self.move_click(self.zb_coordinate[0], self.zb_coordinate[2], 1, 2)
        time.sleep(1)
        k.type_string(message[0])
        time.sleep(1)
        self.move_click(self.zb_coordinate[1], self.zb_coordinate[2], 1, 2)
        time.sleep(1)
        self.move_click(self.zb_coordinate[1], self.zb_coordinate[2], 1, 2)
        time.sleep(1)
        k.type_string(message[1])
        time.sleep(1)
        self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 1, 2)
        time.sleep(1)
        self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 1, 2)
        time.sleep(2)

    def move_click(self, target_x, target_y, button, n):
        xs, ys, i = 0, 0, 0
        k = PyKeyboard()
        x, y = m.position()
        if target_x > x and target_y > y:
            for xs in range(target_x - x):
                m.move(x + xs + random.randint(0, 3), y + random.randint(0, 3))
                if random.random() <= 0.1:
                    time.sleep(random.randint(1, 10) * 0.001)
            for ys in range(target_y - y):
                m.move(x + xs + random.randint(0, 3), y + ys + random.randint(0, 3))
                if random.random() <= 0.1:
                    time.sleep(random.randint(1, 10) * 0.001)
        elif target_x > x and target_y < y:
            for xs in range(target_x - x):
                m.move(x + xs + random.randint(0, 3), y + random.randint(0, 3))
                if random.random() <= 0.1:
                    time.sleep(random.randint(1, 10) * 0.001)
            for ys in range(y - target_y):
                m.move(x + xs + random.randint(0, 3), y - ys + random.randint(0, 3))
                if random.random() <= 0.1:
                    time.sleep(random.randint(1, 10) * 0.001)
        elif target_x < x and target_y > y:
            for xs in range(x - target_x):
                m.move(x - xs + random.randint(0, 3), y + random.randint(0, 3))
                if random.random() <= 0.1:
                    time.sleep(random.randint(1, 10) * 0.001)
            for ys in range(target_y - y):
                m.move(x - xs + random.randint(0, 3), y + ys + random.randint(0, 3))
                if random.random() <= 0.1:
                    time.sleep(random.randint(1, 10) * 0.001)
        else:
            for xs in range(x - target_x):
                m.move(x - xs + random.randint(0, 3), y + random.randint(0, 3))
                if random.random() <= 0.1:
                    time.sleep(random.randint(1, 10) * 0.001)
            for ys in range(y - target_y):
                m.move(x - xs + random.randint(0, 3), y - ys + random.randint(0, 3))
                if random.random() <= 0.1:
                    time.sleep(random.randint(1, 10) * 0.001)
        time.sleep(1)
        k.tap_key(k.function_keys[8])
        time.sleep(1)
        k.tap_key(k.function_keys[8])

    # 程序入口、控制中心
    def start(self):
        k = PyKeyboard()
        message = ['212', '212']
        # 1. 开始
        image = self.screenshot()
        keep = self.contrast(image)
        if keep == 1:
            self.move_click(self.difu_coordinate[0], self.difu_coordinate[1], 1, 2)
            time.sleep(8)
            self.move_click(self.xl_coordinate[0], self.xl_coordinate[1], 1, 2)
            time.sleep(1)
            self.move_click(self.mengpo_coordinate[0], self.mengpo_coordinate[1], 1, 2)
            time.sleep(1)
            self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 1, 2)
            time.sleep(1)
            self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 1, 2)
            time.sleep(8)
            self.move_click(self.loulan_coordinate[0], self.loulan_coordinate[1], 1, 2)
            time.sleep(1)
            self.move_click(self.loulan_coordinate[0], self.loulan_coordinate[1], 1, 2)
            time.sleep(8)
            self.move_click(self.zuoji_coordinate[0], self.zuoji_coordinate[1], 1, 2)
            time.sleep(8)
            self.move_click(self.xl_coordinate[0], self.xl_coordinate[1], 1, 2)
            time.sleep(1)
            self.move_click(self.gaochang_coordinate[0], self.gaochang_coordinate[1], 1, 2)
            time.sleep(1)
            self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 1, 2)
            time.sleep(1)
            self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 1, 2)
            time.sleep(8)
            self.move_click(self.xl_coordinate[0], self.xl_coordinate[1], 1, 2)
            time.sleep(1)
            self.move_click(self.hys_coordinate[0], self.hys_coordinate[1], 1, 2)
            time.sleep(1)
            self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 1, 2)
            time.sleep(1)
            self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 1, 2)
            time.sleep(80)
            # self.move_click(self.queding_coordinate[0], self.queding_coordinate[1], 1, 2)
            # time.sleep(8)
            self.typing(message)
            time.sleep(30)
            self.move_click(self.zuoji_coordinate[0], self.zuoji_coordinate[1], 1, 2)
            time.sleep(1)
            self.move_click(self.zhenshou_coordinate[0], self.zhenshou_coordinate[1], 1, 2)
            time.sleep(1)
            self.move_click(self.xunlian_coordinate[0], self.xunlian_coordinate[1], 1, 2)
            time.sleep(0.5)
            self.move_click(self.xunlian_coordinate[0], self.xunlian_coordinate[1], 1, 2)
            time.sleep(0.5)
            self.move_click(self.xunlian_coordinate[0], self.xunlian_coordinate[1], 1, 2)
            time.sleep(0.5)
            self.move_click(self.xunlian_coordinate[0], self.xunlian_coordinate[1], 1, 2)
            time.sleep(1)
            self.move_click(self.chuzhan_coordinate[0], self.chuzhan_coordinate[1], 1, 2)
            time.sleep(1)
            self.move_click(self.guanbi_coordinate[0], self.guanbi_coordinate[1], 1, 2)
            time.sleep(1)
            self.move_click(self.zidong_coordinate[0], self.zidong_coordinate[1], 1, 2)
        else:
            time.sleep(60)

if __name__ == '__main__':
    wdname = u'《新天龙八部》 0.02.3605 (怀旧一区:仙侣情缘)'
    # wdname = u'桌面控制 教研室'

    img = Image.open('C:/Users/29557/Desktop/微信截图_20210926034129.png')
    demo = GameAssist(wdname, img)

    while(1):
        demo.start()

