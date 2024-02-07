from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

s_obj = Service("C:\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/performance/searchPerformanceReview")
driver.maximize_window()

driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

driver.find_element(By.ID, "menu_performance_defaultPerformance").click()
driver.find_element(By.ID, "menu_performance_searchPerformancReview").click()

employee_name = Select(driver.find_element(By.ID, "employeeName"))
employee_name.select_by_visible_text("Odis Adalwin")

job_title = Select(driver.find_element(By.ID, "jobTitle"))
job_title.select_by_visible_text("Chief technical officer")

review_status = Select(driver.find_element(By.ID, "status"))
review_status.select_by_visible_text("Activated")

include = Select(driver.find_element(By.ID, "include"))
include.select_by_visible_text("Current Employees Only")

reviewer = driver.find_element(By.ID, "employeeReviewerName_empName")
reviewer.send_keys("John Doe")

from_date = driver.find_element(By.ID, "fromDate")
from_date.send_keys("2024-01-01")

to_date = driver.find_element(By.ID, "toDate")
to_date.send_keys("2025-01-01")

search_button = driver.find_element(By.ID, "searchBtn").click()

time.sleep(5)

driver.quit()

# ####################### Employee Reviews ##################
#
# driver.find_element(By.ID, "menu_performance_defaultPerformance").click()
# driver.find_element(By.ID, "menu_performance_searchEmployeeReview").click()
#
# employee_name = Select(driver.find_element(By.ID, "employeeName"))
# employee_name.select_by_visible_text("Odis Adalwin")
#
# job_title = Select(driver.find_element(By.ID, "jobTitle"))
# job_title.select_by_visible_text("Chief technical officer")
#
# sub_unit = Select(driver.find_element(By.ID, "subUnit"))
# sub_unit.select_by_visible_text("Administration")
#
# include = Select(driver.find_element(By.ID, "include"))
# include.select_by_visible_text("Current Employees Only")
#
# reviewer = driver.find_element(By.ID, "employeeReviewerName_empName")
# reviewer.send_keys("John Doe")
#
# from_date = driver.find_element(By.ID, "fromDate")
# from_date.send_keys("2024-01-01")
#
# to_date = driver.find_element(By.ID, "toDate")
# to_date.send_keys("2025-01-01")
#
# search_button = driver.find_element(By.ID, "searchBtn").click()
#
# time.sleep(5)
#
# driver.quit()
#
# ############# TRACKER ##########
#
# driver.find_element(By.ID, "menu__Performance").click()
# driver.find_element(By.ID, "menu_performance_viewMyPerformanceTrackerList").click()
#
# # Click the "View" button
# view_btn = driver.find_element(By.XPATH, "//button[@name='view']").click()
# Add_btn = driver.find_element(By.XPATH,"//button[normalize-space()='Add Log']").click()
#
# log=driver.find_element(By.XPATH,"//input[@placeholder='Type here']")
# log.send_keys("hello")
#
# pos_btn=driver.find_element(By.XPATH,"//button[normalize-space()='Positive']").click()
#
# comment=driver.find_element(By.XPATH,"//textarea[@placeholder='Type here']")
# comment.send_keys("he is the best employee")
#
# save_btn=driver.find_element(By.XPATH,"//button[@type='submit']").click()
#
# time.sleep(5)
#
# driver.close()

