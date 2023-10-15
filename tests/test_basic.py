import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver import Keys
from multiprocessing import Process, Pipe, Pool

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import multiprocessing
from threading import Thread

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def func(x):
  return x+1

def access_gmailSignUp_main():
  driver.implicitly_wait(5)
  driver.get("https://accounts.google.com/signup")
  return driver

def is_gmail_backend_down():
  driver.implicitly_wait(10)
  driver.get("https://accounts.google.com/signup")
  return 0

def validate_mainURL():
  driver = access_gmailSignUp_main()
  result = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/h1/span").text
  if result != "Create a Google Account":
    return -1

  if "createaccount" not in str(driver.current_url):
    return -1

  return 0

#/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/button/div[3]
def createAccount_nameFieldValidation():
  driver = access_gmailSignUp_main()
  WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[id='firstName']")))

  driver.find_element(By.CSS_SELECTOR, "[id='firstName']").send_keys("newFirstName")
  if driver.find_element(By.CSS_SELECTOR, "[id='firstName']").get_attribute("data-initial-value") != "newFirstName":
    return -1

  driver.find_element(By.CSS_SELECTOR, "[id='lastName']").send_keys("newLastName")
  if driver.find_element(By.CSS_SELECTOR, "[id='lastName']").get_attribute("data-initial-value") != "newLastName":
    return -1

  driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/button/span").click()
  time.sleep(2)
  if "birthdaygender" not in str(driver.current_url):
    return -1
  return 0

def birthdayGender_inputValidation():
  return 0

def multiple_clients_openURL():
  def gmailClient(number, result):
    driver = webdriver.Chrome()
    driver.get("https://accounts.google.com/signup")

    title = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/h1/span").text
    if title != "Create a Google Account":
      result[number] = "fail"
    # time.sleep(2)

  number_of_clients = 10
  threads = []
  results = [""] * 10

  for number in range(number_of_clients):
    t = Thread(target=gmailClient, args=(number, results))  # get number for place in list `buttons`
    t.start()
    threads.append(t)

  for t in threads:
    t.join()

  if "fail" in "".join(results):
    return -1
  return 0

# PERFORMANCE tests
def test_is_gmail_backend_down():
  assert is_gmail_backend_down() == 0
def test_multiple_clients():
  assert multiple_clients_openURL() == 0

# FUNCTIONAL tests
def test_createAccount_openURL():
  assert validate_mainURL() == 0
def test_createAccount_nameFieldValidation():
  assert createAccount_nameFieldValidation() == 0
def test_birthdayGender():
  assert birthdayGender_inputValidation() == 0

