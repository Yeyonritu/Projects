import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSdBoFYZL5Zs9EYAPaPahXdsRVLanAfJjubGPK5OJrr1A-2uxw/viewform?usp=sf_link"
URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(URL)
webpage = response.text
# print(webpage)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

soup = BeautifulSoup(webpage, "html.parser")
rental_articles = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
addresses_articles = soup.find_all(name="address", attrs={'data-test': 'property-card-addr'})
rental_prices = []
article_links = []
addresses = []

for price in rental_articles:
    to_add = price.getText()[0:6]
    rental_prices.append(to_add)
    
for link in soup.find_all(name='a', class_="StyledPropertyCardDataArea-anchor"):
    article_links.append(link.get('href'))
    
for address in addresses_articles:
    to_add = address.getText().strip()
    addresses.append(to_add)
    
print(rental_prices)
print(article_links)
print(addresses)
    
for n in range(len(rental_prices)):
    
    driver.get(GOOGLE_FORM)
    sleep(5)
    
    address = driver.find_element(By.CLASS_NAME, value="whsOnd.zHQkBf")
    monthly_price = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_link = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.CLASS_NAME, value="l4V7wb.Fxmcue")
    next_form = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    
    address.send_keys(addresses[n])
    monthly_price.send_keys(rental_prices[n])
    property_link.send_keys(article_links[n])
    submit_button.click()
    # next_form.click()
    
# 
# for place in addresses:
#     sleep(5)
#     address.click()
#     address.clear()
#     address.send_keys(place)

# 
# for price in rental_prices:
#     sleep(5)
#     monthly_price.click()
#     monthly_price.clear()
#     monthly_price.send_keys(price)

# 
# for link in article_links:
#     sleep(5)
#     property_link.click()
#     property_link.clear()
#     property_link.send_keys(link)


    
    
    



    
    
    


