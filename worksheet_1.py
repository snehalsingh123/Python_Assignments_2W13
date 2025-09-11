# TUT 1

print("Q1:")
print("Twinkle, twinkle, little star,")
print("How I wonder what you are!")  # \t for indentation
print("\tUp above the world so high,")
print("\tLike a diamond in the sky.")
print("Twinkle, twinkle, little star,")
print("How I wonder what you are")

print("Q2:")
A=input("first name:")
B=input("last name:")
rev_first=A[::-1]
rev_last=B[::-1]
print("reversed name :",rev_first,rev_last)

print("Q3:")
import math
r = float(input("Enter radius of circle: "))
area = math.pi * (r ** 2)
print("Area of circle =", area)

         
             
             
import math
print("area:",math.pi*float(input("r:"))**2)

print("Q4:") 
color_list = ["Red","Green","White" ,"Black"] 
print("first colour:",color_list[0],"  ","last colour:",color_list[-1])

print("Q5:")
n = int(input("Enter an integer: "))
k = 3  
term = 0
result = 0
for i in range(1, k+1): 
    term = term + n  
    result += term
print("Result =", result)


print("Q6:")
Sample_data=(input("enter number with comma:"))
num_list=Sample_data.split(",")
print("list:",num_list)
num_tuple=tuple(num_list)
print("tuple:",num_tuple)
  
  
print("Q7:")
celcius=float(input("enter temp in celcius:"))
fahrenheit=(9/5*celcius)+32
print("value in fahrenheit:",fahrenheit)

print("Q8:")
x=int(input("enter 1st number:"))
y=int(input("enter 2nd number:"))
a=x
x=y
y=a
x=x+1
print("first number:",x)
print("second number:",y)

print("Q9:")
a=int(input("enter a number:"))
if (a % 2 == 0):
    print("is an even number")
else:
    print("odd number")

print("Q10:")
year=int(input("enter year:"))
if (year % 4 == 0 and year%100 != 0):
    print("leap year")
else:
    print("not a leap year")

print("Q11:")
import math
x1=int(input("enter value of x1:"))
x2=int(input("enter value of x2:"))
y1=int(input("enter value of y1:"))
y2=int(input("enter value of y2:"))
euclidean_distance=math.sqrt((x2-x1)**2 +(y2-y1)**2)
print("euclidean distance",euclidean_distance)

print("Q12:")
a=float(input("angle1:"))
b=float(input("angle1:"))
c=float(input("angle1:"))
if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    print("It can form a triangle")
else:
    print("It cannot form a triangle")


print("Q13:")
P = float(input("Enter Principal: "))
R = float(input("Enter Rate of interest: "))
T = float(input("Enter Time (years): "))
A = P * (1 + R/100) ** T
CI = A - P
print("Compound Interest =", CI)
print("Total Amount =", A)

print("Q14:")
a=int(input("enter a number:"))
for i in range(2,a):
    if (a % i == 0):
        print("a is not a prime number")
        break
else:
          print("prime number")


print("Q15:")
N = int(input("Enter a positive integer: "))
sum_sq = 0
for i in range(1, N+1):
    sum_sq += i**2 #(x += y means x = x + y)

print("Sum of squares =", sum_sq)



 
