from PIL import Image
import os
if not os.path.exists("SortedCharacters"):
    os.mkdir("SortedCharacters")
order="123456789abcdefghijklmnpqrstuvwxyz"
for i in range(0,len(order)):
    black=0
    im1=Image.open("Chars\\"+order[i]+".png")
    if not os.path.exists("SortedCharacters\\"+order[i]):
        os.mkdir("SortedCharacters\\"+order[i])
    im1.save("SortedCharacters\\"+order[i]+"\\First.png")
    pix1=im1.load()
    for y in range(0,32):
        for x in range(0,30):
            if pix1[x,y]==(0,0,0):
                black+=1
    for j in range(1,601):
        match=0
        im2=Image.open("Characters\\"+str(j)+".png")
        pix2=im2.load()
        for y in range(0,32):
            for x in range(0,30):
                if pix1[x,y]==pix2[x,y] and pix2[x,y]==(0,0,0):
                    match+=1
        if float(match)/float(black)>=0.95:
            fp="SortedCharacters\\"+order[i]+"\\"+order[i]+"-"+str(4000+j)+".png"
            im2.save(fp)
