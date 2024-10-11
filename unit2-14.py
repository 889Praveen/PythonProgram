import re 
s='''Founding: Mahatma Gandhi founded Gujarat Vidyapith on October 18, 1920, as a "Rashtriya Vidyapith" or "National University". 
Chancellor: Gandhi served as the university's chancellor, or kulpati, throughout his life. 
Deemed university: Gujarat Vidyapith 7564234123 has been a deemed university since 1963. 
Location: The university is 9494948578 located in Ahmedabad, Gujarat, India. 
Gandhian ethos: The (223) 544 5649 university is a reflection of Gandhian values, with students wearing khadi and inspirational messages from Gandhi on the walls. 
Departments: Some of the 43488 90656  departments at Gujarat Vidyapith include: 
Adhyapak Shiksha Vibhag: This department +8766555234 includes a Hindi teacher training college, a teaching college, and a basic education science institute'''
n1=r'\d{10}'
n2=r'\d{5}\s\d{5}'
n3=r'\(\d{3}\)\s?\d{3}\D\d{4}'
n4=r'\+\d{10}'
temp1=re.findall(n1,s)
temp2=re.findall(n2,s)
temp3=re.findall(n3,s)
temp4=re.findall(n4,s)
print(temp1)
print(temp2)
print(temp3)
print(temp4)
ma=temp1+temp2+temp3+temp4
print(ma)
