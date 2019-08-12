
# -*- coding:utf-8 -*-
import time, os
import traceback
import rpa
import json
from rpa import Chrome
import time
import random
import re
from PIL import Image
from PIL import ImageGrab
from selenium import webdriver
from selenium.webdriver import ActionChains
# from track_img import *
import math
import Queue


class Chrome_init(object):
    '''
    set_argu:   设置初始化的启动项
    create_chrome:  生成chrome对象
    '''

    def __init__(self):
        self.option = rpa.ChromeOptions()

    def set_argu(self):
        self.option.add_argument('disable-infobars')
        return self

    def create_chrome(self):
        return Chrome(self.option)


def simulation_drag(browser, element_name, distance):
    distance = int(distance)


    # 一般1 到2 s 完成拼图  18毫秒监控一次，也就是会记录几十个坐标点     就是说前1/4 时间完成大半拼图 8～9/10距离，最后3/4 或者 4/5时间修正位置1/10
    a_list = [0,0,2,5,10,8,4,2,1]
    while True:
        for x in a_list:
            browser.click_and_hold(element_name, x)


    browser.release()

def simulation_drag1(browser, element_name, distance):
    distance = int(distance)
    # chrome浏览器的监听鼠标的间隔为18ms ，那么时间间隔要先加速再减速

    dt = random.randint(1,18)
    dt_queue = []
    # dt_queue = Queue.Queue()

    # 函数曲线1  ln(5x**2+1)+3ln(10x)   3 那个参数 可以根据移动的总距离除以10 实现
    # ln(5x ** 2 + 1)+3ln(10x)

    # y = math.log(5x ** 2 + 1) + 3math.log(10x)
    for i in xrange(100):
        want_dt = float(dt)/100
        dt_queue.append(want_dt)

    dt_sort_queue = sorted(dt_queue)

    # 拖拽举例
    total_s = 0

    while True:
        time.sleep(dt)
        browser.click_and_hold(element_name, ds)
        if total_s >= distance:
            break

    # 释放鼠标
    browser.release()



class hander_one_pdf(object):
    '''
    set_element_map: 生成查找元素的索引
    execute_flow: 写执行逻辑
    '''
    result_dic = {}

    def __init__(self):
        self.chrome = Chrome_init().set_argu().create_chrome()

    def set_element_map(self):
        self.chrome.add_element('点击登陆', id='', css='',
                                xpath='//*[@id="web-content"]/div/div[1]/div[1]/div/div/div[2]/div/div[4]/a')
        self.chrome.add_element('选择密码登陆', id='', css='', xpath='//div[@class="title-tab text-center"]/div[last()]')
        self.chrome.add_element('usr_name', id='', css='',
                                xpath='//div[@class="module module1 module2 loginmodule collapse in"]/div[2]/div[2]/input')
        self.chrome.add_element('password', id='', css='', xpath='//div[@class="input-warp -block"]/input[1]')
        self.chrome.add_element('开始登陆', id='', css='',
                                xpath='//div[@class="modulein modulein1 mobile_box  f-base collapse in"]/div[5]')

        self.chrome.add_element('拖拽元素', id='', css='', xpath='/html/body/div[10]/div[2]/div[2]/div[2]/div[2]')

        # 截取第一张图
        self.chrome.add_element('原始图片', id='', css='', xpath='//div[@class="gt_cut_fullbg gt_show"]')

        # 将小图片的style重制为""，截取有缺口的图片
        self.chrome.add_element('那个可以移动的小图片', id='', css='', xpath='//div[@class="gt_slice gt_show"]')
        self.chrome.add_element('登陆成功的元素', id='', css='', xpath='//div/a/span[contains(text(),"吕雉")]')

        self.chrome.add_element('输入企业名称', id='', css='', xpath='//*[@id="home-main-search"]')
        self.chrome.add_element('天眼一下', id='', css='',
                                xpath='//*[@id="web-content"]/div/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div')
        self.chrome.add_element('公司页面,天眼一下', id='', css='', xpath='/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div')
        # self.chrome.add_element('判断公司名称',id='',css='',xpath ='/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div')
        self.chrome.add_element('进入公司详情页', id='', css='',
                                xpath='//*[@id="web-content"]/div/div[1]/div[4]/div[2]/div[1]/div/div[3]/div[1]/a')
        # 企业简介表
        self.chrome.add_element('企业简介表', id='', css='#nav-main-stockNum >div:nth-child(2) > table', xpath='')
        # 联系信息表  注册地址
        self.chrome.add_element('联系地址表', id='', css='#nav-main-corpContactInfoCount > div >table', xpath='')
        # 重要人员表 获取法人代表
        self.chrome.add_element('重要人员表', id='', css='#nav-main-corpBasicInfoCount >div:nth-child(2) > table', xpath='')
        # 资质证书表
        # '企业资质'
        self.chrome.add_element('资质证书表', id='', css='#nav-main-certificateCount ~ div > table', xpath='')

    def execute_flow(self):
        targetdict = {u'企业名称': u'', u'法人': u'', u'注册地址': u'', u'企业资质':
            []}

        browser = self.chrome.create('https://www.tianyancha.com/')

        browser.wait_page_loaded(20)
        browser.click('点击登陆')
        browser.click('选择密码登陆')

        browser.input('usr_name', '18602146859')
        browser.input('password', 'Abc12345')
        time.sleep(5)

        browser.mouse_move_in('开始登陆')
        time.sleep(5)
        browser.mouse_click()
        # browser.click('开始登陆')
        time.sleep(0.5)
        row_save_path = 'test/破解滑动验证码/row.png'

        browser.wait_element_loaded('原始图片', timeout=5)
        # 整个屏幕的原始图片
        browser.element_screen_shot('原始图片', row_save_path)

        browser.click('拖拽元素')
        change_save_path = 'test/破解滑动验证码/change.png'

        img_style = browser.attr('那个可以移动的小图片', 'style')

        browser.set_attr('那个可以移动的小图片', 'style', '')

        time.sleep(2)
        browser.element_screen_shot('原始图片', change_save_path)
        browser.set_attr('那个可以移动的小图片', 'style', img_style)

        image1 = Image.open(row_save_path).resize((260, 116))
        image2 = Image.open(change_save_path).resize((260, 116))

        # 步骤五：对比两张图片的所有RBG像素点，得到不一样像素点的x值，即要移动的距离   还要减去小图片的x  59
        distance = get_distance(image1, image2) - 8
        simulation_drag(browser, "拖拽元素", distance)

        time.sleep(100000)

    def quit(self):
        '''
        安全退出chrome
        :return:
        '''
        self.chrome.quit()


