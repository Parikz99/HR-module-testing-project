from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

s_obj = Service("C:\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/leave/addLeaveEntitlement")
driver.maximize_window()

# Login (use your own credentials)
driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

# Navigate to Add Leave Entitlement page
driver.find_element(By.ID, "menu_leave_viewLeaveModule").click()
driver.find_element(By.ID, "menu_leave_Entitlements").click()
driver.find_element(By.ID, "menu_leave_addLeaveEntitlement").click()

time.sleep(5)

# Interaction with the elements on the Add Leave Entitlement page
individual_employee = driver.find_element(By.XPATH, "//input[@id='leaveEntitlement_employee_empName']").click()
employee_name = Select(driver.find_element(By.XPATH, "//select[@id='leaveEntitlement_employee_empName']"))
employee_name.select_by_visible_text("John Smith")

leave_type = Select(driver.find_element(By.XPATH, "//select[@id='leaveEntitlement_leave_type_id']"))
leave_type.select_by_visible_text("CAN-FMLA")

leave_period = Select(driver.find_element(By.XPATH, "//select[@id='leaveEntitlement_leave_period']"))
leave_period.select_by_visible_text("2023/1/1-2023/12/31")

entitlement_input = driver.find_element(By.XPATH, "//input[@id='leaveEntitlement_entitlement']")
entitlement_input.send_keys("20")  # Adjust the entitlement value as needed

save_button = driver.find_element(By.XPATH, "//input[@id='btnSave']").click()

# Close the browser
driver.quit()

#
# ###################### Employee Entitlements
#
# # Navigate to View Leave Entitlements page
# driver.find_element(By.ID, "menu_leave_viewLeaveModule").click()
# driver.find_element(By.ID, "menu_leave_Entitlements").click()
# driver.find_element(By.ID, "menu_leave_viewLeaveEntitlements").click()
#
# # Interaction with the elements on the View Leave Entitlements page
# employee_name = Select(driver.find_element(By.XPATH, "//select[@id='leave_balance_emp_name']")).send_keys("Odis Adalwin")
# leave_type = Select(driver.find_element(By.XPATH, "//select[@id='leave_balance_leave_type']"))
# leave_type.select_by_visible_text("CAN-FMLA")
#
# leave_period = Select(driver.find_element(By.XPATH, "//select[@id='period']"))
# leave_period.select_by_visible_text("2021-01-01-2021-12-31")
#
# search_button = driver.find_element(By.XPATH, "//input[@id='searchBtn']").click()
#
# # Pause for a few seconds to see the results
# time.sleep(5)
#
# # Close the browser
# driver.quit()
