from selenium import webdriver
import time

url = 'https://www.douban.com/'
driver = webdriver.Chrome()
driver.get(url)
driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
time.sleep(2)
login = driver.find_element_by_class_name('account-tab-account')
login.click()
time.sleep(1)
# name_login = driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__footerULoginBtn"]')
# name_login.click()
# time.sleep(1)
username = driver.find_element_by_id('username')
username.send_keys('13188880405')
psw = driver.find_element_by_id('password')
psw.send_keys('Dd19950213')
submit = driver.find_element_by_link_text('登录豆瓣')
submit.click()
time.sleep(1)
more = driver.find_element_by_xpath('//*[@id="db-global-nav"]/div/div[1]/ul/li[2]/a/span[1]')
more.click()
logout = driver.find_element_by_link_text('退出')
logout.click()

