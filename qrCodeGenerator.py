import qrcode

img = qrcode.make("https://www.geeksforgeeks.org/python-programming-language/?ref=shm")
img.save("geekspage.jpg")

imgs = qrcode.make("This is written text in qrcode")
imgs.save("writens.jpg")
