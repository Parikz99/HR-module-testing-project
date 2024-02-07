from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s_obj = Service("C:\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s_obj)  # Corrected the case of 'webdriver'

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

#valid inputs
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

# numeric inputs
# driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("457956")
# driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
# driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

# symbol inputs
# driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("$&%^")
# driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
# driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

# check wheter checkbox is enable and displayed



driver.quit()
