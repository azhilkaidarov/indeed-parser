# Модуль для скачивания страниц вакансий
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from utils.constants import CHROME_BINARY_PATH, CHROME_DRIVER_PATH
import time
import sys

def download_page(url):

    if not CHROME_BINARY_PATH or not CHROME_DRIVER_PATH: 
        print(f"chrome или Chromedriver отсутсвтуют по указанному пути!\n"
              "Проверьте правильность пути в constansts.py!")
        sys.exit(1)

    # Настройка опций для Chrome
    options = webdriver.ChromeOptions()
    options.binary_location = CHROME_BINARY_PATH

    # Инициализация драйвера с использованием сервиса и опций
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)

    # Открываем веб-сайт
    driver.get(url)
    main_url = "https://www.indeed.com/jobs?q=python&l=United+States&sc=0kf%3Aattr%28FGY89%7CWSBNK%7CX62BT%252COR%29explvl%28MID_LEVEL%29occ%28EG6MP%29%3B&vjk=726e74519e47f031"
    
    if url != main_url:
        try: 
            print("-----------------------------ПЫТАЮСЬ НАЖАТЬ BENEFITS-------------------------------------")
            time.sleep(2)
            show_more_benefits_button = driver.find_element(By.XPATH, "//button[@data-testid='collapsedBenefitsButton']")
            show_more_benefits_button.click()

        except Exception as e:
            print(f'Не удалось найти "show more benefits" кнопку {e}')

        try: 
            print("-----------------------------ПЫТАЮСЬ НАЖАТЬ DESCRIPTION-------------------------------------")
            time.sleep(2)
            show_more_description_button = driver.find_element(By.XPATH, "//button[@data-testid='collapsedDescriptionButton']")
            show_more_description_button.click()

        except Exception as e:
            print(f'Не удалось найти "show more description" кнопку {e}')
        
    # Подождем немного, чтобы сайт успел загрузиться
    time.sleep(5)

    # Получаем HTML код страницы
    html_source = driver.page_source

    # Закрываем браузер
    driver.quit()
    
    return html_source 