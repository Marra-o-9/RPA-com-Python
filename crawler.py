from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time

# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver = webdriver.Firefox()

url = driver.get("http://www.imdb.com/")
driver.get(url)

time.sleep(5)

queryBox = driver.find_element(By.ID, "suggestion-search")
queryBox.send_keys("Homem-Aranha")
queryBox.send_keys(Keys.RETURN)
