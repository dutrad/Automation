import sys
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://github.com/login')

def create():
    projectName = str(sys.argv[1])
    print(projectName)
    button = browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[9]")
    button.click()

if __name__ == "__main__":
    create()

