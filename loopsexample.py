#While Loop
#to display numbers from 1 to 5
x=1
while x<=5:
	print(x)
	x+=1
print('End')

#For loop
# to display each char from a string
str='Hello'
for ch in str:
	print(ch)

#display each char from string using sequence index
n=len(str)
for i in range(n):
	print(str[i])

#odd numbers between 1 and 10
for i in range(1,10,2):
	print(i)


#To display numbers in descending order
for x in range(10,0,-1):
	print(x)

#display list of elements
lst=['a',10,25.3,"America"]
for element in lst:
	print(element)

#Sum of list of numbers
list=[10,20,30,40,50]
sum=0;
for s in range(len(list)):
	sum+=list[s]
	s+=1;
print('Sum: ' , sum ,' for the list : ' , list)

#Infinity loop
#Press Ctrl+C or Ctrl+Z to abort loop
while(True):
	print('Hai')