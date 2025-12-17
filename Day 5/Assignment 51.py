# import math as m
# #1 - squareroot
# print(m.sqrt(16))

# #2 - degree to radian
# print(m.degrees(1))

# #3- radian to degree
# print(m.radians(180))

# # 4 - cos and sine function
# print(m.cos(180))
# print(m.sin(0))

#5 - log
# print(m.log10(10))

#6 - factorial
# print(m.factorial(5))

import os
print("current working directory = ",os.getcwd())

# #creating directory
# dir="sunbeam(created using os module)"
# par_dir="D:\Temp"
# path=os.path.join(par_dir,dir)
# os.mkdir(path)

# print(os.cpu_count())

# print(os.getlogin())

# print(os.getppid())

# os.rename("os module.txt", "omkar.txt")

file = open("abhi.txt", "w")
file.write("Hello Python\n")
file.write("File handling using os module")
file.close()

file=open("abhi.txt","r")
print(file.read())
