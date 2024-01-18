import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def  wait_and_click(driver, by, value):
    element = WebDriverWait(driver, 10). until(EC.element_to_be_clickable((by, value)))
    element.click()

def scrape_and_write_to_excel(url, filter_id, sheet_name, min_value, max_value):
    service = Service()
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=option)

    try:
        driver.get(url)
        wait_and_click(driver, By.ID, "mtd_97")
        wait_and_click(driver, By.ID, filter_id)

        driver.find_element(By.ID,"f_o_8_min").send_keys(min_value)
        driver.find_element(By.ID,"f_o_8_max").send_keys(max_value)
        driver.find_element(By.ID,"f_o_18_min").send_keys(2017)
        driver.find_element(By.ID,"f_o_18_max").send_keys(2023)
        driver.find_element(By.ID,"f_o_15_max").send_keys(1.2)

        data = []
        tbody = driver.find_element(By.XPATH, '//*[@id="filter_frm"]/table[2]/tbody')
        for tr in tbody.find_elements(By.XPATH,'//tr' ):
            row = [item.text for item in tr.find_elements(By.XPATH, './/td')]
            data.append(row)

        df = pd.DataFrame (data[4:])
        for row in range(1, len(df)):
            for col in range (2, len(df.columns)):
                df.iloc[row, col - 2] = df.iloc[row, col]
        df = df.iloc[:, :-2]
        excel_filename="projekts.xlsx"

        if not os.path.isfile(excel_filename):
            df.to_excel(excel_filename, index=False, header=False, sheet_name=sheet_name, startrow=1)
        else:
            with pd.ExcelWriter(excel_filename, engine='openpyxl', mode='a') as writer:
                df.to_excel(writer, sheet_name=sheet_name, index=False, header=False, startrow=1)

        print(f"dati ir veiksmīki ielikti {excel_filename}, Sheet: {sheet_name}")

    finally:
            driver.quite()

def scrape_and_write_for_car_brands():
    firmas = [
        ("ahc_112","Citroen" ),
        ("ahc_75068", "Dacia"),
        ("ahc_120", "Ford"),
        ("ahc_123", "Honda"),
        ("ahc_129", "Kia"),
        ("ahc_139", "Mazda"),
        ("ahc_140", "Mercedes"),
        ("ahc_146", "Nissan"),
        ("ahc_153", "Renault"),
        ("ahc_158", "Skoda"),
        ("ahc_159", "Subaru"),
        ("ahc_164", "Toyota"),
        ("ahc_167", "Volvo"),
    ]

    for filter_id, sheet_name in  firmas:
       scrape_and_write_to_excel ("https://www.ss.com/lv/", filter_id, sheet_name, 8000, 12000)

scrape_and_write_for_car_brands()