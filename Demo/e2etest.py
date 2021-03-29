import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="Driver/chromedriver/chromedriver")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_xpath("/html/body/app-root/app-navbar/div/nav/ul/li[2]/a").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")

#//div[@class='card h-100']/div/h4/a
#product = //div[@class='card h-100']
for product in products:
    print(product.find_element_by_xpath("div/h4/a").text)
    productName = product.find_element_by_xpath("div/h4/a").text
    if productName == "Blackberry":
   #add to cart
       product.find_element_by_xpath("div/button").click()
       time.sleep(3)

driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li/a").click()
driver.find_element_by_xpath("/html/body/app-root/app-shop/div/div/div/table/tbody/tr[3]/td[5]/button").click()
driver.find_element_by_id("country").send_keys("ind")
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element_by_link_text("India").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/app-root/app-shop/div/app-checkout/div/div[2]").click()
driver.find_element_by_xpath("/html/body/app-root/app-shop/div/app-checkout/div/form/input").click()
print(driver.find_element_by_class_name("alert-success").text)
successText = driver.find_element_by_class_name("alert-success").text

assert "Success! Thank you!" in successText


driver.get_screenshot_as_file("screen.png")


