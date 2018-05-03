#To find sum of even numbers
import sys

#Read CL args except the pgm name
args = sys.argv[1:]
print(args)

sum=0
#find sum of even args
for a in args:
	x=int(a)
	if x%2==0:
		sum+=x
print("Sum of evens: " , sum)