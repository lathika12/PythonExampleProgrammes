#Parsing command line args
#To find square of a given number
import argparse
#Create ArgumentParser class object.
parser=argparse.ArgumentParser(description='This program displays the square value of given number')
#Add one argument with the name num and type as integer
parser.add_argument("num",type=int,help="Please input integer type number.")
#retrieving the arguments passed to the program
args=parser.parse_args()
#find the square of the argument passed
result=args.num**2
print("Square Value: ", result)