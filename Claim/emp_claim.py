from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

s_obj = Service("C:\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/claim/viewAssignClaim")
driver.maximize_window()

driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

driver.find_element(By.ID, "menu_claim_viewClaimAssignments").click()

employee_name = Select(driver.find_element(By.XPATH, "//select[@id='employee_name']"))
employee_name.select_by_visible_text("Odis Adalwin")

reference_id = driver.find_element(By.XPATH, "//input[@id='assign_claim_claim_id']")
reference_id.send_keys("202307180000004")

event_name = Select(driver.find_element(By.XPATH, "//select[@id='assign_claim_claim_event_id']"))
event_name.select_by_visible_text("Accommodation")

status = Select(driver.find_element(By.XPATH, "//select[@id='assign_claim_claim_status']"))
status.select_by_visible_text("Submitted")

from_date = driver.find_element(By.XPATH, "//input[@id='assign_claim_date_assign_from']")
from_date.send_keys("2024-01-03")

to_date = driver.find_element(By.XPATH, "//input[@id='assign_claim_date_assign_to']")
to_date.send_keys("2024-02-04")

include = driver.find_element(By.XPATH, "//input[@id='assign_claim_include_terminated']").click()
search_button = driver.find_element(By.XPATH, "//input[@id='assign_claim_include_terminated']/following-sibling::input[@id='searchBtn']")
search_button.click()

time.sleep(5)

driver.quit()

# ######## Assign claims ########
#
# driver.find_element(By.ID, "menu_dashboard_index").click()
# driver.find_element(By.ID, "menu_dashboard_assignLeave").click()
#
# assign_button = driver.find_element(By.XPATH, "//button[@id='assignBtn']").click()
#
# employee_name = Select(driver.find_element(By.XPATH, "//select[@id='assignleave_txtEmployee_empName']"))
# employee_name.select_by_visible_text("Odis Adalwin")
#
# event = Select(driver.find_element(By.XPATH, "//select[@id='assignleave_claim_type']"))
# event.select_by_visible_text("Accommodation")
#
# currency = Select(driver.find_element(By.XPATH, "//select[@id='assignleave_currency_id']"))
# currency.select_by_visible_text("Albanian Lek")
#
# remark = driver.find_element(By.XPATH, "//textarea[@id='assignleave_txtComment']")
# remark.send_keys("This is a test remark for assignment")
#
# create_button = driver.find_element(By.XPATH, "//input[@id='assignBtn']").click()
#
# time.sleep(5)
#
# driver.quit()