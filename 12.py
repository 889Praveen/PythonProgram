#Find brithdays in a month using dictionary
bri={'praveen':'03/08/2004',
      'vikram':'05/06/2005',
    'manish':'12/12/2006',
    'raj':'22/10/21'}
month=input("Enter brithday month(mm):")
count=0
for name,bday in bri.items():
    if bday[3:5]==month:
        print(name)
        count=count+1
        break

if(count==0):
    print("Data NOt Found..!")  