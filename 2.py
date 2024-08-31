#Find the Sum of the first n Natural numbers. 
n1=input("Enter Number of Element: ")
while(1):
   if(n1.isnumeric()):
      break
   else:
       n1=input("Enter Number of Element: ")
    
n=int(n1)
sum=n*(n+1)/2
print(" Natural Numbers is:",int(sum))

   
