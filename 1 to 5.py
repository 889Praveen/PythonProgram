program 1:

#Program:1::Find probability .
tc=52
tk=4
ts=13

total_king_spade=tk+ts-1
wks=tc-total_king_spade
pro=wks/tc
print("probability is ",pro)


program:2:

#Find the Sum of the first n Natural numbers. 
n1=input("Enter Number of Element: ")
if(n1.isnumeric()):
    n=int(n1)
    sum=n*(n+1)/2
    print(" Natural Numbers is:",int(sum))
else:
    print("Enter valid Number...!")


program:3:


#roll no using slicing


e=input("Enter Enrollment no:ex-CS24M041").upper()
l=len(e)
dep1=e[0:2]
year=e[2:4]
degree=e[4:5]
rno=e[5:]
if(dep1=="CS"):
    department="Computer Science"
    if(degree=="M"):
        degree="MCA"
    elif(degree=="B"):
        degree="BCA"
            
elif(dep1=="ME"):
    department="Mechanical engineering"
    if(degree=="B"):
        degree="BME"
    elif(degree=="M"):
        degree="MME"
print("Department: {}   Year :20{}   Degree:{}    Roll No:{} ".format(department,year,degree,rno))
    
      
#Department: Mechanical engineering Year :2022 Degree:MME Roll No: 
 
 
Program:4:

#string manipulation 
n="Gujrat vidyapith"
print(n[1])
print(n[-1])
print(n[1::])
print(n[1:])
print(n[1:5])
print(n[:1])
print(n[:-1])
print(n[0:17])
print(n[-3:-1])
print(n[-8::-1])
print(n[-15::-1])
print(" \n")
print("other change ")
t=n[0:6]
s=n[8:10]
f=n[9:16]
print("Before =",n)
print("After =",f,s,t)

Program:5:

#Program 5:Write a Program to find out if the two blood group match
def blood_check(b1,b2):
    if(b1==b2):
        return 1
    else:
        return 0
bg=('A-','A+','B-','B+','O-','O+','AB+','AB-')
while(1): 
   bood_group1=input("Enter first person Blood Group:").upper()
   if(bood_group1 in bg):
        break
while(1):
   bood_group2=input("Enter second person Blood Group:").upper()
   if(bood_group2 in bg):
        break
if(blood_check(bood_group1,bood_group2)==1):
    print(" {} and {} blood groups are match...".format(bood_group1,bood_group2))
else:
    print("{} and {} blood groups are not match...".format(bood_group1,bood_group2))