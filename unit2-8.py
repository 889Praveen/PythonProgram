file=open("Student.txt","w+")
s="The State took it's name from the Gujjars, who ruled the area during the 700's and 800's. Stone Age settlements around Sabarmati and Mahi rivers indicate the same time as that of the Indus Valley Civilization while Harappan centres are also found at Lothal, Rampur, Amri and other places."
file.write(s)
file.close()

file=open("Student.txt","r")
print(file.read())
file.close()



