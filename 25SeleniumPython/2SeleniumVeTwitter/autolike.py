from selenium import webdriver
import time
import userInfo
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path=r'C:\Users\Burak\Desktop\geckodriver\geckodriver.exe')

browser.get("https://twitter.com/login")

time.sleep(3)

usernameInput = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")

passwordInput = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")

usernameInput.send_keys(userInfo.email)
passwordInput.send_keys(userInfo.password)

time.sleep(3)


login = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div")

login.click()

time.sleep(3)

searchArea = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input")


searchArea.send_keys("#atatürk")

searchArea.send_keys(Keys.ENTER)

time.sleep(5)
#birçok elemanı aynı anda çekmek için xpath mantıklı değil


lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True
time.sleep(5)


i = 0
while i < 500:
	try:
		liker = browser.find_element_by_css_selector("[data-testid=like]")
		liker.click()
		i += 1
	except:
		pass
 
browser.close()



