

'''This script was designed to pull in court records from Santa Clara County, 
but it can also work for other court systems. I used this to cross reference lump 
files of business listings or name databases to see which parties had recent court 
cases.'''

from bs4 import BeautifulSoup
import csv
import selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import urllib.parse
import openpyxl
import pandas as pd

wb = openpyxl.Workbook()

with open('{file of search queries}') as csvfile:
    reader = csv.reader(csvfile)

    next(reader)
    data = []
    for row in reader:
        data.append(row[1])

    strip_list = [urllib.parse.quote(item.strip()) for item in data]

driver = webdriver.Chrome()
i = 0
d = []
for item in strip_list:
    i += 1
    print(item)
    driver.get('https://portal.scscourt.org/search/business?businessName='+ item)
    timeout = 10
    try:
        element_present = EC.presence_of_element_located((By.TAG_NAME, 'td'))
        WebDriverWait(driver, timeout).until(element_present)
    except:
        print('Timed out waiting for page to load')
        continue
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    tables = soup.find_all('td')
#    row = []

    if 'dataTables_empty' in str(tables):
        continue
    else:
        print(tables)
        d.append({'Case Number': tables[1].text, 'Case Style': tables[2].text,
        'Case Status': tables[3].text, 'Case Type': tables[4].text, 'Filing Date': tables[5].text})

PandaMap = pd.DataFrame(d)
PandaMap.to_excel('wb.xlsx', index = None, header=True)

print(PandaMap)




