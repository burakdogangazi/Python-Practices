from selenium import webdriver
import time
import random

browser = webdriver.Firefox(executable_path=r'C:\Users\Burak\Desktop\geckodriver\geckodriver.exe')

#'C:\Program Files'
# executable_path=r'C:\Users\Burak\Desktop\geckodriver\geckodriver.exe'

url  = "https://eksisozluk.com/mustafa-kemal-ataturk--34712"

browser.get(url)

time.sleep(5) # sayfayı 5 saniye beklettik

elements = browser.find_elements_by_css_selector(".content") # sitede entrylerin content içinde olduğunu gördük ve aldık

for element in elements:

    print("*************************************")
    print(element.text)


browser.close()







