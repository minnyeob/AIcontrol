# ----------------------------
import tkinter 
top = tkinter.Tk() 
#Tk = class
top.mainloop()
# ------------------------------

fo = open("foo.txt", "wb")
print ("name of the file: ", fo.name)
print("closed or not : ", fo.closed)
print("opening mode : ", fo.mode)
fo.close()
# ------------------------------
fo = opne("foo.txt", "wb")
print("name of the file", fo.name)
fo.close()
# ------------------------------
fo = open("foo.txt","w")
fo.write("python is a great language. \n Yeah its great!! \n")
fo.close()

#--------------------------------

fo = open("foo.txt", "rt")
str = fo.read(10)
print("read strings is : ",str)
fo.close()
#--------------------------------
fo = open("foo.txt","rt")
str= fo.read(10)
print("read string is : ", str)

position = fo.tell()
print("Current file position : ", position)

posisiton = fo.seek(0,0)
str = fo.head(10)
print("again read Strings is : ", str)

fo.close()
#--------------------------------
import os
os.rename( "test1.txt", "test2.txt" )
#--------------------------------

import os
os.mkdir("test")
#--------------------------------

import os
os.chdir("/home/newdir")
#--------------------------------
import os
os.getcwd("newdir")
#--------------------------------
import os
os.rmdir( "/tmp/test"  )