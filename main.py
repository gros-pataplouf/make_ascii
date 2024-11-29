from PIL import Image

with Image.open("xmas.png") as im:
    px = im.load()
    height = im.size[0]
    width = im.size[1]
    for i in range(0, height, 3):
        for j in range(0, width):
            print("*" if px[i,j] == (0, 0, 0, 255) else " ", end="")
        print("\r")

