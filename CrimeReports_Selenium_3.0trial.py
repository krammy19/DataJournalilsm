#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      m_noa
#
# Created:     06/01/2020
# Copyright:   (c) m_noa 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pandas as pd
import csv
import selenium
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

SW = [37.361382, -122.120128]
NW = [37.438523, -122.112426]
NE = [37.434297, -122.045907]
SE = [37.357926, -122.045564]

def Coordinates_check(start, end):
    if start > end:
        print('its over!')
        return False
    else:
        return True

SW_Start = SW[0]
driver = webdriver.Chrome()
driver.maximize_window()
toUpdateDate = 'toUpdateDate=12%2F30%2F2019'
fromUpdateDate ='&fromUpdateDate=12%2F20%2F2019'

#f = open("C:\\Users\\m_noa\\Documents\\Journalism\\crime_reports.csv", "a", newline='')
#writer = csv.writer(f)
#writer.writerow(["incidents", "time", "date", "address", "agency", "description", "coordinates"])

j = 1
x = 0
y = 0
actions = ActionChains(driver)
total = 0

while Coordinates_check(SW[1], NE[1]):
    print('total boxes:', j)
    driver.get(''.join(['https://www.cityprotect.com/map/list/incidents?',
toUpdateDate, fromUpdateDate,
'&pageSize=2000&parentIncidentTypeIds=149,150,148,8,97,104,165,98,100,179,178,180,101,99,103,163,168,166,12,161,14,16,15&zoomLevel=16&latitude='
, str(SW[0]), '&longitude=', str(SW[1]),
'&days=1,2,3,4,5,6,7&startHour=0&endHour=24&timezone=-08:00']))
    try:
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "incident-case-number")))
    except:
        print('Timed out waiting for page to load')
    time.sleep(5)
    ID_element = driver.find_element_by_id(('incidentsList'))
    actions.double_click(ID_element)
    actions.key_down(u'\ue010')
    actions.perform()
#    time.sleep(1)

#    actions.key_up(u'\ue010').perform()

    incidents = [el.text for el in driver.find_elements_by_id(("incident-case-number"))]
    hour = [el.text for el in driver.find_elements_by_id(("incident-time"))]
    date = [el.text for el in driver.find_elements_by_id(("incident-date"))]
    address = [el.text for el in driver.find_elements_by_id(("incident-address"))]
    agency = [el.text for el in driver.find_elements_by_id(("incident-agency"))]
    description = [el.text for el in driver.find_elements_by_id(("incident-description"))]
    j += 1
    i = 0
    while i < len(incidents):
        writing = [incidents[i], hour[i], date[i], address[i], agency[i], description[i], (str(SW[0]) + ', ' + str(SW[1])), '\n']
        for item in writing:
            print(item)
#        f.flush()
        i += 1
    print('coordinates:', SW[0], ", ", SW[1])
    print('grid: ', x, ", ", y)
    print("number of incidents:", len(incidents))
    total += len(incidents)
    print('total incidents:', total)
    y += 1
    SW[0] += 0.0095
    if j == 3: break
    if SW[0] > NW[0]:
        SW[0] = SW_Start
        y = 0
        SW[1] += 0.018
        x += 1
#    print('new coordinates:', SW[0], ", ", SW[1])


