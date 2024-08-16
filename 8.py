#Find out pass-percentage of a class .
while(1):
    num=input("Enter Number of Student:")
    if (num.isnumeric()):
        break
    else:
        print("please Enter Number of Student valid Number...!")
 #user input values
num=int(num)
count=0
Fail=0
for i in range(0,num):
    m1=int(input("Enter student  marks:"))
    if m1>=40:
        count = count+1
        #print(count)
    else:
        Fail=+1
        
if count>0:
    temp=count*100/num
    print("Passed Student:",temp,"%")
    temp=Fail*100/num
    print("Fail Student",Fail,"%")
