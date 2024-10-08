import sys 
myfile=open(sys.argv[1],"r+")
data=myfile.read()
print(data)
newdata=data.replace(sys.argv[2],sys.argv[3])


myfile.write(newdata+"new data")
myfile.seek(0)

print("\n new data")
data1=myfile.read()
print(data1)

myfile.close()



