#to find sum of 2 numbers.
import argparse

#Create ArgumentParser class object
parser = argparse.ArgumentParser(description="The program calculates sum of 2 numbers.")

#ADD 2 NUMBERS WITH NAMES N1 AND N2
parser.add_argument("n1",type=float,help="Input number 1: ")
parser.add_argument("n2",type=float,help="Input number 2: ")

#RETRIEVE THE ARGUMENTS PASSED TO PROGRAM
args=parser.parse_args()

#Convert the values n1 and n2 to float and then add them
sum=float(args.n1)+float(args.n2)
print("Sum is: " , sum)