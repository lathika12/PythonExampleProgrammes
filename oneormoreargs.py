import argparse

parser=argparse.ArgumentParser()

parser.add_argument('nums',nargs='+')

args = parser.parse_args()

for x in args.nums:
	print(x)