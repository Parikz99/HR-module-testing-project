from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s_obj = Service("C:\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSkills")
driver.maximize_window()

# Login (use your own credentials)
driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

# Navigate to Skills page
driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
driver.find_element(By.ID, "menu_admin_Qualifications").click()
driver.find_element(By.ID, "menu_admin_viewSkills").click()

# Checkbox
copywriting_checkbox = driver.find_element(By.XPATH, "//input[@value='Copywriting']")
copywriting_checkbox.click()

# Edit button
edit_button = driver.find_element(By.XPATH, "//input[@value='Edit']")
edit_button.click()

# after clicking on edit button
edit_skill_name = driver.find_element(By.ID, "skill_name").send_keys("content writing")

driver.find_element(By.ID, "btnSave").click()

# Navigate back to the Skills page
driver.find_element(By.ID, "menu_admin_viewSkills").click()

# Checkbox (uncheck for demonstration purposes)
copywriting_checkbox.click()

# Delete button
delete_button = driver.find_element(By.XPATH, "//input[@value='Delete']")
delete_button.click()
driver.switch_to.alert.accept()

driver.quit()

# ###################### education#############
# # go to View Education page
# driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
# driver.find_element(By.ID, "menu_admin_Qualifications").click()
# driver.find_element(By.ID, "menu_admin_viewEducation").click()
#
# checkbox = driver.find_element(By.XPATH, "//input[@value='College Undergraduate']").click()
# edit_button = driver.find_element(By.XPATH, "//input[@id='Edit']").click()
# edit_skill_name = driver.find_element(By.ID, "skill_name").send_keys("HSC graduate")
#
# save_btn=driver.find_element(By.XPATH, "//input[@id='btnSave']").click()
#
# delete_button = driver.find_element(By.XPATH, "//input[@id='btnDelete']").click()
# driver.switch_to.alert.accept()
#
# time.sleep(5)
#
# # Close the browser
# driver.quit()
#
# ###################### Licenses############
# driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
# driver.find_element(By.ID, "menu_admin_Qualifications").click()
# driver.find_element(By.ID, "menu_admin_viewLicenses").click()
#
# checkbox = driver.find_element(By.XPATH, "//input[@value='Certified Information Security Manager (CISM)']").click()
# edit_button = driver.find_element(By.XPATH, "//input[@id='Edit']").click()
# edit_skill_name = driver.find_element(By.ID, "skill_name").send_keys("Certified Trading Professional")
#
# save_btn=driver.find_element(By.XPATH, "//input[@id='btnSave']").click()
#
# delete_button = driver.find_element(By.XPATH, "//input[@id='btnDelete']").click()
# driver.switch_to.alert.accept()
#
# driver.close()
#
# ###################### Languages ############
# driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
# driver.find_element(By.ID, "menu_admin_Qualifications").click()
# driver.find_element(By.ID, "menu_admin_viewLanguages").click()
#
# checkbox = driver.find_element(By.XPATH, "//input[@value='Arabic']").click()
# edit_button = driver.find_element(By.XPATH, "//input[@id='Edit']").click()
# edit_skill_name = driver.find_element(By.ID, "language_name").send_keys("hindi")
#
# save_btn=driver.find_element(By.XPATH, "//input[@id='btnSave']").click()
#
# delete_button = driver.find_element(By.XPATH, "//input[@id='btnDelete']").click()
# driver.switch_to.alert.accept()
#
#
# ###################### Memberships ############
# driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
# driver.find_element(By.ID, "menu_admin_Qualifications").click()
# driver.find_element(By.ID, "menu_admin_viewMemberships").click()
#
# checkbox = driver.find_element(By.XPATH, "//input[@value='ACCA']").click()
# edit_button = driver.find_element(By.XPATH, "//input[@id='Edit']").click()
# name = driver.find_element(By.ID,"language_name").send_keys("Master of Science")
#
# save_btn=driver.find_element(By.XPATH, "//input[@id='btnSave']").click()
#
# delete_button = driver.find_element(By.XPATH, "//input[@id='btnDelete']").click()
# driver.switch_to.alert.accept()
#
# ###################### Nationalities ############
# driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
# driver.find_element(By.ID, "menu_admin_Nationalities").click()
#
# checkbox = driver.find_element(By.XPATH, "//input[@value='Afghan']").click()
# edit_button = driver.find_element(By.XPATH, "//input[@id='Edit']").click()
# name = driver.find_element(By.ID,"Nationality_name").send_keys("Indian")
#
# save_btn=driver.find_element(By.XPATH, "//input[@id='btnSave']").click()
#
# delete_button = driver.find_element(By.XPATH, "//input[@id='btnDelete']").click()
# driver.switch_to.alert.accept()

