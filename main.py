from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from persiantools.jdatetime import JalaliDate
import datetime
import time
import os
FAVORITE_SPOT = 65659
# OPTIONS ; 8, 11, 14, 17
SESSION_ID = 8
username_id = os.environ.get("LIBR_USER")
libpassword = os.environ.get("LIBR_PASS")

# prepare date
tomorrow_date = (JalaliDate.today() + datetime.timedelta(days=1)).strftime("%Y%m%d")


# login to reservation page
driver = webdriver.Chrome()
driver.get("https://107007.samanpl.ir/Account/Login/?returnUrl=%2fHome%2fReserveService%3fps%3dKBFMcEX%2bcxjtd7qyA0Hwbg%3d%3d")
main_tab = driver.current_window_handle
username = driver.find_element(By.NAME, "UserName")
username.send_keys(f"{username_id}")
time.sleep(2)
password = driver.find_element(By.NAME, "Password")
password.send_keys(f"{libpassword}")
time.sleep(2)
login_button = driver.find_element(By.ID,"LoginBtn")
login_button.click()

#reserve the seat
date_selection_bar = driver.find_element(By.NAME,"StartDate1")
date_selection_bar.click()
wait = WebDriverWait(driver, 10)
tomorrow_date_selector = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,f'td[data-number="{tomorrow_date}"]')))
tomorrow_date_selector.click()
wait = WebDriverWait(driver, 7)
session_selector = wait.until(EC.element_to_be_clickable((By.ID,f"{SESSION_ID}")))
session_selector.click()
tabs = driver.window_handles
for tab in tabs:
    if tab != main_tab:
        driver.switch_to.window(tab)
        wait = WebDriverWait(driver, 15)
        spot_selector = wait.until(EC.visibility_of_element_located((By.XPATH,f'//*[@id="{FAVORITE_SPOT}"]')))
        spot_selector.click()
        reserve_button = driver.find_element(By.ID, "btnReserve")
        reserve_button.click()
        time.sleep(2)
        driver.close()

driver.quit()