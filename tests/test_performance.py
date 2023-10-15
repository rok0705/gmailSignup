import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver import Keys
from multiprocessing import Process, Pipe, Pool

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import multiprocessing
from threading import Thread

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def is_gmail_backend_down():
  driver.implicitly_wait(10)
  driver.get("https://accounts.google.com/signup")
  return 0
def multiple_clients_openURL():
  def gmailClient(number, result):
    driver = webdriver.Chrome()
    driver.get("https://accounts.google.com/signup")

    title = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/h1/span").text
    if title != "Create a Google Account":
      result[number] = "fail"
      return
    # tabs.
    for i in range(1,10):
      driver.execute_script("window.open('https://accounts.google.com/signup');")
      driver.switch_to.window(driver.window_handles[i])
      title = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/div/h1/span").text
      if title != "Create a Google Account":
        result[number] = "fail"
        return
      # print("checkup ",i," done.")

  number_of_clients = 10
  threads = []
  results = [""] * 10

  for number in range(number_of_clients):
    t = Thread(target=gmailClient, args=(number, results))
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
