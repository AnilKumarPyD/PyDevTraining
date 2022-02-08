#Math
'''
import math
print(abs(1.5))
print(math.ceil(1.5))
print(math.floor(1.5))
print(round(3.5645,2))
print(max(2,3,1))

#String
str1 = "StringObject"
count_returned = str1.count("S")
print(count_returned)
str2 = "Learning python is easy"
print(str2.replace("easy","not easy"))
print(str2)

paragraph = "Anil and there is python"
if "anil" in paragraph.lower():
    paragraph = paragraph.replace("anil","Anil")
print(paragraph)

#List
lst1 = [2,4,5,6]
print(sorted(lst1,key = ))
'''
#Modules and packages
from mathSubpackage.arithmetic import adder as customName
print(customName.addTwoNumbers(2,3))