from PIL import Image
import os


for file in os.listdir("weapons"):
    img = Image.open(f"weapons/{file}")
    if img.size == (400, 400):
        img2 = img.resize(size=(256,256))
        img2.save(f"weapons/{file}")
        print(img2.size, file)