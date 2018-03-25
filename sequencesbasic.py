#Sequences in Python
'''str
bytes - unmodifiable
bytearray
list
tuple - unmodifiable
range'''
#Str datatype
str="String inside double quotes."
print(str)
str="String inside 'double quotes' with single quotes in the string."
print(str)
str="""String inside "triple quotes".
With multiple lines that are to be displayed.
Line 3 in progress...."""
print(str)
str='''String inside "triple single quotes".
To be displayed as shown.
Line 3 in progress.....'''
print(str)
str="Methods available for strings."
print("str[0] : M" , str[0])
print("str[3:7] : " , str[3:7])
print("str[11:] : 11 to end : " , str[11:])
print("str[-1] : end char : . : " , str[-1] )
print("str*2 : twice the same sentence : \n " , str*2)
#Bytes datatype - unmodifiable - A byte number is any positive integer from [0,255]
elements = [10,20,0,255,2]
x = bytes(elements)
print(x[0])
for i in x : print(i)
#Bytearray datatype - modifiable
elements = [10,255,20,0]
x = bytearray(elements)
for i in x : print(i)
print("x[0] : " , x[0])
x[0]=41
print("x[0] : " , x[0])
#list datatype - modifiable
list = [10,-20,'Vij',"Hi"]
print("list is : " , list)
print("list[0] : " , list[0])
print("list[1:2] : " , list[1:2])#position 2 excluded
print("list[-1] : " , list[-1])
print("list*2 : \n" , list*2)
newl = list*2
print(newl)
newlis = [list*2]
print(newlis)
#tuple datatype - unmodifiable
tpl = (10,-20,15.5,"Vij",'Mar')
print("tpl[0] : ",tpl[0])
print("tpl[1:3] : ",tpl[1:3])
print("tpl[-1] : ", tpl[-1])
print("tpl*2 : ", tpl*2)
newtpl=(tpl*2)
print("newtpl : " , newtpl)
#Range datatype
r = range(5)
for i in r: print(i)
r = range(30,40,2) # 40 is excluded in step of 2
for i in r: print(i)
#lst=list((range(5)))
#print(lst) - supposed to work.