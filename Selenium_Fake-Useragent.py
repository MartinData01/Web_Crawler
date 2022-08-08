from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,random
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options

ua = UserAgent()
options = Options()
options.add_argument('--headless')
options.add_argument("user-agent=" + ua.chrome)
# driver = webdriver.Chrome(chrome_driver_path, options=options)
#pycharm專用
driver = webdriver.Chrome("chromedriver.exe")

driver.implicitly_wait(10)
url = "https://www.google.com/"
driver.get(url)
Q = "apple"

keyword = driver.find_element_by_css_selector("body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")
#fakebox-input
keyword.clear()
time.sleep(random.uniform(2, 3))
keyword.send_keys(Q)
keyword.send_keys(Keys.ENTER)
time.sleep(3)

#google
# //*[@id="rso"]/div[1]/div[1]/div/div[1]/div/div[2]/div/div[1]/a/h3/span
# //div[@class='yuRUbf']/a/h3[@class='LC20lb MBeuO DKV0Md']
items = driver.find_elements_by_xpath("//div[@class='yuRUbf']/a/h3[@class='LC20lb MBeuO DKV0Md']")

for i, item in enumerate(items):
    print(i, item.text)
driver.quit()