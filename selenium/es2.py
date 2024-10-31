from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from datetime import datetime
import logging
import time
import re

logging.basicConfig(level=logging.INFO)

chrome_driver_path = r"C:\Users\alero\OneDrive\Desktop\chromedriver-win64\chromedriver.exe"

service = Service(chrome_driver_path)

options = Options()

PATH = r"C:\Users\alero\OneDrive\Desktop\docu"

options.add_experimental_option("prefs", {
    "download.default_directory": PATH,
    "directory_upgrade": True,
    "profile.default_content_settings.popups": 0,
    "plugins.always_open_pdf_externally": True,
    "safebrowsing.enabled": True
})

# Avvio del driver di Chrome
driver = Chrome(service=service, options=options)

driver.get("https://www.albopretorionline.it/campania/alboente.aspx")

driver.implicitly_wait(10)

def click_cerca(driver):
    try:
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input#btCerca'))
        )
        driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        logging.info("Bottone 'Cerca' cliccato con successo.")
    except NoSuchElementException:
        logging.error("Il bottone 'Cerca' non è stato trovato.")
    except Exception as e:
        logging.error(f"Errore imprevisto: {str(e)}")


# def scarica_docu(driver):
#     try:
#         link= WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href*='download.aspx?ida=56318']"))
#         )
#         driver.execute_script("arguments[0].click();", link)
#         logging.info("Bottone 'link' cliccato con successo.")
#     except NoSuchElementException:
#         logging.error("Il bottone 'link' non è stato trovato.")
#     except ElementClickInterceptedException:
#          logging.error("Non è stato possibile cliccare sul link, potrebbe esserci un elemento sovrapposto.")
#     except Exception as e:
#         logging.error(f"Errore imprevisto: {str(e)}")

def scarica_docu(driver):
    try:
        div_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div#centercol"))
        )
        links = div_element.find_elements(By.TAG_NAME, 'a')
        dati = info_docu(driver)
        
        # Stampa le informazioni estratte
        for dato in dati:
            logging.info(dato)

        for i, link in enumerate(links):
            try:
                WebDriverWait(driver, 3).until(EC.element_to_be_clickable(link))
                link.click()
                logging.info(f"Link cliccato: {link.get_attribute('href')} num: {i + 1}")
                time.sleep(2) 
                # qui richiamo il div_element, perché riesco a scaricare solo 41 documenti anche se c'è ne sono altri, 
                # lo richiamo pensado magari che dopo il 41 link perde la conessione al div e facendo cosi lo ricoloco su esso
                div_element = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "div#centercol"))
                )
                links = div_element.find_elements(By.TAG_NAME, 'a')
            except ElementClickInterceptedException:
                logging.warning("Non è stato possibile cliccare sul link, potrebbe esserci un elemento sovrapposto.")
            except Exception as e:
                logging.error(f"Errore durante il clic sul link: {str(e)}")
        
    except NoSuchElementException:
        logging.error("Il 'div' non è stato trovato.")
    except Exception as e:
        logging.error(f"Errore imprevisto: {str(e)}")

def info_docu(driver):
    try:
        data_docu = []
        div_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div#centercol"))
        )
        dati = div_element.find_elements(By.TAG_NAME, 'li')
        links = div_element.find_elements(By.TAG_NAME, 'a')
        
        for dato in dati:
            element_info = {}
            text = dato.text
            match = re.findall(r'\d{2}-\d{2}-\d{4}', text)

            if match and len(match) == 2:
                data_inizio, data_fine = match
                element_info['data_inizio'] = data_inizio
                element_info['data_fine'] = data_fine

            match = re.search(r'Proc\.\s*(\d{3})', text)
            if match:
                num_atto = match.group(1)  
                element_info['num_atto'] = num_atto
            
            for link in links:
                nome_docu = link.text
                if nome_docu:
                    element_info['nome_docu'] = nome_docu
                
                href = link.get_attribute('href')
                if href:
                    element_info['link'] = href
            
            data_download = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
            element_info['data_download'] = data_download
            
            if element_info:  
                data_docu.append(element_info)
        
        return data_docu  

    except NoSuchElementException:
        logging.error("Il 'div' non è stato trovato.")
    except Exception as e:
        logging.error(f"Errore imprevisto: {str(e)}")

click_cerca(driver)
scarica_docu(driver)
driver.quit()
