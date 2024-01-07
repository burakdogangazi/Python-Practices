"python".upper()
"PYTHON".lower()

"merhaba benim adım burak doğan".replace("a","o")
# a yı kaldırır o yu koyar 

"Python Programlama Dili".replace(" ","-")

"Kunduz".replace("duz","zun")

"Pyton".startswith("p")
#false döner büyük p ile başlıyor çünkü

"Python".endswith("on")
# true

liste ="Python Programlama Dili".split(" ")
# liste yapar her boşluğa kadar bir değere kadar koyarak


"         python          ".strip()
#başındaki ve sonundaki boşlukları sildi
"         python          ".lstrip()# soldakileri siler
"         python          ".rstrip()# sağdakileri siler

">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Python<<<<<<<<<<<<<<<<<<<<<<".strip(">")
# >>>> siler


liste = ["21","02","2014"]

"/".join(liste)
# listenin her birinin arasına / koyar 21/02/2014

liste2 = ["T","B","M","M"]

".".join(liste2)


"ada kapası yandan çarklı".count("a")# 6 kere geçer 6 döner
"ada kapası yandan çarklı".count("a",2)# 2. indeksten başlayarak sayar ve değer döner



"araba".find("a") # 0 döner
"araba".rfind("a")# sondan itibaren arıyor 4 dönüyor.
"araba".find("s")# yoksa -1 döner.












