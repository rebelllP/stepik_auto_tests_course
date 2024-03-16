from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


try:
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.XPATH, "/html/body//div[1]/div[1]/input[@required]")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.XPATH, "/html/body//div[1]/div[2]/input[@required]")
    last_name.send_keys("Ivanov")

    email = browser.find_element(By.XPATH, "/html/body//div[1]/div[3]/input[@required]")
    email.send_keys("@gmail")

    phone = browser.find_element(By.XPATH, "/html/body//div[2]/div[1]/input[@type = 'text']")
    phone.send_keys("+79995553366")

    address = browser.find_element(By.XPATH, "/html/body//div[2]/div[2]/input[@type = 'text']")
    address.send_keys("Russia")

    browser.find_element(By.TAG_NAME, "button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()