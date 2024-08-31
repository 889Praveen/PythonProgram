#Find brithdays in a month using dictionary
bri={'Praveen':'03/08/2004',
      'Vikram':'05/06/2005',
    'Manish':'12/12/2006',
    'Raj':'22/10/21'}
month=input("Enter brithday month(mm):")
count=0
for name,bday in bri.items():
    if bday[3:5]==month:
        print(name,bday)
        count=count+1
        break

if(count==0):
    print("Data NOt Found..!")  