#Class Basics
'''
class University:
    marks =0
    def __init__(self,marks):
        self.marks = marks
    def check_pass_or_fail(self):
        if(self.marks >= 40):
            return(True)
        else:
            return(False)


student1 = University(85)
print(student1.check_pass_or_fail())
student2 = University(35)
print(student2.check_pass_or_fail())

#Inheritence

class Customer:
    customerid_public = 0
    _customerid_protectd = 0
    def __init__(self, name,id=0):
        self._customerid_private=id
        self._customerid_protectd = id +1
        self.customerid_public = id + 2
        self.__customername=name
    def printid(self):
        print("Inside Print Customer ID")
        print(self._customerid_private)

class RegularCustomer(Customer):
    def __init__(self, id=0, name=None, dis=0):
        super().__init__(id,name)
        self.__discount=dis

customer1 = Customer("John",2)
#customer1.printid()
customer1.customerid_public = 5
print(customer1.customerid_public)
customer1._customerid_protectd = 10
print(customer1._customerid_protectd)
#print(customer1._customerid_private)


#Multiple inheritence
class father:
    def land(self):
        print("father's land")
    def money(self):
        print("father's money")
class mother:
    def jewels(self):
        print("mother's jwellery")
    def money(self):
        print("mother's money")
class son(father, mother):
    pass
class daugther(mother, father): 
    pass

john = son()
mary = daugther()
john.land()
john.money()
john.jewels()
mary.jewels()
mary.money()

#Aggregation

class Address:
    def __init__(self, addressline):
        self.__addressline=addressline
    def getaddressline(self):
        return self.__addressline

class Customer:
    def __init__(self, address):
        self.__address=address
    def getaddress(self):
        return self.__address

add = Address("No.333")
custobj = Customer(add)
#Check if address is correctly saved
temp=custobj.getaddress()
print("Address:")
print(temp.getaddressline())

#Abstraction
class temperatureConverter:
    def __init__(self):
        print("Temperature converter Initialized")
    
    def celcius_to_fahrenheit(self,temp):
        return(round(32+9/5*(float(temp)),3))
    def fahrenheit_to_celcius(self,temp):
        return(round(5/9*(float(temp)-32),3))

mytempconv = temperatureConverter()
print(mytempconv.celcius_to_fahrenheit(37))
print(mytempconv.fahrenheit_to_celcius(98.6))

inputType = input("Choose Celcius or Fahrenheit for conversion: ")
if(inputType.lower() == "celcius"):
    print(mytempconv.celcius_to_fahrenheit(input("Enter Temperature in Celcius: ")))
elif(inputType.lower() == "fahrenheit"):
    print(mytempconv.fahrenheit_to_celcius(input("Enter Temperature in Fahrenheit: ")))

#polymorphism
import math
class regularPolygon():
    def __init__(self,n,l):
        self.sides = n
        self.length = l
    def calculateArea(self):
        apothem = (self.length)/(2*math.tan(math.pi/self.sides))
        return(self.sides*self.length*apothem/2)

square = regularPolygon(4,10)
print(square.calculateArea())
equiTriangle = regularPolygon(3,12)
print(equiTriangle.calculateArea())
regularPentagon = regularPolygon(5,9)
print(regularPentagon.calculateArea())

# Class DIR and Help 
class arithmetic:
    _avg = 0
    publicKey = 101
    def __dir__(self):
        This is dummy DIR declaration
        return("_avg","publicKey")
    
    def this_dummy_func():
        This function is dummy
        pass
myObject = arithmetic()
print(dir(myObject))
print(help(myObject))
'''