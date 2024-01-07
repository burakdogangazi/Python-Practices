from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import userInfo

browser  = webdriver.Firefox(executable_path=r'C:\Users\Burak\Desktop\geckodriver\geckodriver.exe')

browser.get("https://www.instagram.com/")

time.sleep(3)

usernameInput = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
passwordInput = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")


usernameInput.send_keys(userInfo.email)
passwordInput.send_keys(userInfo.password)

time.sleep(3)

login = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")


login.click()

time.sleep(5)




profilIconButton = browser.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div/div[1]/div/a")

profilIconButton.click()


time.sleep(5)


followerListButton = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")

followerListButton.click()

time.sleep(5)


jscommand = """


    followers = document.querySelector(".Igw0E.IwRSH.eGOV._vwCYk._3wFWr"")
    followers.scrollTo(0,followers.scrollHeight);
    var lenofPage = followers.scrollHeight;
    return lenOfPage;

"""

lenofPage = browser.execute_script(jscommand)


match = False

match = False

while(match == False):
    lastCount = lenofPage
    time.sleep(1)
    lenofPage = browser.execute_script(jscommand)
    if lastCount == lenofPage:
        match=True

time.sleep(5)

followersList = []
followers = browser.find_elements_by_css_selector(".FPmhX.notranslate.MBL3Z")

for follower in followers:

    followersList.append(follower.text)


with open("followers.txt","w",encoding="UTF-8") as file:
    for follower in followersList:
        file.write(follower +"\n")





