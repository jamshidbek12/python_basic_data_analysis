import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

class JobScraper:
    def __init__(self, db_name="jobs.db"):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            query = """
                CREATE TABLE IF NOT EXISTS jobs(
                    Job_title TEXT,
                    Company_name TEXT,
                    Location TEXT,
                    Job_description TEXT,
                    Application_link TEXT
                )
            """
            cursor.execute(query)

    def scrape_jobs(self):
        data = []
        url = 'https://realpython.github.io/fake-jobs'
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')

        card_contents = soup.findAll(class_='card')

        for card_content in card_contents:
            job = card_content.find('h2').text
            company = card_content.find('h3').text
            location = card_content.findAll(class_='location')[0].text.strip()
            description = card_content.findAll('a')[0]['href']
            apply = card_content.findAll('a')[1]['href']
            data.append({'Job_title': job, 'Company': company, 'Location': location, 'Description': description, 'Application_link': apply})
        return data

    def save_jobs(self, jobs_list):
        with sqlite3.connect('jobs.db') as conn:
            cursor = conn.cursor()

            for job in jobs_list:
                cursor.execute(
                    "SELECT Job_description, Application_link FROM jobs WHERE Job_title=? AND Company_name=? AND Location=?",
                    (job['Job_title'], job['Company'], job['Location'])
                )
                existing = cursor.fetchone()

                if existing is None:
                    cursor.execute(
                        "INSERT INTO jobs VALUES(?, ?, ?, ?, ?)", (
                            job['Job_title'], job['Company'], job['Location'], job['Description'], job['Application_link']
                        )
                    )
                else:
                    old_description, old_link = existing
                    if old_description != job['Description'] or old_link != job['Application_link']:
                        cursor.execute(
                            "UPDATE jobs SET Job_description=?, Application_link=? WHERE Job_title=? AND Company_name=? AND Location=?",
                            (job['Description'], job['Application_link'], job['Job_title'], job['Company'], job['Location'])
                        )


    def filter_jobs(self, location=None, company=None):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            if location:
                cursor.execute("SELECT * FROM jobs WHERE Location=?", (location,))
            elif company:
                 cursor.execute("SELECT * FROM jobs WHERE Company_name=?", (company,))
            else: 
                 cursor.execute("SELECT * FROM jobs")
            job_list = cursor.fetchall()
            self.export_to_csv(job_list)

    def export_to_csv(self, jobs_list, filename="filtered_jobs.csv"):
        with open(filename, 'wt', newline='') as file:
            writer = csv.writer(file)
            columns = ['Job_title', 'Company_name','Location', 'Job_description', 'Application_link']
            writer.writerow(columns)
            for row in jobs_list:
                writer.writerow([row[0], row[1], row[2], row[3], row[4]])
    def run(self):
        jobs = self.scrape_jobs()
        self.save_jobs(jobs)
        


scraper = JobScraper()
scraper.run()
scraper.filter_jobs(company='Mitchell, Jones and Olson')