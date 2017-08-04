from PIL import Image
import os
def CaptchaParse(img):
    captcha=""
    dirs=os.listdir("Chars")
    pix=img.load()
    for y in range(1,44):
        for x in range(1,179):
            if pix[x,y-1]==(255,255,255) and pix[x,y]==(0,0,0) and pix[x,y+1]==(255,255,255):
                pix[x,y]=(255,255,255)
            if pix[x-1,y]==(255,255,255) and pix[x,y]==(0,0,0) and pix[x+1,y]==(255,255,255):
                pix[x,y]=(255,255,255)
            if pix[x,y]!=(255,255,255) and pix[x,y]!=(0,0,0):
                pix[x,y]=(255,255,255)
    for j in range(30,181,30):
        ch=img.crop((j-30,12,j,44))
        pix1=ch.load()
        matches={}
        for i in dirs:
            match=0
            black=0
            pixx=0
            im2=Image.open("Chars\\"+i)
            pix2=im2.load()
            for y in range(0,32):
                for x in range(0,30):
                    if pix1[x,y]==pix2[x,y] and pix2[x,y]==(0,0,0):
                        match+=1
                    if pix2[x,y]==(0,0,0):
                        black+=1
                    if pix1[x,y]==(0,0,0):
                        pixx+=1
            if float(match)/float(black)>=0.80:
                perc=float(match)/float(black)
                matches.update({perc:i[0].upper()})
        try:
            captcha+=matches[max(matches.keys())]
        except ValueError:
            captcha+="0"
##    img.save("testcaptcha\\"+captcha+".png")
    return captcha  
img=Image.open("2.png")
print CaptchaParse(img)

