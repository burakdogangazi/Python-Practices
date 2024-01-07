# pip3 install Pillow
from PIL import Image,ImageFilter

image = Image.open("kuş.jpg")

# image.save("kuş2.jpg") 2.kez kaydetti kuş2 adında
image.show() # resmi gösterir

image.rotate(180).save("kuş3.jpg")

image.convert(mode ="L").save("kuş4.jpg") # siyah beyaz yapar

degistir = (960,600)

image.thumbnail(degistir)

image.save("kuş6.jpg")

image.filter(ImageFilter.GaussianBlur(5)).save("kuş7.jpg")




kırpılacak_alan = (340,0,950,600)
image2 = image.open("atatürk.jpg")
image2.crop(kırpılacak_alan).save("kuş9.jpg")












