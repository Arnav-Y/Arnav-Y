from PIL import Image, ImageOps

a = input("Enter The Image Path : ")

img = Image.open(a)
gs = ImageOps.grayscale(img)
gs.show()