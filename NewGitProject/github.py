import sys
from selenium import webdriver
import time

user = 'dutrad.vinicius@gmail.com'

browser = webdriver.Chrome()
browser.get('https://github.com/login')

def login():
    #Fill username
    userField = browser.find_element_by_id('login_field')
    userField.send_keys(user)
    
    #Fill password
    password = str(sys.argv[2])
    passField = browser.find_element_by_id('password')
    passField.send_keys(password)

    #Login button
    button = browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[9]")
    button.click()

def create():    
    #New button
    newBtn = browser.find_element_by_xpath('//*[@id="repos-container"]/h2/a')
    newBtn.click()

    #Fill repository name
    projectName = str(sys.argv[1])
    repName = browser.find_element_by_id('repository_name')
    repName.send_keys(projectName)

    #Create button
    time.sleep(1)
    createBtn = browser.find_element_by_xpath('//*[@id="new_repository"]/div[3]/button')
    createBtn.click()

    browser.quit()

if __name__ == "__main__":
    login()
    create()

