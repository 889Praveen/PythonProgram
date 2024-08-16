#collatz sequence
def ins():
    num=input("Enter Number of Element:")#user Enter
    while(1):
        if(num.isnumeric()):
            break
        else:
            num=input("Enter Number of Element:") 
    print(num,end=" ")    
    num=int(num)
    while num!=1: 
        if(num%2==0):
            num=int(num/2)
            print(num,end=" ") 
        else:
            num=int(num*3+1)
            print(num,end=" ")
    
ins()
