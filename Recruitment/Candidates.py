from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

s_obj = Service("C:\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
driver.maximize_window()

driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

driver.find_element(By.ID, "menu_recruitment_viewRecruitmentModule").click()
driver.find_element(By.ID, "menu_recruitment_viewCandidates").click()

job_title = Select(driver.find_element(By.ID, "candidateSearch_jobTitle"))
job_title.select_by_visible_text("Account Assitant")

vacancy = Select(driver.find_element(By.ID, "candidateSearch_vacancy"))
vacancy.select_by_visible_text("Junior Account Assitant")

hiring_manager = Select(driver.find_element(By.ID, "candidateSearch_hiringManager"))
hiring_manager.select_by_visible_text("Odis Adalwin")

status = Select(driver.find_element(By.ID, "candidateSearch_status"))
status.select_by_visible_text("Shortlisted")

candidate_name = driver.find_element(By.ID, "candidateSearch_candidateName")
candidate_name.send_keys("Mohan K")

date_of_application_from = driver.find_element(By.ID, "candidateSearch_dateFrom")
date_of_application_from.send_keys("2021-01-02")

date_of_application_to = driver.find_element(By.ID, "candidateSearch_dateTo")
date_of_application_to.send_keys("2021-02-02")

method_of_application= Select(driver.find_element(By.ID, "candidateSearch_methodOfApplication"))
method_of_application.select_by_visible_text("Manual")

search_button = driver.find_element(By.ID, "btnSrch").click()

time.sleep(5)

driver.quit()

# #### Add button in candidate
#
# Add_button = driver.find_element(By.ID,"btnAdd")
#
# full_name = driver.find_element(By.ID, "addCandidate_firstName").send_keys("Parikshit Nayan Chauk")
#
# vacancy= Select(driver.find_element(By.ID, "addCandidate_vacancy")).select_by_visible_text("Senior QA Lead")
#
# email = driver.find_element(By.ID, "addCandidate_email").send_keys("parikshit@gmail.com")
#
# contact_number = driver.find_element(By.ID, "addCandidate_contactNo").send_keys("1234567890")
#
# resume = driver.find_element(By.ID, "addCandidate_resume").send_keys("C:/Users/Hp/Desktop/resume.pdf")
#
# keywords = driver.find_element(By.ID,"addCandidate_keyWords")
# keywords.send_keys("QA, Lead, Testing")
#
# date_of_application = driver.find_element(By.ID, "addCandidate_appliedDate")
# date_of_application.send_keys("2024-01-15")
#
# notes= driver.find_element(By.ID, "addCandidate_comment").send_keys("This candidate has extensive experience in QA.")
#
# save_button = driver.find_element(By.ID, "btnSave").click()
#
# time.sleep(5)
#
# # Close the browser
# driver.quit()
