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
PATH = r"C:\Users\FedericaRizzo\Documents\Progetto_Sara\NGW 18+\doc_arpaLazio"
 
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
 
# Impostazione di un tempo di attesa per il caricamento della pagina
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
 
 
# Funzione per cliccare sul bottone "Ambiente"
def clicca_bottone_ambiente(driver):
    try:
        # Trova il bottone "Ambiente"
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button#Ambiente'))
        )
        # Forza il click con JavaScript
        driver.execute_script("arguments[0].click();", button)
        logging.info("Bottone 'Ambiente' cliccato con successo.")
    except NoSuchElementException:
        logging.error("Il bottone 'Ambiente' non è stato trovato.")
    except Exception as e:
        logging.error(f"Errore imprevisto: {str(e)}")
 
 
# Funzione per cliccare sul link "Open Data"
def clicca_link_open_data(driver):
    try:
        # Attendi che il link "Open Data" sia visibile
        link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[aria-label="Open Data"]'))
        )
        # Clicca sul link
        link.click()
        logging.info("Link 'Open Data' cliccato con successo.")
        # Attendi che la nuova pagina si carichi e accetta i cookie
        WebDriverWait(driver, 10).until(EC.title_contains("Open Data"))  # Attendere che il titolo della pagina indichi che siamo sulla pagina "Open Data"
        accetta_cookie(driver)  # Chiamata per accettare nuovamente i cookie
    except NoSuchElementException:
        logging.error("Il link 'Open Data' non è stato trovato.")
    except ElementClickInterceptedException:
        logging.error("Il click sul link 'Open Data' è stato bloccato.")
    except Exception as e:
        logging.error(f"Errore imprevisto: {str(e)}")
# Funzione per cliccare sul link "Dati della rete micrometeorologica" e accettare i cookie nella nuova pagina
def clicca_dati_rete_micrometeorologica(driver):
    try:
        # Attendi che il link "Dati della rete micrometeorologica" sia visibile
        link = WebDriverWait(driver, 10).until(
              EC.presence_of_element_located((By.CSS_SELECTOR, 'a[aria-label="Dati della rete micrometeorologica dell\'ARPA Lazio"]'))
)
 
        # Clicca sul link
        link.click()
        logging.info("Link 'Dati della rete micrometeorologica' cliccato con successo.")

    except NoSuchElementException:
        logging.error("Il link 'Dati della rete micrometeorologica' non è stato trovato.")
    except ElementClickInterceptedException:
        logging.error("Il click sul link 'Dati della rete micrometeorologica' è stato bloccato.")
    except Exception as e:
        logging.error(f"Errore imprevisto: {str(e)}", exc_info=True)
 
 
 
# Esegui le funzioni precedenti e scarica i documenti
accetta_cookie(driver)
clicca_bottone_ambiente(driver)
clicca_link_open_data(driver)
clicca_dati_rete_micrometeorologica(driver)
 
 
# Chiudi il browser al termine
driver.quit()