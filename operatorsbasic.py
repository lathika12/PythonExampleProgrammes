# Operators in Python
print("Operators in Python : \nArithmetic Operators \nAssignment Operators \nUnary Minus Operator \nRelational Operators \nLogical Operators \nBoolean Operators \nBitwise Operators \
 \nMembership Operators \nIdentity Operators")
 #Arithmetic Operator
print("Arithmetic Operators")
a=50
b=4
print("a+b : " , a+b)
print("a-b : " , a-b)
print("a*b : " , a*b)
print("a/b : " , a/b)
print("a%b : " , a%b)
print("a**b : " , a**b)
print("a//b : " , a//b)
#Assignment Operators
print("Assignment Operators")
z=a+b
print("Op : = z=a+b " , z)
z%=b
print("Op : = z%=b " , z)
z+=b
print("Op : = z+=b " , z)
z-=b
print("Op : = z-=b " , z)
z*=b
print("Op : = z*=b " , z)
z/=b
print("Op : = z/=b " , z)
z**=b
print("Op : = z**=b " , z)
z//=b
print("Op : = z//=b " , z)

#Applying same value to different variables.
a=b=1
print("a=b=1",a,b)
#Assign different variables to different variables 
a=1; b=1; c=2
print("a=1; b=1; c=2",a,b,c)
a,b = 1,2
print("a,b = 1,2",a,b)

#Unary Minus Operator
print("Unary Minus Operator")
n=10
print("-n : for n=10 : " , -n)
print("-n : for above changed n=-10 : " , -n)

#Relational Operators
print("Relational Operators")
a=5
b=3
print("a>b : " , a>b)
print("a<b : " , a<b)
print("a>=b : " , a>=b)
print("a<=b : " , a<=b)
print("a==b : " , a==b)
print("a!=b : " , a!=b)
print("4>2>=3>1 : ",4>2>=3>1)
print("4>2>=3<1 : ",4>2>=3<1)

#Logical Operators
print("Logical Operators")
x=1
y=2
print("And : x and y : " , x and y)
print("And : x or y : " , x or y)
print("And : not y : " , not y)

#Boolean Operators - Act upon bool type literals
print("Boolean Operators")
x=True
y=False
print("And : x and y : " , x and y)
print("And : x or y : " , x or y)
print("And : not y : " , not y)

#Bitwise Operators
print("Bitwise Operators")
x=10
y=11
print("Bitwise complement operator - ~ : " , ~x)
print("Bitwise AND operator - & : " , x&y)
print("Bitwise OR operator - | : " , x|y)
print("Bitwise XOR operator - ^ : " , x^y)
print("Bitwise right shift operator - >> : " , x>>2)
print("Bitwise left shift operator - << : " , x<<2)

#Membership Operators
print("Membership Operators : in , not in")

lst = ["1","2","3","4","5"]

for k in lst :
	print(k)

k=0
	
if k not in lst :
	print("7 not in list.")	

#Identity Operator
print("Identity Operator : is , is not : id() - finds the exact address a value is stored.")
a=b=25
print("For both a=b=25.. id() should be same . ")
print("id(a) : " , id(a))
print("id(b) : " , id(b))
if a is b :
	print("a is b")
else:
	print("a is not b")

#If comparing elements id doesn't exactly help.

one=[1,2,3]
two=[1,2,3]
print("id(one) : " , id(one))
print("id(two) : " , id(two))
if one is two :
	print(" one is two . ")
else:
	print(" one is not two . ")
if one == two :
	print("one == two works. id() doesn't")
else:
	print(" one != two. ")
