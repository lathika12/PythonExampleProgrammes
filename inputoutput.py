# Output Statements.
#print() statement
#print("string") statement
#print('string') statement
print("Line2 has empty print.")
print()
print('Line 3')
# \n - new line \t - horizontal tab \\ - escape escape char.
print("This is \nNext Line.")
print("This is \tHorizontal Tab.")
print("This is \\tEscaped Tab.")
#Print statement thrice
print(3*"Hai")
# + - join without space , ,- join with space
print("City =" + "Hyderabad - with +")
print("City =" , "Hyderabad - with ,")
#print(variable list) print("string",variable list)
a, b= 2,4
print(a , b)
print(a , b , " : Variables. ")
print("Separated by sep examples")
print(a,b,sep=",")
print(a,b,sep=":")
print(a,b,sep="----")
#end = '\n' by default
print("Hello",end='')
print("Next Line?",end='')
print()
print("Hello",end='\t')
print("Next Line?",end='\t')
print()
#print(object) print("string",object)
lst = [10 ,'A' , "Hai"]
print(lst)
d = {'One' : 1 , 'Two' : 2}
print("d : \n " , d)
#print("formatted string") %i %d - decimal %f - float %s - string %c - single char  %20s - 20 spaces %.3f - 3 fraction digits
x=10
print("Value of i = %i" % x)
name='Linda'
print('Hai (%20s)' % name)
print('Hai (%-20s)' % name)
num = 123.456789
print("Value is : %f : %8.2f" % (num , num ) )
#format values - {} need not have indexes or names - default seq. is considered.
n1,n2 = 1,2
print("num1 = {} , num2 = {} " .format(n1,n2))
print("num1 = {0} , num2 = {1} " .format(n1,n2))
print("num1 = {one} , num2 = {two} " .format(one=n1,two=n2))

#INPUT STATEMENTS
#Accepting input
str=input()
print("Using input() : " , str)
#Accepting a string input
str=input('Enter your name: ')
print("Your input was  : " , str)
#Accepting an integer input
str=input('Enter a number:')
x=int(str)
#Accepting a float input
print("The number entered in integer form : " , x)
x=float(input('Enter a number:'))
print("Float form of the entered number is: ",x)
#Accepting single char from keyboard
ch=input('Enter a char : ')
print("The character accepted is : ", ch[0])
#Accepting 2 integers and finding product of them.
x=int(input('Enter x : '))
y=int(input('Enter y : '))
print("The product of {0} and {1} is {2} " .format(x,y,x*y))
#Convert numbers from other systems to decimal number system
str=input('Enter hexadecimal number:')
n=int(str,16) # inform the number is base 16
print('Hexadecimal to decimal :' , n)
str=input('Enter octal number:')
n=int(str,8) # inform the number is base 8
print('octal to decimal :' , n)
str=input('Enter binary number:')
n=int(str,2) # inform the number is base 2
print('binary to decimal :' , n)
#Accept 3 integers in the same line and print their sum
v1,v2,v3=[int(x) for x in input("Enter 3 numbers ").split()]
print("Sum: ", v1+v2+v3)
v1,v2,v3=[int(x) for x in input("Enter 3 numbers , seperate with a , ").split(',')]
print("Sum: ", v1+v2+v3)
#Evaluating an expression
x=eval(input("Enter an expression."))
print("Result - %d" % x)
#Accept a list and display it
lst=eval(input('Enter a list : '))
print("List is: " , lst)
#Accept a tuple and display it
tpl=eval(input('Enter a tuple : '))
print("Entered tuple  : " , tpl)