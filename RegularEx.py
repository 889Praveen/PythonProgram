import re
pattern="python"
data="python is very power full language"
match=re.search(pattern,data)
print(match)

if match:
    pass
else:
    print("Pattern Not Found..!")




data='''The Vidyapith was established to promote educational institutions 
run by Indians for Indians, and to help nationalists establish a system of
education for all Indians. Gandhi wanted the Vidyapith to prepare young
people for national reconstruction and to help achieve his dream of 
Hind Swara'''

pattern = r"^The"

match = re.search(pattern,data)
if match:
    print("Caret Operator Match:", match)
else:
    print("Pattern Not Found..!")


pattern = r'Swara$'
match = re.search(pattern,data)
print("Dollar Sign Match:", match.group())  # Output: "World!"


from re import split
s1="""The university was founded on 18 October
1920 as a 'Rashtriya 55 Vidyapith'Ty ('National University')
by Mahatma Gandhi"""

#compile
# using d+ 1999 89 99 9
p=re.compile('\d+')
print(p.findall(s1))




p=re.compile('\w+')
print(p.findall(s1))
#find a-b character
p=re.compile('[a-b]')
print(p.findall(s1))



s='''The Vidyapith was established to promote educational institutions praveen@gmail.com '''
x=re.search("\.",s)
print(x)


x=re.search("[@]",s)
print(x)

x=re.findall("[a]",s)
print(x)


x=re.findall("^The.*",s)
print(x)








s1="""The university was founded on 18 October
1920 as a 'Rashtriya Vidyapith'Ty ('National University')
by Mahatma Gandhi"""

p1=r"\d{4}"
print(re.findall(p1,s1))

p1=r"\d"
print(re.findall(p1,s1))

p1=r"\d+"
print(re.findall(p1,s1))

p1=r"\w"
print(re.findall(p1,s1))

p1=r"\w+"
print(re.findall(p1,s1))


