from PIL import Image
import os
import json

bitmaps = {}
for image in sorted(os.listdir("library-chars")):
    char_name = image.strip(".png").upper()
    bitmaps[char_name] = []
    img = Image.open(os.path.join("library-chars", image)).convert('L')
    pix = img.load()
    for y in range(0, img.height):
        temp = []
        for x in range(0, img.width):
            temp.append(pix[x, y])
        bitmaps[char_name].append(temp)

with open("bitmaps.json", "w") as f:
    json.dump(bitmaps, f)
