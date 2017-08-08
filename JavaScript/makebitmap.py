import json
f=open("bitmaps.json")
dic=json.load(f)
f.close()
print len(dic)
g=open("newmaps.py","w")
g.write("{\n")
for i in sorted(dic.keys()):
    g.write('"'+str(i)+'":[\n')
    val=dic[i]
    for j in val:
        g.write('\t'+str(j)+',\n')
    g.write('],\n')
print "itworkd"

        
        

