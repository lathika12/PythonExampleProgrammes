# Program for literals
# 3  types: Numeric | Boolean | String
print("Numeric literals : \nInteger \nFloat \nHexadecimal \nOctal \nBinary \nComplex")
a = 3
print("Integer literal : " , a)
a = 4.5
print("Float literal : " , a)
a=0X5A1C
print("Hexadecimal literal : " , a)
a=0O557
print("Octal literal : " , a)
a=0B101101
print("Binary literal : " , a)
a=10+2j
print("Complex literal : ", a)
print("Boolean literals : \nTrue \nFalse")
a=True
print("True : " , a)
a=False
print("False : " , a)
print("String literals :")
a='Normal Single quoted String'
print(a)
a="Double quoted string literal."
print(a)
a='''Multiple lines for triple single quotes.
Line 2.
Line 3.'''
print(a)
a="""Multiple lines for double single quotes.
Line 2.
Line 3."""
print(a)
a='''Multiple lines for triple single quotes.
Line 2. With 'Single quoted and "double quoted" sentence inside.'
Line 3.'''
print(a)
a="""Multiple lines for double single quotes.
Line 2. With 'Single quoted and "double quoted" sentence inside.'
Line 3."""
print(a)
a="First line with slash \
next line should be continued without error."
print(a)
#Escape characters 
print("\ - continuation.")
print(" \\\ - display single slash .")
print(" \\' - display single quote .")
print(" \\\" - display double slash .")
print(" \\ \bb - display backspace .")
print(" \\ XXX \rr - enter .")
print(" \\\tt - display horizontal tab space - 8 chars .")
print(" \\v - display vertical tab . \v Vertical tab.")
print(" \\n - New line. \n New line. ")



# To determine Datatype of a variable.
a=15
print("15: " , type(a))
a=7.5
print("7.5: " , type(a))
a='Hello'
print("Hello: " , type(a))
a=7+5j
print("7+5j: " , type(a))
a=[1,2,3]
print("[1,2,3]: " , type(a))
a={1,2,3}
print("{1,2,3}: " , type(a))

ch='A'
print("A : ", type(ch))

s="Bharat"
for i in s: print(i)
print("Uppercase : " , s[0].isupper())
print("Lowercase : " , s[1].islower())