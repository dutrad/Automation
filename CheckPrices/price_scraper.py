import requests 
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from product import Product
from utils import convert_price_toNumber
import web_driver_conf
import time

def checkPrices():
    options = web_driver_conf.get_web_driver_options()
    web_driver_conf.set_ignore_certificate_error(options)
    web_driver_conf.set_browser_as_incognito(options)
    driver = web_driver_conf.get_chrome_web_driver(options)

    with open('products.json') as json_file:
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

        products.append(prod)

    driver.close()

    with open('products.json', 'w') as json_file:
        data = {}
        data["Products"] = []
        for prod in products:
            data["Products"].append(prod.serialize())
        json.dump(data, json_file, sort_keys=True, indent=4)

while True:
    checkPrices()
    time.sleep(60*60*10)
