# coding:utf-8

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image
import time
import random


def is_similar_color(x_pixel, y_pixel):
    for i, pixel in enumerate(x_pixel):
        if abs(y_pixel[i] - pixel) > 50:
            return False
    return True

def get_distance(cut_image, full_image):
    for x in range(cut_image.width):
        for y in range(cut_image.height):
            cpx = cut_image.getpixel((x, y))
            fpx = full_image.getpixel((x, y))
            if not is_similar_color(cpx, fpx):
                img = cut_image.crop((x, y, x + 50, y + 40))
                # 保存一下计算出来位置图片，看看是不是缺口部分
                img.save('test/破解滑动验证码/simli.png')
                return x




if __name__ == '__main__':
    # 可以通过时间控制速度
    #总距离
    distance = 40

    #每次移动距离
    once_distance = random.random(2,5)

    # 移动频率
    times = distance/once_distance

    dt = random.randint(1,18)

    # 时间间隔
    time_gap = float(dt)/100

    # 修正位置







