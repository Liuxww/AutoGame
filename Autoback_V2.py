# -*- coding:utf-8 -*-
from pymouse import PyMouse
from pykeyboard import *
import win32gui
from PIL import ImageGrab, Image
import numpy as np
import time
import random
from pydamo_0 import Time, DM, Mouse
import pyautogui


class GameAssist:
    def __init__(self, wdname):
        # 取得窗口句柄
        self.hwnd = win32gui.FindWindow(0, wdname)
        if not self.hwnd:
            print('窗口找不到，请确认窗口句柄名称：【%s】' % wdname)
        self.setforward()

        # PyMouse对象，鼠标点击
        self.mouse = PyMouse()
        self.k = PyKeyboard()
        self.dm = DM()  # 可指定dm.dll路径DM(path), 若无法使用某些函数dm.f(), 则使用dm.dm.f()来调用.
        self.ms = Mouse(self.dm)

        # 坐标
        self.update()
        self.ditu = 'KLS'
        self.guaji_zuobiao = [0, 0]
        self.scree_left_and_right_point = (self.main[0]+361, self.main[1]+183, self.main[0]+619, self.main[1]+313)  # 死亡窗口
        self.xl_coordinate = [self.main[0]+978, self.main[1]+241]  # 自动寻路
        self.zb1_coordinate = [self.main[0]+928, self.main[1]+495]  # 输入坐标
        self.zb2_coordinate = [self.main[0]+960, self.main[1]+495]  # 输入坐标
        self.yd_coordinate = [self.main[0]+1000, self.main[1]+495]  # 移动按钮
        self.difu_coordinate = [self.main[0]+592, self.main[1]+280]  # 出窍
        self.mengpo_coordinate = [self.main[0]+935, self.main[1]+327]  # 孟婆 1
        self.loulan_coordinate = [self.main[0]+70, self.main[1]+337]  # 楼兰
        self.luoyang_coordinate = [self.main[0]+70, self.main[1]+264]  # 洛阳
        self.suzhou_coordinate = [self.main[0]+70, self.main[1]+288]  # 苏州
        self.dali_coordinate = [self.main[0]+70, self.main[1]+314]  # 大理
        self.gaochang_coordinate = [self.main[0]+930, self.main[1]+398]  # 高昌 5
        self.dawan_coordinate = [self.main[0]+930, self.main[1]+385]  # 大宛 4
        self.talimu_coordinate = [self.main[0]+930, self.main[1]+418]  # 塔里木 6
        self.take_coordinate = [self.main[0]+930, self.main[1]+366]  # 塔克 3
        self.migong_coordinate = [self.main[0]+930, self.main[1]+349]  # 迷宫/撒马/昆仑山 2
        self.queding_coordinate = [self.main[0]+575, self.main[1]+418]  # 无杀气场景确定按钮
        self.xunlian_coordinate = [self.main[0]+193, self.main[1]+456]  # 驯养珍兽
        self.zidong_coordinate = [self.main[0]+1010, self.main[1]+156]  # 自动打怪
        self.qwy_coordinate = [self.main[0]+620, self.main[1]+430]  # 钱为一
        self.bag_coordinate = [self.main[0]+778, self.main[1]+330]  # 背包

    def update(self):
        self.main = win32gui.GetWindowRect(self.hwnd)
        time.sleep(.5)
        self.k.tap_key(self.k.tab_key)
        time.sleep(.5)
        self.k.tap_key(self.k.tab_key)
        print("完成坐标更新")

    def setforward(self):
        # 窗口显示最前面
        win32gui.SetForegroundWindow(self.hwnd)

    def init_autoback(self, img, check_time=60):
        # 死亡检测
        self.standard = np.array(img.convert('L')).flatten()
        self.check_time = check_time

    # 截取死亡弹窗
    def screenshot(self):
        image = ImageGrab.grab(self.scree_left_and_right_point)

        return image

    # 死亡检测
    def contrast(self, image):
        keep, k_mse = 0, 90
        image = np.array(image.convert('L')).flatten()
        mse = (((image - self.standard) ** 2) / len(self.standard)).sum()
        if mse < k_mse:
            keep = 1
        return keep

    # 自动训练输入坐标移动
    def typing(self, message):
        self.move_click(self.zb1_coordinate[0], self.zb1_coordinate[1], 3)
        self.k.type_string(message[0])
        time.sleep(0.5)
        self.move_click(int(self.main[2]/2), int(self.main[3]/2), 0)
        time.sleep(0.5)
        self.move_click(self.zb2_coordinate[0], self.zb2_coordinate[1], 3)
        self.k.type_string(message[1])
        time.sleep(0.5)

    # 召唤宝宝
    def summons(self):
        self.k.press_key(self.k.alt_key)
        time.sleep(0.5)
        self.k.tap_key('x')
        time.sleep(0.5)
        self.k.release_key(self.k.alt_key)
        print('召唤-宝宝')
        self.move_click(self.xunlian_coordinate[0], self.xunlian_coordinate[1], 4)
        self.k.press_key(self.k.alt_key)
        time.sleep(0.5)
        self.k.tap_key('x')
        time.sleep(0.5)
        self.k.release_key(self.k.alt_key)
        self.k.tap_key(self.k.function_keys[9])
        time.sleep(5)

    # 鼠标移动
    def move_click(self, target_x, target_y, n):
        xs, ys, i = 0, 0, 0

        x, y = self.mouse.position()
        # 当前鼠标在目标位置右下
        if target_x > x and target_y > y:
            for xs in range(target_x - x):
                self.mouse.move(x + xs + random.randint(0, 3), y + random.randint(0, 3))
                if random.random() <= 0.1:
                    time.sleep(random.randint(1, 10) * 0.001)
            for ys in range(target_y - y):
                self.mouse.move(x + xs + random.randint(0, 3), y + ys + random.randint(0, 3))
                if random.random() <= 0.1:
                    time.sleep(random.randint(1, 10) * 0.001)
        # 当前鼠标在目标位置右上
        elif target_x > x and target_y < y:
            for xs in range(target_x - x):
                self.mouse.move(x + xs + random.randint(0, 3), y + random.randint(0, 3))
                if random.random() <= 0.1:
                    time.sleep(random.randint(1, 10) * 0.001)
            for ys in range(y - target_y):
                self.mouse.move(x + xs + random.randint(0, 3), y - ys + random.randint(0, 3))
                if random.random() <= 0.1:
                    time.sleep(random.randint(1, 10) * 0.001)
        # 当前鼠标在目标位置左下
        elif target_x < x and target_y > y:
            for xs in range(x - target_x):
                self.mouse.move(x - xs + random.randint(0, 3), y + random.randint(0, 3))
                if random.random() <= 0.1:
                    time.sleep(random.randint(1, 10) * 0.001)
            for ys in range(target_y - y):
                self.mouse.move(x - xs + random.randint(0, 3), y + ys + random.randint(0, 3))
                if random.random() <= 0.1:
                    time.sleep(random.randint(1, 10) * 0.001)
        # 当前鼠标在目标位置左上
        else:
            for xs in range(x - target_x):
                self.mouse.move(x - xs + random.randint(0, 3), y + random.randint(0, 3))
                if random.random() <= 0.1:
                    time.sleep(random.randint(1, 10) * 0.001)
            for ys in range(y - target_y):
                self.mouse.move(x - xs + random.randint(0, 3), y - ys + random.randint(0, 3))
                if random.random() <= 0.1:
                    time.sleep(random.randint(1, 10) * 0.001)
        for i in range(n):
            time.sleep(0.5)
            self.ms.click_left(target_x, target_y, 0.1)


    # 自动回点
    def autoback(self, nn, die):
        message = [str(random.randint(self.guaji_zuobiao[0] - 2, self.guaji_zuobiao[0] + 2)),
                   str(random.randint(self.guaji_zuobiao[1] - 2, self.guaji_zuobiao[1] + 2))]  # 挂机坐标
        # 1. 检测死亡
        print("检测死亡")
        image = self.screenshot()
        keep = self.contrast(image)
        if keep == 1:
            nn = 0
            die += 1
            print('我被打死了！')
            # 2.出窍地府
            self.move_click(self.difu_coordinate[0], self.difu_coordinate[1], 5)
            print('出窍')
            time.sleep(random.randint(5, 8))
            self.move_click(960, 400, random.randint(2, 4))
            self.move_click(self.xl_coordinate[0], self.xl_coordinate[1], 1)
            self.move_click(self.mengpo_coordinate[0], self.mengpo_coordinate[1], 3)
            self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 3)
            print('移动-孟婆')
            time.sleep(random.randint(8, 10))
            self.move_click(self.loulan_coordinate[0], self.loulan_coordinate[1], 3)
            print('地府-楼兰')
            time.sleep(random.randint(8, 10))
            # 5.召唤BB
            self.k.tap_key(self.k.function_keys[11])
            self.k.tap_key(self.k.function_keys[12])
            self.summons()
            # 3.主城
            self.k.tap_key(self.k.function_keys[10])
            time.sleep(5)
            self.k.tap_key(self.k.tab_key)
            if self.ditu == 'MG':
                self.move_click(self.gaochang_coordinate[0], self.gaochang_coordinate[1], 3)
                self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 2)
                self.k.tap_key(self.k.tab_key)
                print('楼兰-高昌')
                time.sleep(random.randint(8, 10))
            elif self.ditu == 'DW':
                self.move_click(self.dawan_coordinate[0], self.dawan_coordinate[1], 2)
                self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 2)
                self.k.tap_key(self.k.tab_key)
                print('楼兰-大宛')
                time.sleep(random.randint(58, 60))
            elif self.ditu == 'TK' or self.ditu == 'KLS':
                self.move_click(self.talimu_coordinate[0], self.talimu_coordinate[1], 2)
                self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 2)
                self.k.tap_key(self.k.tab_key)
                print('楼兰-塔里木')
                time.sleep(random.randint(58, 60))

            # 4.野外
            if self.ditu == 'MG':
                self.k.tap_key(self.k.tab_key)
                self.move_click(self.migong_coordinate[0], self.migong_coordinate[1], 3)
                self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 3)
                self.k.tap_key(self.k.tab_key)
                print('高昌-迷宫')
                time.sleep(random.randint(25, 30))
                self.move_click(self.queding_coordinate[0], self.queding_coordinate[1], 3)
                time.sleep(8)
                self.k.tap_key(self.k.tab_key)
                self.typing(message)
                time.sleep(.5)
                self.move_click(int(self.main[2] / 2), int(self.main[3] / 2), 0)
                time.sleep(.5)
                self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 3)
                self.k.tap_key(self.k.tab_key)
                print('迷宫-挂机点')
                time.sleep(random.randint(38, 40))
                self.k.tap_key(self.k.function_keys[10])
            elif self.ditu == 'KLS':
                self.k.tap_key(self.k.tab_key)
                self.move_click(self.migong_coordinate[0], self.migong_coordinate[1], 3)
                self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 3)
                self.k.tap_key(self.k.tab_key)
                print('塔里木-昆仑山')
                time.sleep(random.randint(75, 80))
                self.k.tap_key(self.k.tab_key)
                self.typing(message)
                time.sleep(.5)
                self.move_click(int(self.main[2] / 2), int(self.main[3] / 2), 0)
                time.sleep(.5)
                self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 3)
                self.k.tap_key(self.k.tab_key)
                print('昆仑山-挂机点')
                time.sleep(random.randint(38, 40))
                self.k.tap_key(self.k.function_keys[10])
            elif self.ditu == 'TK':
                self.k.tap_key(self.k.tab_key)
                self.move_click(self.take_coordinate[0], self.take_coordinate[1], 3)
                self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 3)
                self.k.tap_key(self.k.tab_key)
                print('塔里木-塔克拉玛干')
                time.sleep(random.randint(55, 60))
                self.move_click(self.queding_coordinate[0], self.queding_coordinate[1], 3)
                time.sleep(8)
                self.k.tap_key(self.k.tab_key)
                self.typing(message)
                time.sleep(.5)
                self.move_click(int(self.main[2] / 2), int(self.main[3] / 2), 0)
                time.sleep(.5)
                self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 3)
                self.k.tap_key(self.k.tab_key)
                print('塔克拉玛干-挂机点')
                time.sleep(random.randint(8, 10))
                self.k.tap_key(self.k.function_keys[10])
            elif self.ditu == 'DW':
                self.k.tap_key(self.k.tab_key)
                self.typing(message)
                time.sleep(.5)
                self.move_click(int(self.main[2] / 2), int(self.main[3] / 2), 0)
                time.sleep(.5)
                self.move_click(self.yd_coordinate[0], self.yd_coordinate[1], 3)
                self.k.tap_key(self.k.tab_key)
                print('大宛-挂机点')
                time.sleep(random.randint(38, 40))
                self.k.tap_key(self.k.function_keys[10])

            # 6.自动打怪
            self.move_click(self.zidong_coordinate[0], self.zidong_coordinate[1], 1)
            print('我又好起来了！')
            time.sleep(.5)
            return nn, die
        else:
            print('我还没死，存活{0}秒!，死亡{1}次。'.format(nn*self.check_time, die))
            time.sleep(self.check_time)
            nn += 1
            return nn, die

    # 自动跑商
    def run(self, num=0, nn=1):
        # 1. 开始
        message = ['147', '56']
        row = 0
        self.move_click(self.qwy_coordinate[0], self.qwy_coordinate[1], 1, 3)
        if num == 0:
            lqyp_coordinate = list(pyautogui.locateCenterOnScreen('./lqyp.png'))
            self.move_click(lqyp_coordinate[0], lqyp_coordinate[1], 1, 3)
            print('开始第' + str(nn) + '次跑商...')
            print('领取银票...')
            row = 1
        if num == 2:
            row = 2
        if num == 4:
            print('全部卖出交付银票...')
            self.srdp_coordinate = list(pyautogui.locateCenterOnScreen('./srdp.png'))
            self.move_click(self.srdp_coordinate[0], self.srdp_coordinate[1], 1, 3)
            self.cl_coordinate = list(pyautogui.locateCenterOnScreen('./cl.png'))
            self.move_click(self.cl_coordinate[0], self.cl_coordinate[1], 1, 3)
            for i in range(5):
                for j in range(7):
                    target_x, target_y = self.bag_coordinate[0] + j * self.size + 5, self.bag_coordinate[
                        1] + i * self.size + 4
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

    def autoattack(self, attack, select):
        self.k.tap_key(self.k.function_keys[select])
        time.sleep(.5)
        self.k.tap_key(self.k.function_keys[attack])
        time.sleep(.5)

