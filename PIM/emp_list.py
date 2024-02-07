from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

s_obj = Service("C:\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
driver.maximize_window()

employee_name = driver.find_element(By.XPATH, "//input[@id='empsearch_employee_name_empName']")
employee_name.send_keys("Maddy Doer")

employee_id = driver.find_element(By.XPATH, "//input[@id='empsearch_id']")
employee_id.send_keys("12345")

employment_status = Select(driver.find_element(By.XPATH, "//select[@id='empsearch_employee_status']"))
employment_status.select_by_visible_text("Full-Time Permanent")

include = Select(driver.find_element(By.XPATH, "//select[@id='empsearch_termination']"))
include.select_by_visible_text("Exclude")

supervisor_name = driver.find_element(By.XPATH, "//input[@id='empsearch_supervisor_name']")
supervisor_name.send_keys("Jane Supervisor")

job_title = Select(driver.find_element(By.XPATH, "//select[@id='empsearch_job_title']"))
job_title.select_by_visible_text("Manager")

sub_unit = Select(driver.find_element(By.XPATH, "//select[@id='empsearch_sub_unit']"))
sub_unit.select_by_visible_text("Administration")

search_button = driver.find_element(By.XPATH, "//input[@id='searchBtn']").click()

time.sleep(5)

add_button = driver.find_element(By.XPATH, "//input[@id='btnAdd']").click()
time.sleep(5)

driver.quit()
