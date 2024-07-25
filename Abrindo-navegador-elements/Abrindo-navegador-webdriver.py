from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time 


service = Service(executable_path="C:\webdriver\chromedriver-win64\chromedriver.exe")
navegador = webdriver.Chrome(service=service)
site = ("https://www.google.com/")
navegador.get(site)

elemen1 = navegador.find_element(By.CLASS_NAME, "gLFyf")
elemen1.send_keys("Leosim" + Keys.ENTER)




time.sleep(40)








