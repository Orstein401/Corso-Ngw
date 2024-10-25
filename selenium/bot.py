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
 
API_TOKEN = '7979618656:AAFKKnrE_LKPRcRspIvldtQpUEpSsn6Iyzc'  # Inserisci il tuo token Telegram
bot = telebot.TeleBot(API_TOKEN)
 
# Percorso del driver di Chrome specifico
chrome_driver_path = r"C:\Users\alero\OneDrive\Desktop\chromedriver-win64\chromedriver.exe"
 
def search_amazon(nome):
    driver = init_driver()  # Inizializza il driver
    try:
        driver.get("https://www.amazon.it")
        time.sleep(2)  # Aspetta che la pagina si carichi

        # Trova il campo di ricerca e inserisci il prodotto
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        search_box.send_keys(nome)
        search_box.send_keys(Keys.RETURN)

        # Aspetta i risultati della ricerca
        time.sleep(3)  # Potresti usare WebDriverWait qui

        # Ottieni i prodotti
        products = []
        items = driver.find_elements(By.CSS_SELECTOR,'div.s-main-slot div.s-result-item')

        for item in items:
            title = item.find_element(By.CSS_SELECTOR,'h2.a-size-mini.a-spacing-none.a-color-base.s-line-clamp-4').text
            try:
                price = item.find_element(By.CSS_SELECTOR, 'span.a-price-whole').text
            except NoSuchElementException:
                price = "Prezzo non disponibile"

            products.append({"title": title, "price": price})

        return products
    except NoSuchElementException:
        logging.error("Il prodotto non è stato trovato")
    except ElementClickInterceptedException:
        logging.error("Il prodotto è atato blocatto.")
    except Exception as e:
        logging.error(f"Errore imprevisto: {str(e)}")
    finally:
        driver.quit()
# Funzione per avviarclse il driver di Selenium
def init_driver():
    service = Service(chrome_driver_path)
    options = Options()
    options.add_argument("--headless")  # Esegui il browser in modalità headless
    driver = Chrome(service=service, options=options)
    return driver

# Gestione dei comandi /start e /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Ciao! Inviami il nome di un prodotto da cercare su Amazon.")
 
# Gestione dei messaggi con testo
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    product_name = message.text
    bot.reply_to(message, f"Cerco '{product_name}' su Amazon, attendi...")
 
    # Esegui lo scraping su Amazon
    products = search_amazon(product_name)
 
    if products:
        for product in products:
            bot.send_message(message.chat.id, f"Prodotto: {product['title']}\nPrezzo: {product['price']} €")
    else:
        bot.send_message(message.chat.id, "Non ho trovato nessun prodotto corrispondente.")
 
# Funzione per eseguire il bot in un thread separato
def run_bot():
    bot.infinity_polling()
 
# Esegui il bot in un thread separato
threading.Thread(target=run_bot).start()