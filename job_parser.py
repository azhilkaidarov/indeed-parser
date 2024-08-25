# Модуль для парсинга страниц с вакансиями
from bs4 import BeautifulSoup
from job_data import Job, add_job
from storage.data_manager import export_to_excel
import os
def parse_title_page(html_source):

    soup = BeautifulSoup(html_source, "html.parser")
    soup.prettify()

    job_urls = []
    job_titles = soup.find_all("a" , {"class" : "jcs-JobTitle css-jspxzf eu4oa1w0"})

    for item in job_titles:
        item_url = item.get("href")
        job_urls.append("https://indeed.com/" + item_url)
    
    return job_urls

def parse_job_title(soup):
    title_tag = soup.find("h1", class_ = "jobsearch-JobInfoHeader-title css-1b4cr5z e1tiznh50")
    return title_tag.get_text(strip = True) if title_tag else "Null"

def parse_company_name(soup):
    name_tag = soup.find("a", class_ = "css-1ioi40n e19afand0")
    return name_tag.get_text(strip = True) if name_tag else "Null"

def parse_address(soup):
    adress_tag = soup.find("div", class_ = "css-1ojh0uo eu4oa1w0")
    return adress_tag.get_text(strip = True) if adress_tag else "Null"

def parse_work_type(soup):
    work_type_tag = soup.find("div", class_ = "css-17cdm7w eu4oa1w0")
    return work_type_tag.get_text(strip = True) if work_type_tag else "Null"

def parse_salary(soup):
    salary_tag = soup.find("span", class_ = "css-19j1a75 eu4oa1w0")
    return salary_tag.get_text(strip = True) if salary_tag else "Null"

def parse_schedule(soup):
    schedule_tag = soup.find("span", class_ = "css-k5flys eu4oa1w0")
    return schedule_tag.get_text(strip = True) if schedule_tag else "Null"

def parse_description(soup):
    description_tag = soup.find("div", class_ = "jobsearch-JobComponent-description css-16y4thd eu4oa1w0")
    all_description = [description.getText() for description in description_tag]
    result = '\n'.join(item.strip() for item in all_description)

    return result if result else "Null"

def parse_benefits(soup):
    benefits_tag = soup.find_all("li", class_="css-kyg8or eu4oa1w0")
    all_benefits = [benefit.getText() for benefit in benefits_tag]

    if all_benefits:
        result = '\n'.join(item.strip() for item in all_benefits)
        return result
    return "Null"

def parse_job_page(html_file = "indeed_job_№2.html"):
    with open(html_file, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    title = parse_job_title(soup)
    company_name = parse_company_name(soup)
    location = parse_address(soup)
    work_type = parse_work_type(soup)
    salary = parse_salary(soup)
    schedule = parse_schedule(soup)
    benefits = parse_benefits(soup)
    description = parse_description(soup)
    
    test = Job(title=title, 
               company_name=company_name,
               description=description,
               work_type=work_type,
               location=location,
               schedule=schedule,
               salary=salary,
               benefits=benefits)
    add_job(test)

    """
    1. Job title <h1 class = jobsearch-JobInfoHeader-title css-1b4cr5z e1tiznh50
    2. Company name <a class = css-1ioi40n e19afand0
    3. Adress (optional) <div class = css-1ojh0uo eu4oa1w0
    4. Work type personal/hybrid/remote <div class = css-17cdm7w eu4oa1w0
    5. Salary (optional) <span class = css-19j1a75 eu4oa1w0
    6. Work schedule (optional) fulltime/part-time/else <span class = css-k5flys eu4oa1w0
    7. Benefits (optional) <div class = css-eynugf eu4oa1w0
    8. Description <div class = jobsearch-JobComponent-description css-16y4thd eu4oa1w0
    """



