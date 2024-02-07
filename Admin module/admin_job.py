from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s_obj = Service("C:\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s_obj)  # Corrected the case of 'webdriver'

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

time.sleep(5)

# admin --> job --> job titles
driver.find_element(By.XPATH, "//a[@class='oxd-main-menu-item active']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Job']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Job Titles']").click()

#validate the add button
Add=driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()

job_title=driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--active']").send_keys("Senior Engineer")
job_des=driver.find_element(By.XPATH,"//textarea[@placeholder='Type description here']").send_keys("Senior Engineer: Lead and drive software development initiatives. Expertise in Java, Python, or C++. Strong leadership, problem-solving, and communication skills. Shape the future with our innovative IT team.")
notes=driver.find_element(By.XPATH,"//textarea[@placeholder='Add note']").send_keys("Senior Engineer role at Orange: Senior Engineer: Lead and drive software development initiatives. Expertise in Java, Python, or C++. Strong leadership, problem-solving, and communication skills. Shape the future with our innovative IT team.")
savebtn=driver.find_element(By.XPATH, "//button[@type='submit']").click()


# #validate the checkboxes and edit functionality
# chck_box=driver.find_element(By.XPATH,"//div[@role='table']").click()
#
# edit=driver.find_element(By.XPATH,"//button[@class='oxd-icon-button oxd-table-cell-action-space' and @type='button']").click()
#
# job_decription=driver.find_element(By.XPATH,"//textarea[@placeholder='Type description here']").send_keys("Seeking Assistant Engineer to contribute to software development, provide technical support, and ensure quality assurance. Bachelor's degree in CS, proficiency in Java, Python, or C++. Join us for a dynamic role in a forward-thinking IT company!")
# job_title=driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--active']").send_keys("Assistant Engineer")
# notes=driver.find_element(By.XPATH,"//textarea[@placeholder='Add note']").send_keys("Assistant Engineer role at Orange: Contribute to software dev, provide tech support, ensure QA. CS degree, Java/Python/C++. Join us for a dynamic role in a forward-thinking IT company!")
# save_btn=driver.find_element(By.XPATH, "//button[@type='submit']").click()

#
# ############ Pay Grade in job
#
# pay_grade=driver.find_element(By.XPATH,"//a[normalize-space()='Pay Grades']").click()
#
# #add button in pay grade
# pay_grade=driver.find_element(By.XPATH,"//a[normalize-space()='Pay Grades']").click()
#
# Add_btn=driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
#
# Name=driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--focus']").send_keys("Grade 8")
# save_btn=driver.find_element(By.XPATH, "//button[@type='submit']").click()
#
# ########### Employment status
# Emp_status=driver.find_element(By.XPATH,"//a[normalize-space()='Employment Status']").click()
#
# Add_btn=driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
#
# Name=driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--focus']").send_keys("Full time")
# save_btn=driver.find_element(By.XPATH, "//button[@type='submit']").click()
#
# ########### JOB Category
# job_category=driver.find_element(By.XPATH,"//a[normalize-space()='Job Categories']").click()
#
# Add_btn=driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
#
# Name=driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--focus']").send_keys("office staff")
# save_btn=driver.find_element(By.XPATH, "//button[@type='submit']").click()


