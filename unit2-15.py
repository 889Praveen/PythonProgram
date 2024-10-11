import re
s ='''
In June 1947, Mahadev Desai Samaj Sewa Mahavidyalay (M.D.S.S.M.V.) was established
.Initially only degree level courses were conducted in this college (M.D.S.S.M.V.).
Considering the national @rupeshsomething and international level significance in value based 
education of Vidyapith.rupesh_something@usa.net The rupesh0somethiNg@gmail.com Government of India, in July 1963, under the 
University praveen.@gvp Grants Commission (UGC) Act, 1956, under its section 3 recognised 
Gujarat Vidyapith as “deemed to be University” and started providing grants in 
aid to Gujarat Vidyapith. After joining the Universe of Universities, the levelof
educational courses in Gujarat @11 Vidyapith were upgraded upto M.A., M.Phil; 
and Ph.D. level. Besides, the Rashtrabhasha Hindi Prachar Samiti; Adult Education,
Tribal Research and Training Institute and Krushi Vignan Kendras were 
established in Gujarat Vidyapith.'''
n1=r'\w+\@\w+'
n2=r'\@\w+'
n3=r'\w+\.@\w+'

temp1=re.findall(n1,s)
temp2=re.findall(n2,s) 
temp3=re.findall(n3,s)

print(temp1)
print(temp2)
print(temp3)

ma=temp1+temp2+temp3

print(ma)