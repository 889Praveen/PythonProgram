#Find brithdays in a month using dictionary
bri={'praveen':'03/08/2004',
      'vikram':'05/06/2005',
    'manish':'12/05/2006'}
month=input("Enter brithday month(mm)")
for name,bday in bri.items():
    bday_month=bday[3:5]
    if bday_month==month:
        print(name)