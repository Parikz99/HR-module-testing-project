from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from tkinter.tix import Select
import time

s_obj = Service("C:\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

time.sleep(5)

# Admin --> Organization --> General Information
driver.find_element(By.XPATH, "//span[normalize-space()='Organization']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='General Information']").click()

# Clicking the edit button
driver.find_element(By.XPATH, "//span[@class='oxd-switch-input oxd-switch-input--active --label-left']").click()

# Updating organization information
org_name = driver.find_element(By.XPATH, "//input[@id='organization_name']").clear()
org_name.send_keys("Orange HRM")

reg_number = driver.find_element(By.XPATH, "//input[@id='organization_registrationNumber']").clear()
reg_number.send_keys("1234")

tax_id = driver.find_element(By.XPATH, "//input[@id='organization_taxId']").clear()
tax_id.send_keys("5678")

phone = driver.find_element(By.XPATH, "//input[@id='organization_phone']").clear()
phone.send_keys("5678")

fax = driver.find_element(By.XPATH, "//input[@id='organization_fax']").clear()
fax.send_keys("5678")

email = driver.find_element(By.XPATH, "//input[@id='organization_email']").clear()
email.send_keys("info@orangehrm.com")

add1 = driver.find_element(By.XPATH, "//input[@id='organization_address1']").clear()
add1.send_keys("538 Teal Plaza")

add2 = driver.find_element(By.XPATH, "//input[@id='organization_address2']").clear()
add2.send_keys("Mysore")

city = driver.find_element(By.XPATH, "//input[@id='organization_city']").clear()
city.send_keys("Secaucus")

state_province = driver.find_element(By.XPATH, "//input[@id='organization_province']").clear()
state_province.send_keys("NJ")

zip_postal = driver.find_element(By.XPATH, "//input[@id='organization_postalCode']").clear()
zip_postal.send_keys("51217")

notes = driver.find_element(By.XPATH, "//textarea[@id='organization_notes']").clear()
notes.send_keys("HRM Software")

# Clicking the Save button
save_btn = driver.find_element(By.XPATH, "//button[@type='submit']").click()


# #################### location #############
#
# driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
# driver.find_element(By.ID, "menu_admin_Organization").click()
# driver.find_element(By.ID, "menu_admin_viewLocations").click()
#
# name_input = driver.find_element(By.ID, "searchLocation_locationName").send_keys("canadian")
# city_input = driver.find_element(By.ID, "searchLocation_city").send_keys("ottawa")
# country_dropdown = Select(driver.find_element(By.ID, "searchLocation_country"))
# country_dropdown.select_by_visible_text("Canada")
# search_button = driver.find_element(By.ID, "searchBtn").click()
#
# add_button = driver.find_element(By.ID, "btnAdd").click()
#
# name_input = driver.find_element(By.XPATH, "//input[@id='location_name']").send_keys("HQ India")
# city_input = driver.find_element(By.XPATH, "//input[@id='location_city']").send_keys("prabhadevi")
# state_input = driver.find_element(By.XPATH, "//input[@id='location_province']").send_keys("maharashtra")
# zip_code_input = driver.find_element(By.XPATH, "//input[@id='location_zipCode']").send_keys("54128")
# country_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='location_country']"))
# country_dropdown.select_by_visible_text("india")
# phone_input = driver.find_element(By.XPATH, "//input[@id='location_phone']").send_keys("9876548896")
# fax_input = driver.find_element(By.XPATH, "//input[@id='location_fax']").send_keys("45643")
# address_input = driver.find_element(By.XPATH, "//textarea[@id='location_address']").send_keys("mumbai")
# notes_input = driver.find_element(By.XPATH, "//textarea[@id='location_notes']").send_keys("work from office is started")
# save_button = driver.find_element(By.XPATH, "//button[@id='btnSave']").click()
#
#
# driver.quit()

