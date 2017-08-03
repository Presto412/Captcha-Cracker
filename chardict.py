import os
from PIL import Image
dirs=os.listdir("Chars")
chardict={}
for i in dirs:
    cordlist=[]
    im=Image.open("Chars//"+i)
    pix=im.load()
    for y in range(0,30):
        for x in range(0,25):
            if pix[x,y]==(0,0,0):
                cordlist.append(str(x)+","+str(y))#check from git
    chardict.update({i[0]:cordlist})
with open("CharacterMaps.py","wb") as f:
    f.write("chardict="+str(chardict))
