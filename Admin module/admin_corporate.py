from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s_obj = Service("C:\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/addTheme")
driver.maximize_window()

# Login (use your own credentials)
driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

# Navigate to Add Theme page
driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
driver.find_element(By.ID, "menu_admin_Corporate_Branding").click()

time.sleep(5)

primary_color_input = driver.find_element(By.ID, "theme_primary").send_keys("#402716")
primary_font_color_input = driver.find_element(By.ID, "theme_font_primary").send_keys("#3498db")
primary_gradient_color1_input = driver.find_element(By.ID, "theme_gradient_primary1").send_keys("#ffffff")
secondary_color_input = driver.find_element(By.ID, "theme_secondary").send_keys("#e74c3c")
secondary_font_color_input = driver.find_element(By.ID, "theme_font_secondary").send_keys("#2980b9")
primary_gradient_color2_input = driver.find_element(By.ID, "theme_gradient_secondary2").send_keys("#c0392b")

client_logo_input = driver.find_element(By.ID, "client_logo").send_keys("C:/Users/Hp/Desktop/apple.png")
client_banner_input = driver.find_element(By.ID, "client_banner").send_keys("C:/Users/Hp/Desktop/apple.png")
login_banner_input = driver.find_element(By.ID, "login_banner").send_keys("C:/Users/Hp/Desktop/apple.png")

publish_button = driver.find_element(By.ID, "btnSave")

# Click the Publish button
publish_button.click()

# Close the browser
driver.quit()
