from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

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

# Select the first mat-card inside col-3
first_mat_card = driver.find_element(By.XPATH, "//div[contains(@class, 'col-3')]//mat-card[1]")
first_mat_card.click()  # Click the mat-card

time.sleep(2)

# Select and click the second div inside the first mat-card
first_mat_card.find_element(By.XPATH, "./div[2]").click()
time.sleep(2)

driver.find_element(By.XPATH, "//button[contains(@class, 'mat-primary')]//span[contains(text(),' Delete Package Type')]").click()
time.sleep(2)


# Logout
driver.find_element(By.XPATH, "//mat-icon[text()='more_vert']").click()
driver.find_element(By.XPATH, "//button[contains(text(), 'Logout')]").click()
time.sleep(3)

# Close browser
driver.quit()
