from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://localhost:8000/index.html")

driver.find_element(By.ID, "num1").send_keys("5")
driver.find_element(By.ID, "num2").send_keys("6")
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(1)
result = driver.find_element(By.ID, "result").text
print("Result on page:", result)
assert "30" in result

driver.quit()
