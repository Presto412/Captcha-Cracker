from PIL import Image
import os
if not os.path.exists("captchas"):
    os.mkdir("captchas")
for i in range(0,100):
    im=Image.open("download\\"+str(i)+".png")
    pix=im.load()
    for y in range(1,44):
        for x in range(1,179):
            if pix[x,y-1]==(255,255,255) and pix[x,y]==(0,0,0) and pix[x,y+1]==(255,255,255):
                pix[x,y]=(255,255,255)
            if pix[x-1,y]==(255,255,255) and pix[x,y]==(0,0,0) and pix[x+1,y]==(255,255,255):
                pix[x,y]=(255,255,255)
            if pix[x,y]!=(255,255,255) and pix[x,y]!=(0,0,0):
                pix[x,y]=(255,255,255)
    im.save("captchas\\"+str(i)+".png")
