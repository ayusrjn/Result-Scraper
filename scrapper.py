from selenium import webdriver
import time
import os
import csv
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys


def scrapping_result(reg_no):
    
    edge_driver_path = "C:\\Users\\ayush\\Downloads\\edgedriver_win64\\msedgedriver.exe"

    
    service = Service(edge_driver_path)
    options = Options()
    options.use_chromium = True
    driver = webdriver.Edge(service=service, options=options)

    
    driver.get("http://results.beup.ac.in/BTech1stSem2023_B2023Results.aspx")

    
    textbox = driver.find_element(By.ID, "ContentPlaceHolder1_TextBox_RegNo")
    registration_number = reg_no
    textbox.send_keys(registration_number)
    textbox.send_keys(Keys.ENTER)

    
    time.sleep(2)

    
    student_name_element = driver.find_element(By.ID, "ContentPlaceHolder1_DataList1_StudentNameLabel_0")
    student_name = student_name_element.text.strip()

    
    table = driver.find_element(By.ID, "ContentPlaceHolder1_GridView1")

    
    rows = table.find_elements(By.TAG_NAME, "tr")[1:]

    
    csv_file_path = 'scraped_data_EEE.csv'
    file_exists = os.path.exists(csv_file_path)

    
    with open(csv_file_path, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["REGISTRATION", "NAME", "Chemistry", "PPS", "WMP", "English", "Mathematics I"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists or os.stat(csv_file_path).st_size == 0:
            writer.writeheader()

        subject_to_column = {
            "CHEMISTRY": "Chemistry",
            "PROGRAMMING FOR PROBLEM SOLVING": "PPS",
            "WORKSHOP MANUFACTURING PRACTICES": "WMP",
            "ENGLISH": "English",
            "MATHEMATICS - I (CALCULUS AND LINEAR ALGEBRA)": "Mathematics I"
        }

        row_data = {"REGISTRATION": registration_number, "NAME": student_name}

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) > 0:
                subject_name = cells[1].text.strip()
                total = cells[4].text.strip()

                if subject_name in subject_to_column:
                    column_name = subject_to_column[subject_name]
                    row_data[column_name] = total

        writer.writerow(row_data)

    driver.quit()


for i in range(1,61, 1):
    scrapping_result(23101126000 + i )

