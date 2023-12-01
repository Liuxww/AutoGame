# -*- coding:utf-8 -*-
from pymouse import PyMouse
from pykeyboard import *
import win32gui
from PIL import ImageGrab, Image
import numpy as np
import operator
import time
import random
import pyautogui

m = PyMouse()
k = PyKeyboard()

class GameAssist:
    def __init__(self, wdname, img):
        # 购买物品标准图片 32*32
        self.standard = np.array(img.convert('L')).flatten()

        # 取得窗口句柄
        self.wdname = wdname
        self.hwnd = win32gui.FindWindow(0, wdname)
        if not self.hwnd:
            print('窗口找不到，请确认窗口句柄名称：【%s】' % wdname)

        # 窗口显示最前面
        win32gui.SetForegroundWindow(self.hwnd)

        # 主截图的左上角坐标和右下角坐标
        self.main = (447, 147)
        self.scree_left_and_right_point = (self.main[0]+353, self.main[1]+136, self.main[0]+674, self.main[1]+362)

        # 坐标
        self.shop_coordinate = [(self.scree_left_and_right_point[0]+16, self.scree_left_and_right_point[1]+16),
                                (self.scree_left_and_right_point[0]+16, self.scree_left_and_right_point[1]+54),
                                (self.scree_left_and_right_point[0]+16, self.scree_left_and_right_point[1]+92),
                                (self.scree_left_and_right_point[0]+16, self.scree_left_and_right_point[1]+130),
                                (self.scree_left_and_right_point[0]+16, self.scree_left_and_right_point[1]+168),
                                (self.scree_left_and_right_point[0]+16, self.scree_left_and_right_point[1]+206),
                                (self.scree_left_and_right_point[0]+181, self.scree_left_and_right_point[1]+16),
                                (self.scree_left_and_right_point[0]+181, self.scree_left_and_right_point[1]+54),
                                (self.scree_left_and_right_point[0]+181, self.scree_left_and_right_point[1]+92),
                                (self.scree_left_and_right_point[0]+181, self.scree_left_and_right_point[1]+130),
                                (self.scree_left_and_right_point[0]+181, self.scree_left_and_right_point[1]+168),
                                (self.scree_left_and_right_point[0]+181, self.scree_left_and_right_point[1]+206),
                                ]
        self.bag_coordinate = [self.main[0]+778, self.main[1]+298]
        self.xl_coordinate = [self.main[0]+978, self.main[1]+215]  # 自动寻路
        self.zb1_coordinate = [self.main[0]+928, self.main[1]+465]  # 输入坐标
        self.zb2_coordinate = [self.main[0]+960, self.main[1]+465]  # 输入坐标
        self.yd_coordinate = [self.main[0]+1000, self.main[1]+468]
        self.qwy_coordinate = [self.main[0]+620, self.main[1]+400]
        self.srdp_coordinate = [self.main[0]+80, self.main[1]+375, self.main[0]+80, self.main[1]+200]
        self.cl_coordinate = [self.main[0]+825, self.main[1]+270]
        self.cm_coordinate = [self.main[0]+449, self.main[1]+579]
        self.mlz_coordinate = [self.main[0]+766, self.main[1]+260]
        self.yi_coordinate = [self.main[0]+930, self.main[1]+303]
        self.san_coordinate = [self.main[0]+930, self.main[1]+338]
        self.lq_coordinate = [self.main[0]+933, self.main[1]+304]
        self.zx_coordinate = [self.main[0]+933, self.main[1]+388]
        self.cyl_coordinate = [self.main[0]+80, self.main[1]+212]
        self.qy_coordinate = [self.main[0]+933, self.main[1]+336]
        self.ml_coordinate = [self.main[0]+933, self.main[1]+319]
        self.db_coordinate = [self.main[0]+933, self.main[1]+355]
        self.qsmy_coordinate = [self.main[0]+80, self.main[1]+213]
        self.lqyp_coordinate = [self.main[0]+80, self.main[1]+220]
        self.jh_coordinate = [self.main[0]+80, self.main[1]+237]
        self.sbzj_coordinate = [1552, 170]
        self.sbyj_coordinate = [self.sbzj_coordinate[0]+152, self.sbzj_coordinate[1]]

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
        image_list = {
            'shop': {}
        }

        offset_h = self.high
        offset_w = self.wide
        x = 0
        for a in range(2):
            y = 0
            for i in range(6):
                top = y
                left = x
                right = x + self.size
                bottom = y + self.size

                # 用crop函数切割成小图标，参数为图标的左上角和右下角左边
                im = image.crop((left, top, right, bottom))
                # 将切割好的图标存入对应的位置
                image_list['shop'][i+a*6] = im
                y += offset_h
            x += offset_w

        return image_list

    def contrast(self, image_list):
        image = []
        keep, k_mse = 0, 100
        for i in range(len(image_list['shop'])):
            image.append(np.array(image_list['shop'][i].convert('L')).flatten())
        for i in range(len(image)):
            mse = (((image[i] - self.standard) ** 2) / len(self.standard)).sum()
            if mse < k_mse:
                keep = i
                k_mse = mse
        return keep

    def typing(self, message):
        k.tap_key(k.tab_key)
        time.sleep(0.5)
        self.move_click(self.zb1_coordinate[0], self.zb1_coordinate[1], 1, 2)
        k.type_string(message[0])
        time.sleep(0.5)
        self.move_click(960, 400, 1, 0)
        self.move_click(self.zb2_coordinate[0], self.zb2_coordinate[1], 1, 2)
        k.type_string(message[1])
        time.sleep(0.5)
        self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 1, 5)
        time.sleep(0.5)
        k.tap_key(k.tab_key)

    def move_click(self, target_x, target_y, button, n):
        xs, ys, i = 0, 0, 0
        k = PyKeyboard()
        x, y = m.position()
        if button == 1 and self.flag != 1:
            for xs in range(self.sbzj_coordinate[0] - x):
                m.move(x + xs + random.randint(0, 3), y + random.randint(0, 3))
                if random.random() <= 0.1:
                    time.sleep(random.randint(1, 10) * 0.001)
            for ys in range(y-self.sbzj_coordinate[1]):
                m.move(x + xs + random.randint(0, 3), y - ys + random.randint(0, 3))
                if random.random() <= 0.1:
                    time.sleep(random.randint(1, 10) * 0.001)
            time.sleep(0.5)
            m.click(self.sbzj_coordinate[0], self.sbzj_coordinate[1], button=1, n=2)
            time.sleep(0.5)
            self.flag = 1
            win32gui.SetForegroundWindow(self.hwnd)
            time.sleep(0.5)
        if button == 2 and self.flag != 2:
            for xs in range(self.sbyj_coordinate[0]-x):
                m.move(x + xs + random.randint(0, 3), y + random.randint(0, 3))
                if random.random() <= 0.1:
                    time.sleep(random.randint(1, 10) * 0.001)
            for ys in range(y-self.sbyj_coordinate[1]):
                m.move(x + xs + random.randint(0, 3), y - ys + random.randint(0, 3))
                if random.random() <= 0.1:
                    time.sleep(random.randint(1, 10) * 0.001)
            time.sleep(0.5)
            m.click(self.sbyj_coordinate[0], self.sbyj_coordinate[1], button=1, n=2)
            time.sleep(0.5)
            self.flag = 2
            win32gui.SetForegroundWindow(self.hwnd)
            time.sleep(0.5)
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
        for i in range(n):
            time.sleep(0.5)
            k.tap_key(k.function_keys[8])
            time.sleep(0.5)
            k.tap_key(k.function_keys[8])

    # 程序入口、控制中心
    def start(self, num=0, nn=1):
        # 1. 开始
        message = ['147', '56']
        row = 0
        self.move_click(self.qwy_coordinate[0], self.qwy_coordinate[1], 1, 3)
        if num == 0:
            self.move_click(self.lqyp_coordinate[0], self.lqyp_coordinate[1], 1, 3)
            print('开始第' + str(nn) + '次跑商...')
            print('领取银票...')
            row = 1
        if num == 2:
            row = 2
        if num == 4:
            print('全部卖出交付银票...')
            self.move_click(self.srdp_coordinate[0], self.srdp_coordinate[1], 1, 3)
            self.move_click(self.cl_coordinate[0], self.cl_coordinate[1], 1, 3)
            for i in range(5):
                for j in range(7):
                    target_x, target_y = self.bag_coordinate[0]+j*self.size+5, self.bag_coordinate[1]+i*self.size+4
                    self.move_click(target_x, target_y, 2, 2)
                    self.move_click(960, 400, 2, 0)
            self.move_click(self.jh_coordinate[0], self.jh_coordinate[1], 1, 3)
            print('完成跑商' + str(nn) + '次')
            k.tap_key(k.escape_key)
            time.sleep(random.randint(5, 10) / 10)
            nn += 1
            num = 0
            return num, nn
        self.move_click(self.srdp_coordinate[0], self.srdp_coordinate[1], 1, 3)
        self.move_click(self.cl_coordinate[0], self.cl_coordinate[1], 1, 3)
        print('卖出材料...')
        for i in range(row):
            if num != 0:
                for j in range(7):
                    target_x, target_y = self.bag_coordinate[0] + j * self.size + 5, self.bag_coordinate[
                        1] + i * self.size + 4
                    self.move_click(target_x, target_y, 2, 2)
                    self.move_click(960, 400, 2, 0)
                self.move_click(self.srdp_coordinate[0], self.srdp_coordinate[1], 1, 3)
                time.sleep(random.randint(5, 10) / 10)
            # 2.先截取游戏区域大图，然后分切每个小图
            image_list = self.screenshot()
            keep = self.contrast(image_list)

            # 3. 获取目标物品位置， 买卖
            target_x, target_y = self.shop_coordinate[keep]
            print('买入材料...')
            self.move_click(target_x, target_y, 1, 7)
        if num != 0:
            self.move_click(self.srdp_coordinate[0], self.srdp_coordinate[1], 1, 3)
            time.sleep(random.randint(5, 10) / 10)
            # 2.先截取游戏区域大图，然后分切每个小图
            image_list = self.screenshot()
            keep = self.contrast(image_list)

            # 3. 获取目标物品位置， 买卖
            target_x, target_y = self.shop_coordinate[keep]
            print('买入材料...')
            self.move_click(target_x, target_y, 1, 12)
        num += 1

        k.tap_key(k.tab_key)
        self.move_click(self.cm_coordinate[0], self.cm_coordinate[1], 1, 3)
        print('向城门移动...')
        k.tap_key(k.tab_key)
        time.sleep(random.randint(40, 45))
        k.tap_key(k.tab_key)
        time.sleep(random.randint(5, 10) / 10)
        self.move_click(self.yi_coordinate[0], self.yi_coordinate[1], 1, 3)
        self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 1, 5)
        time.sleep(random.randint(5, 10) / 10)
        self.move_click(self.san_coordinate[0], self.san_coordinate[1], 1, 3)
        self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 1, 5)
        k.tap_key(k.tab_key)
        print('向清源移动...')
        time.sleep(random.randint(20, 25))
        k.tap_key(k.tab_key)
        time.sleep(random.randint(5, 10) / 10)
        self.move_click(self.lq_coordinate[0], self.lq_coordinate[1], 1, 3)
        self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 1, 5)
        k.tap_key(k.tab_key)
        print('向龙泉移动...')
        time.sleep(random.randint(92, 95))
        k.tap_key(k.tab_key)
        time.sleep(random.randint(5, 10) / 10)
        self.move_click(self.zx_coordinate[0], self.zx_coordinate[1], 1, 3)
        self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 1, 5)
        k.tap_key(k.tab_key)
        print('向龙泉正西移动...')
        time.sleep(random.randint(65, 70))
        self.move_click(self.cyl_coordinate[0], self.cyl_coordinate[1], 1, 3)
        print('传送苍云岭...')
        time.sleep(random.randint(8, 10))

        self.typing(message)
        print('向钱为一移动...')
        time.sleep(random.randint(35, 40))
        self.move_click(self.qwy_coordinate[0], self.qwy_coordinate[1], 1, 3)
        if num == 1:
            row = 1
        if num == 3:
            row = 3
        self.move_click(self.srdp_coordinate[2], self.srdp_coordinate[3], 1, 3)
        self.move_click(self.cl_coordinate[0], self.cl_coordinate[1], 1, 3)
        print('卖出材料...')
        for i in range(row):
            for j in range(7):
                target_x, target_y = self.bag_coordinate[0] + j * self.size + 5, self.bag_coordinate[
                    1] + i * self.size + 4
                self.move_click(target_x, target_y, 2, 2)
                self.move_click(960, 400, 2, 0)
            # 2.先截取游戏区域大图，然后分切每个小图
            self.move_click(self.srdp_coordinate[2], self.srdp_coordinate[3], 1, 3)
            time.sleep(random.randint(5, 10) / 10)
            image_list = self.screenshot()
            keep = self.contrast(image_list)

            # 3. 获取目标物品位置， 买卖
            target_x, target_y = self.shop_coordinate[keep]
            print('买入材料...')
            for _ in range(7):
                self.move_click(target_x, target_y, 1, 1)
        self.move_click(self.srdp_coordinate[2], self.srdp_coordinate[3], 1, 3)
        time.sleep(random.randint(5, 10) / 10)
        image_list = self.screenshot()
        keep = self.contrast(image_list)

        # 3. 获取目标物品位置， 买卖
        target_x, target_y = self.shop_coordinate[keep]
        print('买入材料...')
        self.move_click(target_x, target_y, 1, 12)
        if num == 3:
            self.move_click(target_x, target_y, 1, 7)
        num += 1

        k.tap_key(k.tab_key)
        self.move_click(self.cm_coordinate[0], self.cm_coordinate[1], 1, 3)
        k.tap_key(k.tab_key)
        print('向城门移动...')
        time.sleep(random.randint(40, 45))
        k.tap_key(k.tab_key)
        time.sleep(random.randint(5, 10) / 10)
        self.move_click(self.qy_coordinate[0], self.qy_coordinate[1], 1, 3)
        self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 1, 5)
        k.tap_key(k.tab_key)
        print('向清源移动...')
        time.sleep(random.randint(68, 73))
        k.tap_key(k.tab_key)
        time.sleep(random.randint(5, 10) / 10)
        self.move_click(self.ml_coordinate[0], self.ml_coordinate[1], 1, 3)
        self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 1, 5)
        k.tap_key(k.tab_key)
        print('向梅岭移动...')
        time.sleep(random.randint(90, 95))
        k.tap_key(k.tab_key)
        time.sleep(random.randint(5, 10) / 10)
        self.move_click(self.db_coordinate[0], self.db_coordinate[1], 1, 3)
        self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 1, 3)
        k.tap_key(k.tab_key)
        print('向梅岭东北移动...')
        time.sleep(random.randint(3, 5))
        self.move_click(self.qsmy_coordinate[0], self.qsmy_coordinate[1], 1, 3)
        print('传送秦时明月...')
        time.sleep(random.randint(8, 10))
        self.typing(message)
        print('向钱为一移动...')
        time.sleep(random.randint(35, 40))

        return num, nn


def main():
    wdname = u'《新天龙八部》 0.02.7205 (怀旧一区:仙侣情缘)'
    # wdname = u'桌面控制 教研室'

    img = Image.open('target.png')
    demo = GameAssist(wdname, img)
    num = 0
    nn = 1
    for _ in range(16):
        num, nn = demo.start(num, nn)


if __name__ == '__main__':
    main()
