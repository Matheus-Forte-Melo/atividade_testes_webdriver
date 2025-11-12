# Equipe: Matheus Forte de Melo, Matheus Kuchenbecker, Luan ELizeu Santos, Willian Carlos Busch e Jefferson Machado

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://youtube.com") # Abrir o caminho no arquivo

time.sleep()

driver.quit()