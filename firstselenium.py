# 从selenium 导入webdriver
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Firefox() # 创建浏览器对象
driver.get("https://www.baidu.com") # 打开百度
time.sleep(1)
# 定位元素，然后操作元素
driver.find_element(by=By.ID, value="kw").send_keys("Selenium2")
time.sleep(1)
driver.find_element(by=By.ID, value="su").click()
time.sleep(1)
driver.quit()
