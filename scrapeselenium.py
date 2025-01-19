import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)
driver.get("https://www.carwow.co.uk/used-cars")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "card-genericctas")))
driver.execute_script("window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' })")

time.sleep(random.uniform(2, 5))

link_wrappers = driver.find_elements(By.CLASS_NAME, "card-genericctas")
links = [wrapper.find_element(By.TAG_NAME, "a").get_attribute("href") for wrapper in link_wrappers]

print(links)

def scrape_one_car(link):
    print(f"Scraping {link}")
    driver.get(link)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "deal-titlemodel")))
    model = driver.find_element(By.CLASS_NAME, "deal-titlemodel").text

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "summary-listitem")))
    summary_items = driver.find_elements(By.CLASS_NAME, "summary-listitem")

    summary_info = {}
    for item in summary_items:
        key = item.find_element(By.TAG_NAME, "dt").text
        value = item.find_element(By.TAG_NAME, "dd").text
        summary_info[key] = value

    car_details = {
        "model": model,
        "summary_info": summary_info
    }
    return car_details

if links:
    car_details = scrape_one_car(links[0])
    print(car_details)

driver.quit()




# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# import random
# #from webdriver_manager.chrome import ChromeDriverManager



# options = Options()
# options.headless = True


# ''' A Selenium Powered Web Scraper that enables me to scrape a used-cars website and scrape all the info from them: e.g. petrol amount, engine, model, etc..'''

# driver = webdriver.Chrome(options=options) # Opens chrome - powered by linux because im awesome - i dont know my pathway to chrome driver, so i let it search for it manually, if i add the pathway it would open faster..
# driver.get("https://www.carwow.co.uk/used-cars") # Carwow/used-cars is the website im scraping - will move deeper
# time.sleep(random.uniform(2, 5)) # Let the user actually see something! - dont close chrome too fast
# driver.execute_script(" window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' })", "")
# time.sleep(random.uniform(2, 5))


# # finds the general class (BY classname) that holds all the info as named below
# my_variable = driver.find_elements(By.CLASS_NAME, "card-generic__ctas") 
# # submit_button = driver.find_element(By.ID, "accept")

# # submit_button.click()

# ''' This scrapes all the links of the 12 cars on the first page of the website '''
# links = []

# for linkWrapper in my_variable:
#     links.append(linkWrapper.find_element(By.TAG_NAME, "a").get_attribute("href"))

# print(links)

    
# time.sleep(random.uniform(2, 5)) # add a breakpoint here and 'Run and Debug' - will enable you to run commands in the terminal (examples below) and Chrome wont close

# cars = []

# summaryinfo = []




# def scrape_one_car(link):
#     print(link)
#     driver.get(link)
#     namodel = driver.find_elements(By.CLASS_NAME, "deal-title__model")
#     addmod = {"model": namodel}
#     cars.append(addmod)
#     summaryinfo = driver.find_elements(By.CLASS_NAME, "summary-list__item")
#     for item in summaryinfo:
#         summaryinfo.append(item.find_element(By.TAG_NAME, "dt"))



# print(cars)
# print(summaryinfo)
# scrape_one_car(links[0])

# driver.quit()


# ''' Some example commands you can run in the terminal to serach for desired items. '''
# # - driver.find_element(By.ID, "fruits")
# # - my_variable.get_attribute('innerHTML')
# # element.get_attribute('innerHTML') -  returns inner html contents
# # my_variable.get_attribute("href") - return href attribute 
# # my_variable.text  - return text
# # driver.find_element(By.CLASS_NAME, "name_of_my_class")  - find single element, error if doesn't find
# # driver.find_elements(By.CLASS_NAME, "name_of_my_class") - find mulitple element, puts them in a list. empty list if no element found
