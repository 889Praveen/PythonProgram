text='''The early modern period began in the 16th century, when the Mughal Empire 
conquered most of the Indian subcontinent,[16] signaling the proto-industrialisation,
becoming the biggest global economy and manufacturing power.[17][18][19] The Mughals
suffered a gradual decline in the early 18th century, largely'''

file=open("split.txt","w+")
file.write(text)
file.close()

myfile1=open("split.txt","r")
line=myfile1.read()
#print(line)
s=line.split()
print("<===============use Split==============>")
print(s)
myfile1.close()

myfile2=open("split1.txt","w+")
for i in s:
    myfile2.write(i+" ")


myfile2.seek(0)
newfile=myfile2.read()
print(newfile)
myfile2.close()
