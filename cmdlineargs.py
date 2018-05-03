#Command Line Arguments
import sys
n=len(sys.argv)
args=sys.argv
print("Number of command line arguments is: " , n)
print("The args are : " , args)
print("Arguments one by one : ")
for x in args:
	print(x)