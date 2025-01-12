import time
from selenium import webdriver
from selenium.webdriver.common.by import By


''' A Selenium Powered Web Scraper that enables me to scrape a used-cars website and scrape all the info from them: e.g. petrol amount, engine, model, etc..'''

driver = webdriver.Chrome('chrome-linux64') # Opens chrome - powered by linux because im awesome - i dont know my pathway to chrome driver, so i let it search for it manually, if i add the pathway it would open faster..
driver.get('https://www.carwow.co.uk/used-cars') # Carwow is the website im scraping
time.sleep(3) # Let the user actually see something! - dont close chrome too fast
driver.execute_script(" window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' })", "")
time.sleep(3)


# finds the general class (BY classname) that holds all the info as named below
my_variable = driver.find_elements(By.CLASS_NAME, "card-generic__ctas") 

''' This scrapes all the links of the 12 cars on the first page of the website '''
links = []

for linkWrapper in my_variable:
    links.append(linkWrapper.find_element(By.TAG_NAME, "a").get_attribute("href"))

print(links)

    
time.sleep(5) # add a breakpoint here and 'Run and Debug' - will enable you to run commands in the terminal (examples below) and Chrome wont close
driver.quit()






''' Some example commands you can run in the terminal to serach for desired items. '''
# - driver.find_element(By.ID, "fruits")
# - my_variable.get_attribute('innerHTML')
# element.get_attribute('innerHTML') -  returns inner html contents
# my_variable.get_attribute("href") - return href attribute 
# my_variable.text  - return text
# driver.find_element(By.CLASS_NAME, "name_of_my_class")  - find single element, error if doesn't find
# driver.find_elements(By.CLASS_NAME, "name_of_my_class") - find mulitple element, puts them in a list. empty list if no element found
