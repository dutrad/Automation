import sys
import getpass
from selenium import webdriver

user = 'dutrad.vinicius@gmail.com'

browser = webdriver.Chrome()
browser.get('https://github.com/login')

def login():
    userField = browser.find_element_by_id('login_field')
    userField.send_keys(user)
    
    password = getpass.getpass('Password:')
    passField = browser.find_element_by_id('password')
    passField.send_keys(password)

    button = browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[9]")
    button.click()

def create():
    login()
    
    newBtn = browser.find_element_by_xpath('//*[@id="repos-container"]/h2/a')
    newBtn.click()

    projectName = str(sys.argv[1])
    repName = browser.find_elements_by_id('repository_name')
    repName.send_keys(projectName)

    createBtn = browser.find_element_by_xpath('//*[@id="new_repository"]/div[3]/button')
    createBtn.click()
    

if __name__ == "__main__":
    create()

