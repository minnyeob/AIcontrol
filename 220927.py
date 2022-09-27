print ("Hello, Python!")
# ------------------------------
print ("Hello, Python")
# ------------------------------
print ("Hello, Pyhthon!")
# ------------------------------
counter = 100
miles = 1000.0
name = "john"

print (counter)
print (miles)
print (name)
# ------------------------------
str = 'Hello World'

print (str)
print (str[0])
print (str[2:5])
print (str[2:])
print (str*2)
print (str + "test")
# ------------------------------
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)          
print (list[0])       
print (list[1:3])     
print (list[2:])      
print (tinylist * 2)  
print (list + tinylist) 
# ------------------------------
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)           
print (tuple[0])        
print (tuple[1:3])      
print (tuple[2:])       
print (tinytuple * 2)   
print (tuple + tinytuple) 
# ------------------------------
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (dict['one'])       
print (dict[2])           
print (tinydict)          
print (tinydict.keys())   
print (tinydict.values())
# ------------------------------
# 중요
var = 100
if(var == 110):
    print("value of expressiont is 100")
else :
    print("거짓된 조건입니다")
    print("goodbye")

# ------------------------------
var = 70

if(var > 75):
    print ("var는 75초과입니다")
elif(var <= 75 & var > 25):
    print("var는 25초과 75이하입니다")
else :
    print("var는 25이하입니다")
# ------------------------------
var1 = 'Hello world'
var2 = "python programming"

print("var1[0]: ", var1[0])
print("var[1:5]", var2[1:5])
# ------------------------------
var1 = 'hello world'
print ("updating string : -", var1[:6] + python)
# ------------------------------
prnt("My name is %s and weight is %d kg!"%('zara,21'))
# ------------------------------
para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print (para_str)
# ------------------------------
print ('C:\\nowhere')
# ------------------------------
print(r'C:\\nowhere')
# ------------------------------
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1,2,3,4,5,6,7]

print("list1[0]", list[0])
print("list[1:5] : ", list2[1:5])
# ------------------------------
list = ['physics','chmisty', 1997, 2000]
print ("Value available at index 2 : ", list[2])

list[2] = 2001
print *"new value available at index 2", list[2]
# ------------------------------
list = ['physics', 'chemistry', 1997, 2000]
print (list)

del list[2]
print ("After delting value at index 2", list)
# ------------------------------
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1,2,3,4,5,6,7)

print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]", tup2[1:5])
# ------------------------------
tup1 = (12, 34.56)
tup2 = ('abc', 'xyx')

tup3 = tup1 + tup2
print (tup3)
# ------------------------------
# 중요
import sys
#sys는 모듈
list = [1,2,3,4]

for x in list:
    print (x, end = " ")

it = iter(list)

while True :
    try :
        print (next(it))
    except StopIteration :
        break

#stopiteration => 파이선 종료

# ------------------------------
var1 = 'hello World'
var2 = "python Programing"

print ("var1[0]:", var1[0])
print ("var2[1:5]: ", var2[1:5])

# ------------------------------
var1 = 'Hello World'
print ("updated String : -", var1[:6] + 'Python')

# ------------------------------
def printme(str) :
    print (str)
    return

printme("This is first call to the user defined function!")
printme("Again second call to the same function")

# ------------------------------

def changeme(mylist):
    "this changes a paased list into this function"
    print ("Values inside the function before change: ", mylist)
    mylist[2]=50
    print("Values inside the function after change: ",mylist)
    return

mylist = [10,20,30]
changeme(mylist)
print("Values outside the function: ", mylist)

# ------------------------------

def printme(str) :
    "this print a passed string into this function"
    print (str)
    return

printme()

# ------------------------------

def printme(str):
    print(str)
    return
printme(str = "my string")

# ------------------------------

def printinfo(name, age):
    print ("Name: ", name)
    print ("age", age)
    return
printinfo(age = 50 , name = "miki")

# ------------------------------

def printinfo(name, age =35):
    "this prints a passed info into this function"
    print("name:", name)
    print("age", age)
    return
printinfo(age=50,name="miki")
printinfo(name = "miki")

# ------------------------------

def printinfo(arg1, *vartuple):
    "this prints a variable passed arguments"
    print ("output is:")
    print (arg1)
    for var in vartuple:
        print(var)
    return

printinfo(10)
printinfo(70,60,50)

# ------------------------------

sum = lambda arg1, arg2: arg1 + arg2

print ("value of total : ", sum(10,20))
print ("value of total : ", sum(20,20))

# ------------------------------
def sum(arg1, arg2):
    total = arg1 + arg2
    print("Inside the function: ", total)
    return total

total = sum(10,20)
print ("Outside the function: ", total)
    
# ------------------------------
total = 0
def sum(arg1,arg2):
    total = arg1 + arg2
    print("Inside the function lcal total : ", total)
    return total

sum(10,20)   
print("outside the function global total: ", total)

# ------------------------------

def fib(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a,b = b, a+b
    return result
if __name__ == "__main__":
    f = fib(100)
    print(f)
    
# ------------------------------
Money = 2000
def AddMoney():
   Money = Money + 1

print (Money)
AddMoney()
print (Money)

# ------------------------------

import math

content = dir(math)
print (content)