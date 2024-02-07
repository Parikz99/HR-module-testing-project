from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

s_obj = Service("C:\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet")
driver.maximize_window()

driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

driver.find_element(By.ID, "menu_time").click()

employee_name = driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']")
employee_name.send_keys("Odis Adalwin")

view_btn = driver.find_element(By.XPATH,"//button[@type=btn'View']").click()

# ############## attendance my records ######
#
# driver.find_element(By.ID, "menu_attendance_Attendance").click()
# driver.find_element(By.ID, "menu_attendance_viewMyAttendanceRecord").click()
#
# # Select date '2023/1/1'
# date_input = driver.find_element(By.ID, "attendance_date")
# date_input.clear()
# date_input.send_keys("2023-01-01")
#
# # Click on the 'View' button
# view_button = driver.find_element(By.ID, "viewBtn")
# view_button.click()
#
# ############ Reports ###########
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
#
# s_obj = Service("C:\\chromedriver-win64\\chromedriver.exe")
# driver = webdriver.Chrome(service=s_obj)
#
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/time/displayProjectReportCriteria")
# driver.maximize_window()
#
# driver.find_element(By.ID, "menu_time").click()
# driver.find_element(By.XPATH,"//span[normalize-space()='Reports']").click()
#
# date_range_start = driver.find_element(By.XPATH, "//input[@id='dateRangeStartDate']")
# date_range_start.clear()
# date_range_start.send_keys("01/01/2023")
#
# date_range_end = driver.find_element(By.XPATH, "//input[@id='dateRangeEndDate']")
# date_range_end.clear()
# date_range_end.send_keys("02/02/2023")
#
# approved_timesheets = driver.find_element(By.XPATH, "//input[@id='approvedOnly']")
# approved_timesheets.click()
#
# view_button = driver.find_element(By.XPATH, "//input[@id='viewButton']")
# view_button.click()
#
# time.sleep(5)
# driver.quit()
#
#
# ############ employee reports ##########
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
#
# s_obj = Service("C:\\chromedriver-win64\\chromedriver.exe")
# driver = webdriver.Chrome(service=s_obj)
#
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/time/displayEmployeeReportCriteria")
# driver.maximize_window()
#
# driver.find_element(By.ID, "menu_time").click()
# driver.find_element(By.XPATH,"//a[normalize-space()='Employee Reports']").click()
#
# driver.find_element(By.XPATH, "//select[@id='employee']").send_keys("Odis Adalwin")
# driver.find_element(By.XPATH, "//select[@id='project']").send_keys("ACME Ltd - ACME Ltd")
# driver.find_element(By.XPATH, "//select[@id='activity']").send_keys("bug fixes")
#
# driver.find_element(By.XPATH, "//input[@id='dateFrom']").clear()
# driver.find_element(By.XPATH, "//input[@id='dateFrom']").send_keys("2023/01/02")
#
# driver.find_element(By.XPATH, "//input[@id='dateTo']").clear()
# driver.find_element(By.XPATH, "//input[@id='dateTo']").send_keys("2023/06/02")
#
# driver.find_element(By.XPATH, "//input[@id='btnView']").click()
#
# time.sleep(5)
# driver.quit()


