from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

s_obj = Service("C:\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewMyLeaveList")
driver.maximize_window()

# Login (use your own credentials)
driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

# Navigate to View My Leave List page
driver.find_element(By.ID, "menu_leave_viewLeaveModule").click()
driver.find_element(By.ID, "menu_leave_viewMyLeaveList").click()

# Interaction with the elements on the View My Leave List page
from_date_input = driver.find_element(By.XPATH, "//input[@id='calFromDate']")
from_date_input.clear()
from_date_input.send_keys("2023-10-02")

to_date_input = driver.find_element(By.XPATH, "//input[@id='calToDate']")
to_date_input.clear()
to_date_input.send_keys("2023-11-03")

show_leave_with_status = Select(driver.find_element(By.XPATH, "//select[@id='leaveList_cmbSubunit']"))
show_leave_with_status.select_by_visible_text("pending")

leave_type = Select(driver.find_element(By.XPATH, "//select[@id='leaveList_cmbWithTermination']"))
leave_type.select_by_visible_text("US-FMLA")

search_button = driver.find_element(By.XPATH, "//input[@id='btnSearch']").click()

time.sleep(5)

# Close the browser
driver.quit()
