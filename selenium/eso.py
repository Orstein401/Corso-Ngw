from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
import logging
import time
 
# Configurazione delogger
logging.basicConfig(level=logging.INFO)
 
# Percorso del driver di Chrome specifico
chrome_driver_path = r"C:\Users\alero\OneDrive\Desktop\chromedriver-win64\chromedriver.exe"
 
# Inizializzo il servizio con il percorso specifico del driver di Chrome
service = Service(chrome_driver_path)
 
# Inizializzo le opzioni del browser Chrome
options = Options()
 
# DIRECTORY DI DESTINAZIONE DEI FILE
PATH = r"C:\Users\alero\OneDrive\Desktop\selenium"
 
options.add_experimental_option("prefs", {
    "download.default_directory": PATH,
    "directory_upgrade": True,
    "profile.default_content_settings.popups": 0,
    "plugins.always_open_pdf_externally": True,
    "safebrowsing.enabled": True  # Abilita il safe browsing per evitare problemi con i download
})
 
# Avvio del driver di Chrome
driver = Chrome(service=service, options=options)
 
 
driver.get("https://www.arpalazio.it/")

driver.implicitly_wait(10)
 
def accetta_cookie(driver):
    try:
        # Attendi che l'elemento sia presente e cliccabile
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.acceptcookies"))
        ).click()
        logging.info("Cookie accettati con successo.")
    except NoSuchElementException:
        logging.error("Il bottone per accettare i cookie non è stato trovato.")
    except ElementClickInterceptedException:
        logging.error("Il click sul bottone dei cookie è stato bloccato.")
    except Exception as e:
        logging.error(f"Errore imprevisto: {str(e)}")


def clicca_bottone_servizio(driver):
    try:
        # Trova il bottone "Servizio"
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button#Servizi'))
        )
        # Forza il click con JavaScript
        driver.execute_script("arguments[0].click();", button)
        logging.info("Bottone 'Servizio' cliccato con successo.")
    except NoSuchElementException:
        logging.error("Il bottone 'Servizio' non è stato trovato.")
    except Exception as e:
        logging.error(f"Errore imprevisto: {str(e)}")



def clicca_link_tarrifario(driver):
    try:
        # Attendi che il link "Tariffario" sia visibile
        link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[aria-label="Tariffario"]'))
        )
        # Clicca sul link
        driver.execute_script("arguments[0].click();", link)
        # link.click()
        logging.info("Link 'Tariffario' cliccato con successo.")
        
        WebDriverWait(driver, 10).until(EC.title_contains("Tarrifario"))  # Attendere che il titolo della pagina indichi che siamo sulla pagina "tariffario"
        accetta_cookie(driver)  # Chiamata per accettare nuovamente i cookie
    except NoSuchElementException:
        logging.error("Il link 'Tariffario' non è stato trovato.")
    except ElementClickInterceptedException:
        logging.error("Il click sul link 'Tariffario' è stato bloccato.")
    except Exception as e:
        logging.error(f"Errore imprevisto: {str(e)}")


def scarica_file_tariffario(driver):
    try:
        # Attendi che il link "Dati della rete micrometeorologica" sia visibile
        links= WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'a')), )
    except NoSuchElementException:
        logging.error("link non trovato")
        for link in links:
            try:
                href=link.get_attribute('href')
                if href:
                    driver.execute_script("arguments[0].click();", href)
                    logging.info("Link cliccato con successo.")

            except NoSuchElementException:
             logging.error("link non trovato")
            except ElementClickInterceptedException:
             logging.error("link bloccato")
            except Exception as e:
             logging.error(f"Errore imprevisto: {str(e)}")
   
        
accetta_cookie(driver)
clicca_bottone_servizio(driver)
clicca_link_tarrifario(driver)
scarica_file_tariffario(driver)

driver.quit()