import requests

from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"

response = requests.get(url)

# print(response) # kontrol ettik response geldi

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")


a = float(input("Ratingi giriniz:"))

basliklar = soup.find_all("td",{"class":"titleColumn"})
ratingler = soup.find_all("td",{"class":"ratingColumn imdbRating"})

# for i in soup.find_all("td",{"class":"titleColumn"}):
#     print(i.text)
#     print("***********************************")

for baslik,rating in zip(basliklar,ratingler):
    
    baslik = baslik.text
    rating = rating.text
    baslik = baslik.strip()
    baslik = baslik.replace("\n","")
    rating = rating.strip()
    rating = rating.replace("\n","")
  
    if(float(rating)> a):
        print("Film ismi : {} Filmin Ratingi : {}".format(baslik,rating))














