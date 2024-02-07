from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

s_obj = Service("C:\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7")
driver.maximize_window()

driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

driver.find_element(By.ID, "menu_pim_viewMyDetails").click()

first_name = driver.find_element(By.XPATH, "//input[@id='personal_txtEmpFirstName']")
first_name.clear()
first_name.send_keys("parikshit")

middle_name = driver.find_element(By.XPATH, "//input[@id='personal_txtEmpMiddleName']")
middle_name.clear()
middle_name.send_keys("nayan")

last_name = driver.find_element(By.XPATH, "//input[@id='personal_txtEmpLastName']")
last_name.clear()
last_name.send_keys("chauk")

nickname = driver.find_element(By.XPATH, "//input[@id='personal_txtEmpNickName']")
nickname.clear()
nickname.send_keys("parikz")

employee_id = driver.find_element(By.XPATH, "//input[@id='personal_txtEmployeeId']")
employee_id.clear()
employee_id.send_keys("123456")

license_number = driver.find_element(By.XPATH, "//input[@id='personal_txtLicenNo']")
license_number.send_keys("ABC123")

license_expiry_date = driver.find_element(By.XPATH, "//input[@id='personal_txtLicExpDate']")
license_expiry_date.send_keys("2025-01-02")

ssn_number = driver.find_element(By.XPATH, "//input[@id='personal_txtNICNo']")
ssn_number.send_keys("123-45-6789")

sin_number = driver.find_element(By.XPATH, "//input[@id='personal_txtSINNo']")
sin_number.send_keys("987654321")

nationality = Select(driver.find_element(By.XPATH, "//select[@id='personal_cmbNation']"))
nationality.select_by_visible_text("Indian")

marital_status = Select(driver.find_element(By.XPATH, "//select[@id='personal_cmbMarital']"))
marital_status.select_by_visible_text("Single")

date_of_birth = driver.find_element(By.XPATH, "//input[@id='personal_DOB']")
date_of_birth.clear()
date_of_birth.send_keys("1997-01-03")

gender = Select(driver.find_element(By.XPATH, "//select[@id='personal_cmbSex']"))
gender.select_by_visible_text("Male")

military_service = driver.find_element(By.XPATH, "//input[@id='personal_chkSmokeFlag']").click()

blood_type = Select(driver.find_element(By.XPATH, "//select[@id='personal_cmbBlood']"))
blood_type.select_by_visible_text("B+")

add_attachment_button = driver.find_element(By.XPATH, "//input[@id='btnAddAttachment']").click()

comment = driver.find_element(By.XPATH, "//textarea[@id='personal_txtEmpNickName']")
comment.send_keys("Adding a comment for testing")

driver.find_element(By.XPATH, "//input[@id='btnSave']").click()

time.sleep(5)
driver.quit()


# ################### contact #########
#
# driver.find_element(By.ID, "menu_pim_viewMyDetails").click()
# driver.find_element(By.ID, "menu_pim_viewContact").click()
#
# street1 = driver.find_element(By.ID, "contact_street1")
# street1.clear()
# street1.send_keys("Updated Street 1")
#
# street2 = driver.find_element(By.ID, "contact_street2")
# street2.clear()
# street2.send_keys("Updated Street 2")
#
# city = driver.find_element(By.ID, "contact_city")
# city.clear()
# city.send_keys("Updated City")
#
# state = driver.find_element(By.ID, "contact_province")
# state.clear()
# state.send_keys("Updated State")
#
# zip_code = driver.find_element(By.ID, "contact_emp_zipcode")
# zip_code.clear()
# zip_code.send_keys("12345")
#
# country = Select(driver.find_element(By.ID, "contact_country"))
# country.select_by_visible_text("India")
#
# telephone_home = driver.find_element(By.ID, "contact_emp_hm_telephone")
# telephone_home.clear()
# telephone_home.send_keys("1234567890")
#
# mobile = driver.find_element(By.ID, "contact_emp_mobile")
# mobile.clear()
# mobile.send_keys("9876543210")
#
# work = driver.find_element(By.ID, "contact_emp_work_telephone")
# work.clear()
# work.send_keys("9876543211")
#
# work_email = driver.find_element(By.ID, "contact_emp_work_email")
# work_email.clear()
# work_email.send_keys("updated@example.com")
#
# save_button = driver.find_element(By.ID, "btnSave").click()
#
# time.sleep(5)
# driver.quit()
