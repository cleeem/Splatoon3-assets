from PIL import Image
import os

key = "image3d"
for file in os.listdir(f"weapons/{key}"):
    img = Image.open(f"weapons/{key}/{file}")
    if img.size == (400, 400):
        img2 = img.resize(size=(256,256))
        img2.save(f"weapons/{key}/{file}")
        print(img2.size, file)