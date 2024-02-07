from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

s_obj = Service("C:\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewJobVacancy")
driver.maximize_window()

driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

driver.find_element(By.ID, "menu_recruitment_viewRecruitmentModule").click()
driver.find_element(By.ID, "menu_recruitment_viewJobVacancy").click()

job_title = Select(driver.find_element(By.ID, "vacancySearch_jobTitle"))
job_title.select_by_visible_text("Account Assistant")

vacancy = Select(driver.find_element(By.ID, "vacancySearch_jobVacancy"))
vacancy.select_by_visible_text("Senior QA Lead")

hiring_manager = Select(driver.find_element(By.ID, "vacancySearch_hiringManager"))
hiring_manager.select_by_visible_text("John Smith")

status= Select(driver.find_element(By.ID, "vacancySearch_status"))
status.select_by_visible_text("Active")

search_button = driver.find_element(By.ID, "btnSrch").click()

driver.quit()


# ############ ADD button in vacancies
# driver.find_element(By.ID, "btnAdd").click()
#
# job_title = Select(driver.find_element(By.ID, "addJobVacancy_jobTitle"))
# job_title.select_by_visible_text("Account Assistant")
#
# vacancy = driver.find_element(By.ID, "addJobVacancy_name")
# vacancy.send_keys("Senior QA Lead")
#
# description = driver.find_element(By.ID, "addJobVacancy_description")
# description.send_keys("This is a senior QA lead position description.")
#
# hiring_manager = Select(driver.find_element(By.ID, "addJobVacancy_hiringManager"))
# hiring_manager.select_by_visible_text("Odis Adalwin")
#
# number_of_positions = driver.find_element(By.ID, "addJobVacancy_noOfPositions").send_keys("5")
# active_switch = driver.find_element(By.ID, "addJobVacancy_status").click()
# save_button = driver.find_element(By.ID, "btnSave").click()
#
# time.sleep(5)
#
# driver.quit()