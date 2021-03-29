import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="Driver/chromedriver/chromedriver")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
time.sleep(5)

print(len(checkboxes))

for checkbox in checkboxes:
    print(checkbox.get_attribute("value"))
    #if checkbox.get_attribute("value") =="option2":
    checkbox.click()
    assert  checkbox.is_selected()

radiobuttons = driver.find_elements_by_name("radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()