# if __name__ == '__main__':
#     try:
#         hander = hander_one_pdf()
#         hander.set_element_map()
#         targetdict = hander.execute_flow()
#         # # 准备附件3原对比数据
#         # sourcedict = {}
#         #
#         # sourcedict[u'企业名称'] = get_excel_cell('../附件3：模拟项目企业资质.xls', 'Sheet1', 0, u'企业名称')
#         # sourcedict[u'法人'] = get_excel_cell('../附件3：模拟项目企业资质.xls', 'Sheet1', 0, u'法人')
#         # sourcedict[u'注册地址'] = get_excel_cell('../附件3：模拟项目企业资质.xls', 'Sheet1', 0, u'注册地址')
#         # sourcedict[u'企业资质'] = []
#         #
#         # zizhi = {}
#         # zizhi[u'证书类型'] = get_excel_cell('../附件3：模拟项目企业资质.xls', 'Sheet1', 0, u'证书类型')
#         # zizhi[u'证书名称'] = get_excel_cell('../附件3：模拟项目企业资质.xls', 'Sheet1', 0, u'证书名称')
#         # zizhi[u'证书编号'] = get_excel_cell('../附件3：模拟项目企业资质.xls', 'Sheet1', 0, u'证书编号')
#         # zizhi[u'发证日期'] = str(get_excel_cell('../附件3：模拟项目企业资质.xls', 'Sheet1', 0, u'发证日期').to_pydatetime().date())
#         # zizhi[u'截止日期'] = str(get_excel_cell('../附件3：模拟项目企业资质.xls', 'Sheet1', 0, u'截止日期').to_pydatetime().date())
#         #
#         # sourcedict[u'企业资质'].append(zizhi)
#
#         # 准备从天眼查查来目标对比的数据
#         # targetdict = {u'企业名称': u'达观', u'法人': u'陈运文', u'注册地址': u'', u'企业资质':
#         #     [{u'证书类型': u'', u'证书名称': u'', u'证书编号': u'', u'发证日期': u'', u'截止日期': u''},
#         #      {u'证书类型': u'', u'证书名称': u'', u'证书编号': u'', u'发证日期': u'', u'截止日期': u''}]}
#
#         # checkresult = check(sourcedict, targetdict)
#
#         # print json.dumps(checkresult, ensure_ascii=False)
#     except Exception as e:
#         print traceback.format_exc()
#         print "get Exception:", e
#     finally:
#         hander.quit()


if __name__ == '__main__':
    print float(random.randint(1,18))/100