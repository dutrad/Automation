from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_chrome_web_driver(options):
    return webdriver.Chrome(chrome_options=options)

def get_web_driver_options():
    return webdriver.ChromeOptions()

def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')

def set_browser_as_incognito(options):
    options.add_argument('--incognito')

def set_automation_as_head_less(options):
    options.add_argument('--headless')

def set_no_sandbox(options):
    options.add_argument('--no-sandbox')

def disable_dev_shm_usage(options):
    options.add_argument('--disable-dev-shm-usage')

def set_all(options):
    set_automation_as_head_less(options)
    set_browser_as_incognito(options)
    set_ignore_certificate_error(options)
    set_no_sandbox(options)
    disable_dev_shm_usage(options)
