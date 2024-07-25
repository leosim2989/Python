from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time 


service = Service(executable_path="C:\webdriver\chromedriver-win64\chromedriver.exe")
navegador = webdriver.Chrome(service=service)
site = ("https://web.whatsapp.com/")
navegador.get(site)
time.sleep(60)




contato = ['Amor','junior']

#Procurar contato no buscar
elemen1 = navegador.find_element(By.CLASS_NAME,"selectable-text")
elemen1.send_keys(contato + Keys.ENTER)
time.sleep(3)

#Selecionar conversa
elemen2 = navegador.find_element(By.CLASS_NAME,"_ak1l")
elemen2.click()
mensagem = "Mensagem automatica"
elemen2.send_keys(mensagem)
time.sleep (10)

#Enviar conversa 
elemen3 = navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()

#Envia mensagem 
time.sleep(40)


