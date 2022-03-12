# This scirpt scrape the job title, company name, salay and job summary from the indeed.co.uk webiste for python devloper position.
# Results are appended to the lists and saved to csv file as pandas data frame. 

import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
    url = f'https://uk.indeed.com/jobs?q=python+developer&start={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = 'job_seen_beacon')
    for item in divs:
        job_title = item.find('h2', class_ = 'jobTitle').text.strip()
        company_name = item.find('span', class_ = 'companyName').text.strip()
        try:
            salary = item.find('div', class_ = 'salary-snippet').text.strip()
        except:
            salary = ''
        summary = item.find('div', class_ = 'job-snippet').text.strip().replace('\n', '')
        
        job = {
            'title': job_title,
            'company': company_name,
            'salary': salary,
            'summary': summary
        }
        joblist.append(job)
    return
   
joblist = []   

# change second value in 'range' below to scrape different number of sites
for i in range(0, 10):
    print(f'Getting page, {i}')
    c = extract(0)
    transform(c)

df = pd.DataFrame(joblist)
print(df.head())
df.to_csv('indeed_jobs_10_pages.csv')

