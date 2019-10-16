from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://www.vivaair.com/co/es/vuelo?DepartureCity=BOG&ArrivalCity=BAQ&DepartureDate=2019-10-25&Adults=1&Currency=COP"

# create a new Firefox session
driver = webdriver.Firefox(executable_path="/home/sebastian/Downloads/gecko/geckodriver", log_path="/home/sebastian/Downloads/gecko/geckodriver.log")
driver.implicitly_wait(30)
driver.get(url)

#python_button = driver.find_element_by_id('day selected') #FHSU
#python_button.click()

soup= BeautifulSoup(driver.page_source, 'lxml')

js = soup.findAll('div', class_="from-price")

print(js)

#Para que este codigo funcione hay que hacer un tema con el PATH de Firefox y tener instalado Selsnium
#Lo que hace es buscar todas las etiquetas from-price

