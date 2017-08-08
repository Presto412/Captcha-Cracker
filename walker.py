from os import walk
import timeit,os
from PIL import Image
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
            if float(match)/float(black)>=0.85:
                perc=float(match)/float(black)
                matches.update({perc:i[0].upper()})
        try:
            captcha+=matches[max(matches.keys())]
        except ValueError:
            captcha+="0"
##    img.save("testcaptcha\\"+captcha+".png")
    return captcha  
f = []
for (dirpath, dirnames, filenames) in walk('download\\'):
    f.extend(filenames)
    break
timesum=0
size=len(f)
count=1
maxtime=0
mintime=100
currtime=0
for im in f:
    img=Image.open("download\\"+str(im))
    starttime = timeit.default_timer()
    captcha=CaptchaParse(img)
    print "CAPTCHA:"+captcha
    endtime = timeit.default_timer()
    currtime=endtime-starttime
    if(currtime>maxtime):
            maxtime=currtime
            maximg=img.copy()
            print "new max:"+str(maxtime)
    if(currtime<mintime):
            mintime=currtime
            minimg=img.copy()
            print "new min:"+str(mintime)

    timesum+=currtime
    print "Comparing image "+str(count)+"/"+str(size)
    count+=1
avg=timesum/size

print "========================================"
print "Maximum Time:"+str(maxtime)
print "Minimum Time:"+str(mintime)
print "Total Time:"+str(timesum)
print "Average Time:"+str(avg)
print "========================================"
