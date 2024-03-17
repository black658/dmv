# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import re
import datetime
import time
import random

# %%
driver = webdriver.Chrome()

# %%
def set_up():
    driver.get("https://dmv.de.gov/mydmv.ejs?command=MyDMVLogin")
    driver.find_element(By.ID, "username").send_keys("usr1548")
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.ID, "submitBtn").click()
    try:
        driver.find_element(By.LINK_TEXT, "Close").click()
    except:
        pass
    driver.find_element(By.LINK_TEXT, "Road Test Appointment").click()
    driver.find_element(By.ID, "submitNew").click()
    driver.find_element(By.ID, "next").click()
def attempt_to_book():
    driver.find_element(By.ID, "firstAvailable").click()
    buttons = WebDriverWait(driver, 300).until(lambda x: x.find_elements(By.CLASS_NAME, "button1")) 
    for button in buttons:
        time = re.search('2024-0[234].*T', button.get_attribute("onclick")).group()[:-1]
        print(str(datetime.datetime.now()), "available:", time)
        if time > "2024-02-17" and time < "2024-03-04":
            button.click()
            e = driver.find_element(By.ID, "confirmAdd")
            driver.execute_script("arguments[0].click();",e)
            return True
    return False


# %%
while True:
    try:
        set_up()
        while not attempt_to_book():
            time.sleep(random.randint(1, 120))
        break
    except:
        time.sleep(60)



