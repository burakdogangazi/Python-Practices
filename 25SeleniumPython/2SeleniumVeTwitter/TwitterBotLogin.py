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

tweets = []

elements = browser.find_elements_by_css_selector(".css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0")
#.css-901oao.r-18jsvk2.r-1qd0xha.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0 udemy yorum
#css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0 kendim

for element in elements:
    #  print("*******************************")
    #  print(element.text)
    tweets.append[element]







tweetCount = 1

with open("tweets.txt","w",encoding="UTF-8") as file:
    for tweet in tweets:
        file.write(str(tweetCount) + "\n" + tweet +"\n")
        file.write("****************************\n")
        tweetCount+=1




browser.back() # home sayfasına geri döner








