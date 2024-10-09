import re
s="""The State took it's name from the Gujjars, who ruled the area during
the 700's and 800's. Stone Age settlements around Sabarmati and Mahi
rivers indicate the same time as that of the Indus Valley Civilizati
on while Harappan centres are also found at Lothal,a.gvp@gmail.com Rampur, Amri and
other places."""
s1=" also found at Lothal,a. gvp@gmail.com Rampur  Amri and Stone Age settlements around "
m2=r'\w+\@\w+\.\w+'
m3=r'\w+\@\w+\.\w+'
m1=r'\w+@.[w\.].+\w'
x=re.findall(m2,s1)
print(x)
x=re.findall(m3,s1)
print(x)
x=re.findall(m1,s1)
print(x)
