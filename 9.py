#Print Fibonacci sequence
while(1):
    n =input("Enter Number:")
    if (n.isnumeric()):
        break
n=int(n)        
num1 = 0
num2 = 1
num3= num2    
count = 1
print("1",end=" ")
while count <= n:
    print(num3, end=" ")
    count += 1
    num1, num2 = num2, num3
    num3= num1 + num2
    