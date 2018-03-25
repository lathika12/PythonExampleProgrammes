#Program representing binary octal, hexadecimal and decimal system
n1=0O17 # Octal - 0postfixed with Capital 'O' or small 'o'
n2=0B11110010 # Binary - 0postfixed with Capital 'B' or small 'b'
n3=0X1c2 # Hexadecimal - 0postfixed with Capital 'X' or small 'x'

n=int(n1)
print("Octal 17 : " , n)
n=int(n2)
print("Binary 11110010 : " , n)
n=int(n3)
print("Hexadecimal 1c2 : " , n)

#Converting an integer to one of the above formats 
n=20
print("Octal form of 20 : " , oct(n))
print("Hexadecimal form of 20 : " , hex(n) )
print("Binary form of 20 : " , bin(n))

#Program to convert strings another expected base
str="1c2" #1c2 is a hexadecimal number
n=int(str,16)
print("Printing the integer form of hexadecimal 1c2 in str : " , n)
str="11101100"
n=int(str,2)
print("Printing the integer form of binary 11101100 in str : " , n)
str="17"
n=int(str,8)
print("Printing the integer form of octal 17 in str : " , n)