from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

s_obj = Service("C:\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/directory/viewDirectory")
driver.maximize_window()

driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

driver.find_element(By.ID, "menu_directory_viewDirectory").click()

employee_name = Select(driver.find_element(By.ID, "searchDirectory_emp_name_empName"))
employee_name.select_by_visible_text("Odis Adalwin")

job_title = Select(driver.find_element(By.ID, "searchDirectory_job_title"))
job_title.select_by_visible_text("Chief Technical Officer")

location = Select(driver.find_element(By.ID, "searchDirectory_location"))
location.select_by_visible_text("HQ-CA,USA")

search_btn = driver.find_element(By.ID, "searchBtn").click()

time.sleep(5)

driver.quit()
