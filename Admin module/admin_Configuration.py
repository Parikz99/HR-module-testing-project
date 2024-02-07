from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s_obj = Service("C:\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/listMailConfiguration")
driver.maximize_window()

# Login (use your own credentials)
driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

# Navigate to Mail Configuration page
driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
driver.find_element(By.ID, "menu_admin_Configuration").click()
driver.find_element(By.ID, "menu_admin_listMailConfiguration").click()
time.sleep(5)

# Interaction with the elements on the Mail Configuration page
mail_sent_as = driver.find_element(By.XPATH, "//input[@id='mail_configuration[send]']")
mail_sent_as.clear()
mail_sent_as.send_keys("parikshitchauk99@gmail.com")

secure_smtp_radio = driver.find_element(By.XPATH, "//input[@id='mail_configuration[sendSmtp]']").click()
#smtp = driver.find_element(By.XPATH, "//input[@id='mail_configuration[sendMail]']")
smtp_host_input = driver.find_element(By.XPATH, "//input[@id='mail_configuration[smtp_host]']").send_keys("www.google.com")
smtp_port_input = driver.find_element(By.XPATH, "//input[@id='mail_configuration[smtp_port]']").send_keys("587")
smtp_auth_no_radio = driver.find_element(By.XPATH, "//input[@id='mail_configuration[smtp_auth][0]']").click()
tls_switch = driver.find_element(By.XPATH, "//div[@class='oxd-switch-input oxd-switch-input--active']")
send_test_mail_switch = driver.find_element(By.XPATH, "//div[@class='oxd-switch-input oxd-switch-input--active']")
save_button = driver.find_element(By.XPATH, "//input[@id='btnSave']")

# Toggle TLS switch
tls_switch.click()
#send_test_mail_switch.click()

# Click the Save button
save_button.click()
driver.quit()
