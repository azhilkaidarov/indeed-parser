# Модуль для хранения и обработки данных о вакансиях
class Job:
    def __init__(self, title, company_name, description, work_type, location = None, schedule = None, salary = None, benefits = None):
        self.title = title
        self.company_name = company_name
        self.location = location
        self.work_type = work_type
        self.schedule = schedule
        self.benefits = benefits
        self.description = description
        self.salary = salary
    
job_listings = []

def add_job(data: Job) -> None: 
    job_listings.append(data)