#! /usr/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import schedule
import time
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By

# 定义打开链接
def connection_network(url):
    count_down(minutes=10,seconds=0)   #修改时间多久登陆一次，默认10分钟
    my_username = ''     #填写自己的账号
    my_password = ''      #填写自己的密码
    global driver
    options = webdriver.ChromeOptions()
    # options.add_experimental_option('detach', True) #不自动关闭浏览器
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    path=Service('/home/xss/zhangxiaozhi/packages/chromedriver_linux64/chromedriver')
    driver = webdriver.Chrome(options=options,service=path)
    driver.minimize_window()  #最小化浏览器
    #driver.set_window_size(424, 424)
    driver.get(url)
    time.sleep(2)
    try:
        input_username = driver.find_element(By.XPATH, '//input[@id="username"]')
        input_username.send_keys(my_username)
        time.sleep(1)
        input_password = driver.find_element(By.XPATH, '//input[@id="pwd_tip"]')
        input_password.click()
        input_password = driver.find_element(By.XPATH, '//input[@id="pwd"]')
        input_password.send_keys(my_password)
        time.sleep(1)
        save_password= driver.find_element(By.XPATH,'/html/body/div[2]/table/tbody/tr[2]/td[2]/div/div/div[14]/div[1]/div[1]/div')
        save_password.click()
        time.sleep(1)
        auto_connection = driver.find_element(By.XPATH,'/html/body/div[2]/table/tbody/tr[2]/td[2]/div/div/div[14]/div[3]/div[1]/div')
        auto_connection.click()
        time.sleep(1)
        submit_btn = driver.find_element(By.XPATH, '//div[@id="loginLink_div"]')
        submit_btn.click()
        print("\t登陆成功")
    except:
        print("\t无需重复登陆")
    time.sleep(3)
    driver.quit()

def count_down(weeks=0, days=0, hours=0, minutes=0, seconds=0):
    remain_time = timedelta(weeks=weeks, days=days, hours=hours, minutes=minutes, seconds=seconds)
    now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    while remain_time.total_seconds() > 0:
        time.sleep(1)
        remain_time -= timedelta(seconds=1)
        print("\r上一次登陆{}-->距下一次登陆 倒计时：{}".format(now_time,remain_time), end="", flush=True)

if __name__ == '__main__':
    e_time = 1
    schedule.every(e_time).seconds.do(connection_network, url='http://172.30.1.1')    
    # schedule.every().days.at("12:41").do(connection_network)

    while True:
        schedule.run_pending()
        
