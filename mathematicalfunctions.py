import math
from math import sqrt
import math as m
from math import *
# Program for Mathematical Functions
# Need to import math for functions to work.
# Importing ways: 
# import math
# import math as m
# from math import functions1, func2
# from math import *
a=math.cos(0)
print("Cos of 0 : ", a)
x=sqrt(16)
print("sqrt of 16 : ", x)
y=m.factorial(5)
print("Factorial of 5 : ", y)
# Multiple Math functions
print("Math Functions. \n")
x=4.5
print("Ceil of 4.5 :", ceil(x))
print("floor of 4.5 : " , floor(x))
print("degree of 3.14159 : ", degrees(3.14159))
print("radians of 180 degrees : " , radians(180))
print("sin of 90 is : " , sin(90))
print("cos of 0 is : " , cos(0))
print("tanu of 45 is : " , tan(45))
print("exp of 0.5 is : " , exp(0.5))
print("absolute value of -4.56 is : " , fabs(-4.56))
print("factorial of 4 is : " , factorial(4))
print("modulus of a float number say 14.5 with 3 is : " , fmod(14.5,3))
print("accurate sum of floating points - 1.5 , 2.4 , -3.3 is : " , fsum([1.5,2.4,-3.3]))
print("float and integer parts of 2.56 : " , modf(2.56))
print("base 10 log of 5.2345 is : " , log10(5.2345))
print("natural log of 5.5 with base 2 is : " , log(5.5,2))
print("sqrt of 49 is : " , sqrt(49))
print("5 power 3 is : " , pow(5,3))
print("gcd of 25 and 30 is : " , gcd(25,30))
print("real value of 15.5676 truncated is " , trunc(15.5676))
print("positive infinity : true : " , isinf(float('Inf')))
print("Constant Is not a number : " , isnan(float('NaN')))
print("Constant pi : " , pi)
print("Constant e : ", e)
print("Constant inf : ", float('inf'))