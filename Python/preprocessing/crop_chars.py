from PIL import Image
import os
ct = 0
if not os.path.exists("cropped-chars"):
    os.mkdir("cropped-chars")
for image in os.listdir("noise-reduced-images"):
    image_path = os.path.join("noise-reduced-images", image)
    img = Image.open(image_path)
    for j in range(30, 181, 30):
        ct += 1
        character_path = os.path.join("cropped-chars", str(ct) + ".png")
        ch = img.crop((j-30, 12, j, 44))
        ch.save(character_path)
