#Program to check number is prime or not 
while(1):
    num=input("Enter Number of Element:")
    if(num.isnumeric()):
        break
    else:
        print("please Enter valid Number...!")

num=int(num)
n1=num
f=0

for i in range(2,(num//2)+1):
    if(num%i==0):
        f=1;
        break
if(f==0):
    print("Number is a prime:",n1)
elif(f==1):
    print("Number is Not prime:",n1)
    