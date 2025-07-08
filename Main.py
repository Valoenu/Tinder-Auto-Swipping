# Tinder-Auto-Swipping

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.Keys import Keys
from selenium.common.exceptions import NoSichElementException, ElementClickInterceptedException
from time import sleep


EMAIL_ACCOUNT = "Your Email"
PASSWORD_ACCOUNT = "Your Password"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
webdriver.get("https://tinder.com/")



time.sleep(3)
log_in = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
log_in.click()


time.sleep(3)
facebook = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook.click()


time.sleep(5)
windows = driver.window_handles()
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
# Switch to Facebook log in window
driver.switch_to.window(fb_login_window)
print(driver.title)
time.sleep(2)

email = driver.find_element(By.XPATH, value='//*[@id="email"]')
email.send_Keys(PHONE_NUMBER)

passord = driver.find_element(By.XPATH, value='//*[@id="pass"]')
password.send_Keys(PASSWORD_ACCOUNT)
password.send_Keys(Keys.Enter)


driver.switch_to.window(base_window)
print(driver.title)
time.sleep(10)


# Click Allow (2nd option)
location_pop_up = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
location_pop_up.click()


# Click Not Interested (1nd option)
notification_pop_up = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notification_pop_up.click()

# Cookie Privacy
cookies = driver.find_element(By.XPATH, value="")
cookies.click()


for n in range(100):

  time.sleep(2)
  
  try:
    like = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
    like.click()

  #'Match' cases
  except ElementClickInterceptedException:
    try:
      match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
      match_popup.click()

          # Catches situations where the "Like" button has not yet loaded
  except NoSuchElementException:
    sleep(2)

time.quit()

