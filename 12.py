Program12:
birth={"Jignesh":'30/03/00',"Rahul":'1/2/01',"Mehul":'10/1/24',"Hitesh":'15/8/22',"Akshay":'2/2/89'}
person={1:"Jignesh",2:"Rahul",3:"Mehul",4:"Hitesh",5:"Akshay"}
for key,value in person.items():
    print(key," ",value)

no=input("\nEnter no of person , you want to show birthdate Month : ")
num=('0','1','2','3','4','5','6','7','8','9')
while(1):
    i=0
    while(i<len(no)):
       c=no[i]
       if( not c in num):
           no=input("Enter no of person , you want to show birthdate Month : ")
           break
       i+=1
    if(i==len(no)):
        break 
no=int(no)
if(no in person.keys()):
  s=birth[person[no]]
  print(s," ",birth[s]," is find")
else:
    print("Note find")
