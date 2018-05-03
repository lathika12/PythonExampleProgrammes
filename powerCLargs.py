#to find power value of a number.
import argparse

#Call the ArgumentParser()
parser=argparse.ArgumentParser()

#Add the arguments to the parser.
parser.add_argument("nums",nargs=2)

#Retrieve the arguments into args object
args=parser.parse_args()

#find the power value
#args.nums represents a list
print('Number=',args.nums[0])
print('Its power:' , args.nums[1])

#Convert args into folat and find result
pow=float(args.nums[0])**float(args.nums[1])
print('Power of {0} to {1} is {2}'.format(args.nums[0],args.nums[1],pow))