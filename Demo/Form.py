import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="Driver/chromedriver/chromedriver")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("Ticvic")
time.sleep(5)
driver.find_element_by_name("email").send_keys("test@gmail.com")
time.sleep(3)
driver.find_element_by_id("exampleInputPassword1").send_keys("Password")
time.sleep(5)
driver.find_element_by_id("exampleCheck1").click()

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
time.sleep(5)
dropdown.select_by_index(0)
time.sleep(5)

driver.find_element_by_xpath("/html/body/app-root/form-comp/div/form/input").click()
time.sleep(3)
message = driver.find_element_by_class_name("alert-success").text
print(message)