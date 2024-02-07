from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s_obj = Service("C:\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s_obj)  # Corrected the case of 'webdriver'

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

time.sleep(5)

# admin --> users management --> users
driver.find_element(By.XPATH, "//a[@class='oxd-main-menu-item active']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='User Management']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Users']").click()

add_btn = driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()

#dropdown
enable=driver.find_element(By.XPATH,"//div[contains(text(),'Enabled')]").click()
disable=driver.find_element(By.XPATH,"//div[contains(text(),'Disabled')]").click()

#Validate that the Employee name should accept alphabets characters
emp_name=driver.find_element(By.XPATH,"//input[@placeholder='Type for hints...']").send_keys("odis adawel")

#Validate that the Employee name should not accept numbers and special characters
# emp_name=driver.find_element(By.XPATH,"//input[@placeholder='Type for hints...']").send_keys("123456")
# emp_name1=driver.find_element(By.XPATH,"//input[@placeholder='Type for hints...']").send_keys("$%^&@")

#input alphabets in username field
username=driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--focus']").send_keys("Odis Adalwin")

#input numbers in username field
#username=driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--focus']").send_keys("123456")

#Validate the user name with Symbols "+-=$^"
#username=driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--focus']").send_keys("+-=$^")

# validate the password field is accept all characters
password=driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Pass@123")

#validate the confirm password field matches password field
driver.find_element(By.XPATH,"//input[@type='password'][2]").send_keys("Pass@123")

#check the link on page
orng=driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()

