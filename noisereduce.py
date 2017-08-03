from PIL import Image
for i in range(0,100):
    im=Image.open("download\\"+str(i)+".png")
    pix=im.load()
    for y in range(1,49):
        for x in range(1,149):
            if pix[x,y-1]==(255,255,255) and pix[x,y]==(0,0,0) and pix[x,y+1]==(255,255,255):
                pix[x,y]=(255,255,255)
            if pix[x-1,y]==(255,255,255) and pix[x,y]==(0,0,0) and pix[x+1,y]==(255,255,255):
                pix[x,y]=(255,255,255)
    im.save("captchas\\"+str(i)+".png")
