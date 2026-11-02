import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

def scrape_jobs():
    response = requests.get('https://realpython.github.io/fake-jobs')
    soup = BeautifulSoup(response.text, 'html.parser')
    
    jobs = []
    for card in soup.find_all('div', class_='card-content'):
        title = card.find('h2', class_='title').text.strip()
        company = card.find('h3', class_='company').text.strip()
        location = card.find('p', class_='location').text.strip()
        description = card.find('p', class_='').text.strip()
        link = card.find('a')['href']
        jobs.append((title, company, location, description, link))
    
    return jobs

def init_db():
    with sqlite3.connect('jobs.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS jobs 
                        (title TEXT, company TEXT, location TEXT, 
                         description TEXT, link TEXT, 
                         UNIQUE(title, company, location))''')

def update_jobs():
    jobs = scrape_jobs()
    
    with sqlite3.connect('jobs.db') as conn:
        c = conn.cursor()
        
        for job in jobs:
            c.execute('''SELECT description, link FROM jobs 
                        WHERE title=? AND company=? AND location=?''', job[:3])
            existing = c.fetchone()
            
            if existing:
                if existing != job[3:5]:
                    c.execute('''UPDATE jobs SET description=?, link=? 
                                WHERE title=? AND company=? AND location=?''',
                             (job[3], job[4], job[0], job[1], job[2]))
                    print(f"Updated: {job[0]}")
            else:
                c.execute('INSERT INTO jobs VALUES (?,?,?,?,?)', job)
                print(f"Added: {job[0]}")

def filter_jobs(location=None, company=None):
    with sqlite3.connect('jobs.db') as conn:
        c = conn.cursor()
        
        query = 'SELECT * FROM jobs WHERE 1=1'
        params = []
        
        if location:
            query += ' AND location LIKE ?'
            params.append(f'%{location}%')
        if company:
            query += ' AND company LIKE ?'
            params.append(f'%{company}%')
        
        return c.execute(query, params).fetchall()

def export_csv(filename, location=None, company=None):
    jobs = filter_jobs(location, company)
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Company', 'Location', 'Description', 'Link'])
        writer.writerows(jobs)

init_db()
update_jobs()
export_csv('filtered_jobs.csv', location='New York')