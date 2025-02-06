from ast import Return
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Setup WebDriver
driver = webdriver.Chrome()
driver.get("https://ecspro-qa.kloudship.com")

# Login
driver.find_element(By.ID, "login-email").send_keys("kloudship.qa.automation@mailinator.com")
driver.find_element(By.ID, "login-password").send_keys("Password1")
driver.find_element(By.ID, "login-btn").send_keys(Keys.RETURN)
time.sleep(5)

# Click on "Package Types"
package_types_element = driver.find_element(By.XPATH, "//span[contains(text(),'Package Types')]/parent::p/parent::mat-card")
package_types_element.click()
time.sleep(5)


# Click on the Add Button
add_button = driver.find_element(By.XPATH, "//button[contains(@class,'mat-icon-button')]//mat-icon[text()='add']")
add_button.click()
time.sleep(5)

# Randomize dimensions for package
random_length = random.randint(1, 20)
random_breadth = random.randint(1, 20)
random_height = random.randint(1, 20)



# Fill out the form
driver.find_element(By.CSS_SELECTOR, "[formcontrolname='name']").send_keys("Shrish_gupta")  # Name field
driver.find_element(By.CSS_SELECTOR, "[formcontrolname='length']").send_keys(random_length)  # Name field
driver.find_element(By.CSS_SELECTOR, "[formcontrolname='width']").send_keys(random_breadth)  # Name field
driver.find_element(By.CSS_SELECTOR, "[formcontrolname='height']").send_keys(random_height)  # Name field
driver.find_element(By.TAG_NAME, "form").submit()  # Name field
time.sleep(5)

#Log out
driver.find_element(By.XPATH, "//mat-icon[text()='more_vert']").click()
driver.find_element(By.XPATH, "//button[contains(text(), 'Logout')]").click()
time.sleep(3)