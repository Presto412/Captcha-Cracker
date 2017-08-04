from PIL import Image
import os
ct=0
if not os.path.exists("Characters"):
    os.mkdir("Characters")
for i in range(0,100):
    fn="captchas//"+str(i)+".png"
    img=Image.open(fn)
    for j in range(30,181,30):
        ct+=1
        fin="Characters\\"+str(ct)+".png"
        ch=img.crop((j-30,12,j,44))
        ch.save(fin)
    img.save(fn)
