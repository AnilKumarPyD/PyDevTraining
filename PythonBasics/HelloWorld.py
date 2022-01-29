print("\nHelloWorld, Welcome To PyDevTraining")

#This is one line comment

"""
This is multiline  comment
"""

#IF Elif Else
if(True):
    print("\nInside IF True") #do something
elif(False):
    pass
else:
    pass

#For Loop
print("\nFor Loop example")
for i in range(5): # [0,1,2,3,4]
    print(i,end=" ")

#While Loop
print("\nInside While Loop")
i=0
while(i <5):
    print(i)
    i+=1

#lists
print("\nList Example")
thisList1 = []
thisList2 = [i for i in range(10)] #populating list with generator
thisList1.append(list(range(10))) #Lets just append range list
print(thisList1)
print(thisList2)

#Tuple
print("\nTuple Example")
tuple1 = (1,2) #immutable
print(tuple1[0])
#tuple1[0] = 2  #Disable comment to see failure of immution
print(tuple1[0])

#Sets
print("\nSet Example")
set1 = set(thisList2)
set2 = set([i for i in range(10) if i%2==0])
print(set1)
print(set2)
print("Odd Numbers",set1-set2)

#Dictionaries
print("\nDictionary example")
key2 = "key2"
dcn1 = {"key1":123456,key2:2345}
print(dcn1["key1"],dcn1[key2])

#Functions
print("\nFunction Example")
def ThisFunction(param1,param2):
    #do something with params
    param1 = param2+34
    return(param1)
print(ThisFunction(2,3))

#Class
print("\nClass Example")
class FirstClass():
    classElements = 0

    def __init__(self):
        #initialize object data
        print("This method is called once a class is called/object is created")
        print(self.classElements)

    def ClassMethod1(self,): #class method is called on self
        self.classElements+=1

    def ClassMethod2(self,):
        self.classElements+=1

class secondClass(FirstClass):
    pass

#Instantiating an object
FirstObject = FirstClass()
print(FirstObject.ClassMethod1())
print(FirstObject.classElements)

FirstObject = secondClass()
print(FirstObject.ClassMethod1())
print(FirstObject.classElements)

'''
Class has below properties:
1.) Polymorphism
2.) Encapsulation
3.) Inheritence
4.) Abstraction
'''
print("\nEnd of HelloWorld")