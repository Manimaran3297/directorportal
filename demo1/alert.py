from selenium import webdriver

validateText = "Option3"
driver = webdriver.Chrome(executable_path="Driver/chromedriver/chromedriver")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#name").send_keys("Option3")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
#alertText = alert.text
#assert validateText in alertText
#alert.accept()

alert.dismiss()