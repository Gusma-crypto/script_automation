import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup konfigurasi logging
logging.basicConfig(
    filename="selenium_log.txt",  # Nama file log
    level=logging.INFO,  # Menentukan level log yang dicatat
    format="%(asctime)s - %(levelname)s - %(message)s",  # Format log
)

# Menambahkan log ketika program mulai
logging.info("Program dimulai.")

# Setup WebDriver dengan Service
service = Service(ChromeDriverManager().install())
webDrv = webdriver.Chrome(service=service)

try:
    logging.info("Membuka website https://www.example.com")
    webDrv.get("https://www.example.com")
    
    # Tunggu beberapa detik agar halaman sepenuhnya dimuat
    time.sleep(2)
    
    logging.info("Mencari tombol untuk diklik.")
    button = webDrv.find_element(By.ID, "submit_button")
    button.click()
    logging.info("Tombol berhasil diklik.")
    
    # Mengisi form
    logging.info("Mengisi form username.")
    username_field = webDrv.find_element(By.ID, "username")
    username_field.send_keys("my_username")
    
    logging.info("Mengisi form password.")
    password_field = webDrv.find_element(By.ID, "password")
    password_field.send_keys("my_password")
    
    logging.info("Form berhasil diisi.")
    
    # Tunggu beberapa detik agar form terisi
    time.sleep(2)

except Exception as e:
    logging.error(f"Terjadi error: {e}")

finally:
    logging.info("Menutup browser.")
    webDrv.quit()

# Log selesai
logging.info("Program selesai.")
