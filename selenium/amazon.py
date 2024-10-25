from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
 
# Configurazione del logger
logging.basicConfig(level=logging.INFO)
 
# Percorso del driver di Chrome specifico
chrome_driver_path = r"C:\Users\alero\OneDrive\Desktop\chromedriver-win64\chromedriver.exe"
 
# Inizializzo il servizio con il percorso specifico del driver di Chrome
service = Service(chrome_driver_path)
 
# Inizializzo le opzioni del browser Chrome
options = Options()
 
# Avvio del driver di Chrome
driver = Chrome(service=service, options=options)
 
# Vai alla pagina di Amazon
driver.get("https://www.amazon.it/?tag=wwwbingcom07-21&ref=pd_sl_8nrp9peygk_e&adgrpid=1227055293731746&hvadid=76691120301091&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy=1821&hvtargid=kwd-76691194887418:loc-93&hydadcr=10840_1834685&msclkid=bb314bc0081b135719c42cc4d7ac79d1")
 
time.sleep(2)

def accetta_cookie(driver):
    try:
    
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input#sp-cc-accept"))
        ).click()
        logging.info("Cookie accettati con successo.")
    except NoSuchElementException:
        logging.error("Il bottone per accettare i cookie non è stato trovato.")
    except ElementClickInterceptedException:
        logging.error("Il click sul bottone dei cookie è stato bloccato.")
    except Exception as e:
        logging.error(f"Errore imprevisto: {str(e)}")

def ricerca(driver):
    try:
        cerca= WebDriverWait(driver, 10).until(
          EC.presence_of_element_located((By.CSS_SELECTOR, 'input#twotabsearchtextbox'))
        )
        cerca.send_keys("gormiti")
        cerca.send_keys(Keys.RETURN)
        logging.info("Inviato con sucesso")
        time.sleep(2)
        accetta_cookie(driver)

    except NoSuchElementException:
            logging.error("Non trovato il tasto ricerca")
    except ElementClickInterceptedException:
            logging.error("bloccato il tasto ricerca")
    except Exception as e:
            logging.error(f"Errore imprevisto: {str(e)}")

def stampa(driver):
     try:

          testi=WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span.a-size-base-plus.a-color-base.a-text-normal'))
          )
         
          for testo in testi:
             print(testo.text)
          logging.info("Stampato con sucesso")

     except NoSuchElementException:
            logging.error("Non trovato il Testo ricerca")
     except ElementClickInterceptedException:
            logging.error("bloccato il testo ricerca")
     except Exception as e:
            logging.error(f"Errore imprevisto: {str(e)}")


accetta_cookie(driver)
ricerca(driver)
time.sleep(2)
stampa(driver)
driver.quit()