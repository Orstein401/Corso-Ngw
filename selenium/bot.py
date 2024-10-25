import telebot
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
import threading
 
# Configurazione del logger
logging.basicConfig(level=logging.INFO)
 
API_TOKEN = ''  # Inserisci il tuo token Telegram
bot = telebot.TeleBot(API_TOKEN)
 
# Percorso del driver di Chrome specifico
chrome_driver_path = r"C:\Users\FedericaRizzo\Documents\Progetto_Sara\NGW 18+\chromedriver-win64\chromedriver-win64\chromedriver.exe"
 
# Funzione per avviare il driver di Selenium
def init_driver():
    service = Service(chrome_driver_path)
    options = Options()
    options.add_argument("--headless")  # Esegui il browser in modalità headless
    driver = Chrome(service=service, options=options)
    return driver