def main():
    print("当前游戏版本号")
    # wdname = u'《新天龙八部》 0.03.1607 (怀旧一区:仙侣情缘)'
    number = input()
    wdname = '《新天龙八部》 '+number+' (怀旧一区:仙侣情缘)'
    Master = GameAssist(wdname)
    print("选择功能:1.自动回点 2.自动跑商(升级中，勿选) 3.自动打怪")
    flag = int(input())
    if flag == 1:
        print("Autoback 2.0\n"
              "注意:\n"
              "1.确保显示模型数最低\n"
              "2.每次打开游戏窗口请将分辨率设置为1024*768\n"
              "完成以上操作后进入配置阶段:")
        img = Image.open('die.png')
        Master.init_autoback(img)
        print("当前游戏窗口左上角位置:{},{}".format(Master.main[0], Master.main[1]))
        print("选择挂机地图,输入大写首字母:KLS(昆仑山), MG(迷宫), DW(大宛), TK(塔克)")
        Master.ditu = input()
        print("输入挂机坐标,用空格分开,示例:20 20")
        Master.guaji_zuobiao = list(map(int, input().strip().split(' ')))
        print("输入死亡检测间隔,单位(秒),默认值60")
        t = input()
        if t != '':
            Master.check_time = int(t)
        print("点击一下游戏窗口内部,核对注意事项,5秒后启动")
        for i in range(5, 0, -1):
            print(i, '\n')
            time.sleep(1)
        nn, die = 0, 0
        while True:
            if win32gui.GetWindowRect(Master.hwnd) != Master.main:
                print("检测到窗口移动,正在更新新的坐标...")
                Master.update()
            nn, die = Master.autoback(nn, die)
    elif flag == 2:
        num = 0
        nn = 1
        for _ in range(16):
            num, nn = Master.run(num, nn)
    elif flag == 3:
        print("选择攻击键,实例：F1攻击,输入1")
        attack = int(input())
        print("选择攻击键,实例：F11选怪,输入11")
        select = int(input())
        Master.setforward()
        while True:
            Master.autoattack(attack, select)


if __name__ == '__main__':
    main()
