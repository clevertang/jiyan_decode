# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     selenium_demo
   Description :
   Author :       tangxin
   date：          2017/12/21
-------------------------------------------------
   Change Activity:
                   2017/12/21:
-------------------------------------------------
"""
__author__ = 'tangxin'
# !/usr/bin/env python
# encoding: utf-8
import time
import urllib

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from proxy import get_chrome_proxy_extension

# ip = "111.75.74.193:7777"
# url = "http://www.landchina.com/DesktopModule/BizframeExtendMdl/workList/bulWorkView.aspx?wmguid=20aae8dc-4a0c-4af5-aedf-cc153eb6efdf&recorderguid=9ded915d-5ed7-4454-945d-ef42b07e6a24&sitePath="
chromedriver = "/Applications/Chromium.app/Contents/MacOS/chromedriver"

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',

}
service_args = [
    # '--proxy=119.186.243.151:8888',
    '--proxy-type=http',
    '--load-images=no',
    '--disk-cache=no',
    '--ignore-ssl-errors=true',
    # "--proxy-auth=haizhi:haizhi"
]
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap[
    "phantomjs.page.settings.userAgent"] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
# driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=service_args)
# driver.implicitly_wait(30)
# driver.set_page_load_timeout(30)
# driver.set_script_timeout(30)
# # chome_options = webdriver.ChromeOptions()
driver = webdriver.PhantomJS()
# driver = webdriver.Chrome(chromedriver, service_args=service_args)
# url = "https://www.jufaanli.com/search2?TypeKey=1%3A%E5%AE%9D%E9%92%A2%E7%89%B9%E9%92%A2%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8"
# base_url = "http://www.baidu.com"
# url = "https://www.jufaanli.com/search2?TypeKey=1:厂"
# url=""
# url
# name = urllib.quote(":厂")
# url = "https://www.jufaanli.com/search2?TypeKey=1{}".format(name)
# url1 = "https://www.jufaanli.com/search2?TypeKey=1:有限公司"
# url2 = "https://www.jufaanli.com/search2?TypeKey=1%3A%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8"
url3 = "https://www.jufaanli.com/search2?TypeKey=1%3A%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8"

# print urllib.quote(url1)
#
# print url
# url = "https://www.jufaanli.com/search2?TypeKey=1%3A%E5%8E%82"  # 这个可以

driver.get(url3)
LIST_LOCATOR = (By.XPATH, "//li[@class='active jufa-page-no']")
WebDriverWait(driver, 200).until(EC.presence_of_element_located(LIST_LOCATOR))
print driver.page_source
# if "JumpSelf()" in browser.page_source:
#     browser.find_element_by_xpath("/html/body/div/div[2]/input").click()
# WebDriverWait(browser, 20).until(EC.title_contains(u"裁判文书"))
# time.sleep(10)
