import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--tart--maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore--certificate-errors")

driver = webdriver.Chrome(executable_path="Driver/chromedriver/chromedriver")
time.sleep(5)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
time.sleep(3)
driver.quit()
