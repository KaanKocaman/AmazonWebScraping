from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import csv
import shutil
web = "https://www.amazon.com.tr/s?rh=n%3A12601898031%2Cp_72%3A4-&content-id=amzn1.sym.ba2e439d-3464-4d0d-9a6b-476f2f9a8a48&pd_rd_r=453f1a05-e327-468b-95ea-fb8f6b9a77d8&pd_rd_w=6zcKR&pd_rd_wg=gUZNt&pf_rd_p=ba2e439d-3464-4d0d-9a6b-476f2f9a8a48&pf_rd_r=77CKT7RBJ2X3CMTANYAB&ref=Oct_d_otopr_S"
path = "C:\\Users\\Kanki\\Desktop\\Selenium\\chromedriver.exe"
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(web)
with open('input.csv', 'w', newline='',encoding="UTF-8") as file:
    writer = csv.writer(file)
    field = ["Marka","Urun_Ismi", "Fiyat"]
    writer.writerow(field)

while True:
    products = driver.find_elements(by="xpath", value='//div[contains(@class, "sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20")]')

    for product in products:
        product_names = product.find_element(by="xpath", value='.//span[contains(@class, "a-size-base-plus")]').text
        #ratings = product.find_element(by="xpath", value='.//span[contains(@class , "a-icon-alt")]').text
        marka = product_names.split(" ")[0].lower().capitalize()
        try:
            prices = product.find_element(by="xpath",value='.//span[contains(@class, "a-price-whole")]').text
        except:
            print("ürün bilgisi bulunamadı")
        else:
            if int(prices.replace(".","")) >= 6898:
                print(f'''Marka: {marka}
                        Ürün İsmi:{product_names}
                        Fiyatı:{prices} TL''')
                amazondata = {
                    "Marka": marka,
                    "Urun_Ismi": product_names,
                    "Fiyat": prices
                }
                with open('input.csv', 'a', newline='',encoding="UTF-8") as file:
                        writer = csv.writer(file)
                        writer.writerow([marka,product_names,prices])
    try:
        skill = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//a[contains(@class , "s-pagination-item s-pagination-next s-pagination-button s-pagination-separator")]')))
        driver.execute_script("arguments[0].click();" ,skill)
        time.sleep(5)
    except:
        driver.quit()
        break

with open('input.csv', newline='',encoding="UTF-8") as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

with open('AmazonVeri.json', 'w') as jsonfile:
    json.dump(data, jsonfile)

#shutil.move("C:\\Users\\Kanki\\Desktop\\Selenium\\AmazonVeri.json", "C:\\Users\\Kanki\\Desktop\\Flask\\AmazonVeri.json")