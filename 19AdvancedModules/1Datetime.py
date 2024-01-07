from datetime import date, datetime
import locale

locale.setlocale(locale.LC_ALL,"") # TÜRKÇE YAPTIK

# print(datetime.now())


şu_an = datetime.now()

# print(şu_an.year)#2021
# print(şu_an.month)
# print(şu_an.hour)

print(datetime.ctime(şu_an))# güzel bir gösterimle mevcutu söyler.

print(datetime.strftime(şu_an,"%Y"))
print(datetime.strftime(şu_an,"%M"))
print(datetime.strftime(şu_an,"%D"))
print(datetime.strftime(şu_an,"%B %Y"))

saniye = datetime.timestamp(şu_an)

şu_an2 = datetime.fromtimestamp(saniye)
print(şu_an2(datetime.strftime(şu_an,"%Y")))

şu_an2 = datetime.fromtimestamp(0) # 1970 milat olarak kabul edilir 0. saniye 1970-01-01 saat 03:00:00
# epoch time  


tarih = datetime(2019,12,1)

şu_an4 = datetime.now()

print(tarih - şu_an4)










