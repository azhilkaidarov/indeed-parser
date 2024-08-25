# Главный файл для запуска программы
from job_scraper import download_page
from job_parser import parse_title_page, parse_job_page
from storage.data_manager import export_to_excel
import os
import sys 


def main():
    #Ссылка на страницу с готовыми фильтрами (Skills: Python, SQL, Communicational skills; Exp: Mid Level; Where: United States; Dev type: Backed End Developers)
    url = (
        "https://www.indeed.com/jobs?q=python&l=United+States&sc=0kf%3Aattr"
        "%28FGY89%7CWSBNK%7CX62BT%252COR%29explvl%28MID_LEVEL%29occ%28EG6MP"
        "%29%3B&vjk=726e74519e47f031"
    )

    #По этому ссылке скачиваем html страничку с результатом запроса
    job_titles_page = download_page(url)   
    #Вытаскиваем все ссылки на отдельные страницы с вакансиями 
    job_urls = parse_title_page(job_titles_page)

    #Скачиваем все странички с вакансиями
    save_job_pages(job_urls)
    #Парсим каждую страничку и вытаскиваем нужную информацию
    save_job_data() 
    export_to_excel()


def save_job_pages(job_urls: list):
    """
    1.Эта функция сохраняет странички с вакансиями из главного запроса в indeed.
    2.Сохраняет каждую страничку в дочерней папке ./storage/pages 
    3.Каждой страничке выдается уникальный номер
    """
    if not job_urls:
        print("Не удалось получить ссылки на вакансии. Завершение работы.")
        sys.exit(1)  # Завершить выполнение программы с кодом ошибки 1

    file_name_counter = 1
    for link in job_urls:
        file_name = "indeed_job_"

        file_path = os.path.join("storage", "pages", f"{file_name}{file_name_counter}.html")
        file_name_counter += 1
        job_page = download_page(link)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(job_page)


def save_job_data():
    """
    1. Эта функция передает каждую сохраненный html файл в parse_job_page()
    """
    folder_path = os.path.join("storage", "pages")

    for file in os.listdir(folder_path):
        if file.endswith(".html"):
            file_path = os.path.join(folder_path, file)
            parse_job_page(file_path)


if __name__ == "__main__":
    main()