import requests
from bs4 import BeautifulSoup # web sayfası içinde div vb blokları alabiliriz bu ile

#Kurulum

# pip3 install requests
# pip3 install beautifulsoup4 termianlden indir
# web sayfasından veri almada kullanılır


url = "https://yellowpages.com.tr/ara?q=ankara"
response = requests.get(url)
# resposne503 dedi ulaşabildik
# print(response)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")


# print(soup.find_all("a")) # a etiketlerini olduğu bir liste döndürür

for i in soup.find_all("a"):
    # print(i)
    print(i.get("href"))
    # print(i.text)
    print("******************************")

print(soup.find_all("div",{"class":"yp-poi-box-2"})) # tüm div etiketleri gelmesin








