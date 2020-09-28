import requests, json, os, time, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from product import Product
import web_driver_conf

sys.path.append(os.path.join(sys.path[0], "..", "SendEmail"))
from mail import sendMail

def checkPrices():
    driver = web_driver_conf.get_chrome_driver_with_options()

    jsonPath = os.path.join(os.path.dirname(__file__), 'products.json')
    with open(jsonPath) as json_file:
        data = json.load(json_file)

    prodList = data['Products']
    prod = Product("",0,0,"","")
    products = []

    for prodJson in prodList:
        prod.from_json(prodJson)
        driver.get(prod.link)
        element = driver.find_elements_by_class_name(prod.price_element)[0]
        prod.last_price = float(element.text.replace(',','.'))
        if(prod.last_price < prod.lowest_price):
            prod.lowest_price = prod.last_price
            sendMail(prod.name, "Novo preço: " + str(prod.last_price))

        products.append(prod)

    driver.close()

    with open(jsonPath, 'w') as json_file:
        data = {}
        data["Products"] = []
        for prod in products:
            data["Products"].append(prod.serialize())
        json.dump(data, json_file, sort_keys=True, indent=4)

while True:
    checkPrices()
    time.sleep(60*60*10)
