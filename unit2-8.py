import sys
file=open(sys.argv[1],"w")
'''s="Founding: Mahatma Gandhi founded Gujarat $ ^ @ $ Vidyapith\n\n \n #Rashtriya VidyapithDeemed university: Gujarat Vidyapith has been a deemed university since 1963. "'''
data=sys.argv[2].split(".")

sentecs=""

for i in data:
    sentecs+=' '+i

file.write(sentecs)

file.close()

file=open("student.txt","r")
f=file.read()
for i in f:
    print(i,end="")
file.close()

myfile=open("hello.txt","w+")
myfile.write(f)
myfile.seek(0)
line=myfile.read()
print(line)
myfile.close()
    


