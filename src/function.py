# def printme(str):
#     "this prints a passed stirng into this function"
#     print (str)
#     return

# printme("this is first call to the user defined function!")
# printme("Again second call to the same function")

# -------------------------------

# def printinfo( name, age = 35):
#     "this prints a passed info into this function"
#     print ("name:", name)
#     print ("age : ", age)
#     return
# # ㄴ age값을 미입력시 작동으로 35설정

# printinfo(age = 50, name = "miki")
# printinfo(name = "miki")

# ---------------------------------

import support
support.print_func("Zara")

# > 함수 끄집어 내기

# ----------------------------------

import math
math.cos(math.pi/2)

# ---------------------------------

import time
localtime = time.asctime(time.localtime(time.time()))
print ("local current time: ", localtime)


#-----------------------------------

클래스변수
class Employee :
    'common base calss for all employees'
    empCount = 0

    #self = 인스턴스화 된 오브젝트
    def __init__ (self, name, salary):
        self.name = Name
        self.salary = salary
        Employee.empCount += 1
        #이게 있어야 인스턴스화 됨
        #생성자(constructer)     
    
    def displayCount(self) : 
        print("totla employee %d" % Employee.empCount)
    
    def diplayEmployee(self) :
        print("name : ", self.name, "salary",self.salary)

#쿨래스의 이름은 영문대문자
#함수는 영문 소문자

# -------------------------------------
class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

>>>> 클래스 정의

#This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
#This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)

# >>>>>> 메인함수

# ------------------------------------
typing

class Employee :
    'common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("total employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("name: ", self.name, ",salary: ", self.salary)

emp1= Employee("zara",2000)
emp2= Employee("manni",5000)
emp1.displayEmployee()
emp2.displayEmployee()

print("total employee %d" % Employee.empCount)

#-------------------------------------

class Parent:
    parentAttr = 100
    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print('Calling parent method')

    def setAttr(self, attr):
        Parent.parentAttr = attr
    
    def getAttr(self):
        print("Parent attribute :", Parent.parentAttr)

class Child(Parent) : 
    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print('Calling child method')

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()