from math import *
from random import *

#1------------------------------------------------------

#try:
#    n = int(input("sisestage arv vahemikus 1 kuni 9: "))
#    while n:
#        if n<1 or n>9:
#            print("Error")
#            break
#        if n.str.isalpha():
#            print("Value Error")
#        else: 
#            for i in range(n):
#                print("   -----  ", end="  ")
#            print()
#            for i in range(3):
#                for j in range(n):
#                    if i == 0:
#                        print("  |  O  |  ", end="  ")
#                    elif i == 1:
#                        print("  !  -  !  ", end="  ")
#                    else:
#                        print("   -----  ", end="  ")
#                print()
#            break
#except: 
#    print("Value Error")

#2------------------------------------------------------
#try:
#    kraadi = int(input("sisesta astendaja: "))
#    n = int(input("Sisestage numbrid n: "))
#except: (print("Value Error"))

#for i in range(1, n+1):
#    print(i ** kraadi)

#3--------------------------------------

#students = randint(1, 30)

#sum = 0

#for i in range(students):
#    grade = randint(1, 5)
#    sum += grade

#average = sum / students

#print(f"õpilaste arv : {students} ", round(average,2))

#4--------------------------------------------

#gift = 1
#birthday = 1
#while gift <= 100:
#    gift += birthday
#    birthday += 1
#print(birthday, "päevaks ületab eelarve 100 dollarit")

#5---------------------------------------------

a, b = 0, 1
while b < 22:
    print(b)
    a, b = b, a + b
