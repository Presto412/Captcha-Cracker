from PIL import Image
import os
order="123456789abcdefghijklmnpqrstuvwxyz"
for i in range(0,len(order)):
    small=750
    char=order[i]
    fn=os.listdir("SortedCharacters\\"+char)
    for i in fn:
        ct=0
        im=Image.open("SortedCharacters\\"+char+"\\"+i)
        pix=im.load()
        for y in range(0,32):
            for x in range(0,30):
                if pix[x,y]==(0,0,0):
                    ct+=1
        if ct<=small:
            small=ct
            im.save("Chars\\"+char+".png")
print "it workd"
