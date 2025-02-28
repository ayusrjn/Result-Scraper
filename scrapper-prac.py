import time
import os

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def scrapper():
    path_to_driver = "C:\\Users\\ayush\\Downloads\\edgedriver_win64\\msedgedriver.exe"
    service = Service(path_to_driver)
    options = Options()

    driver = webdriver.Edge(service= service, options=options)

    driver.get("https://acadsphere.in/user/register")

    # text_field = driver.find_element(By.CLASS_NAME, "gLFyf")
    # search_query = "hi this a automated test"
    # text_field.send_keys(search_query)
    # text_field.send_keys(Keys.ENTER)
    name_field = driver.find_element(By.NAME, "name")
    name_field.send_keys("HI MF")

    email_field = driver.find_element(By.NAME, "email")
    email_field.send_keys("motherfucker@gmail.com")

    college_field = driver.find_element(By.NAME, "college")
    college_select = Select(college_field)
    college_select.select_by_index(1)

    sem_field = driver.find_element(By.NAME, "semester")
    sem_f = Select(sem_field)
    sem_f.select_by_index(1)

    branch_field = driver.find_element(By.NAME, "branch")
    branch_f = Select(branch_field)
    branch_f.select_by_index(1)

    passwrd = driver.find_element(By.NAME, "password")
    passwrd.send_keys("ThisIs@012")
    con_pass = driver.find_element(By.NAME, "confirmPassword")
    con_pass.send_keys("ThisIs@012")
    con_pass.send_keys(Keys.ENTER)


    time.sleep(5)

    driver.quit()
while(1):
    scrapper()