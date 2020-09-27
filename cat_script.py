#!/usr/bin/python3.8

#import module
import argparse

#Variable (parser) = module.class(ArgumentParser)
parser = argparse.ArgumentParser()

#module, populating with positional parameters
parser.add_argument('files', metavar='F', type=str, nargs='+')
parser.add_argument('-n', '--numbers', action='store_true',
        help='Print line numbers')

#parse_args = convert the args at the command-line into an object with attributes
args = parser.parse_args()

#prints file names to be displayed (args)
print(">>> parsed args: ", args)

#line_number variable = 1
line_number = 1
#for in_file_name variable in files positional parameter argument
for in_file_name in args.files:
#open file stated in positional paramter
    in_file = open(in_file_name)
#if there are psotional parameter line numbers (contents in file)
    if args.numbers:
#for each line read contents
        for line in in_file.readlines():
#print contents of each line
            print(f"\t{line_number}\t{line}", end="")
#repeat for each line of file
            line_number += 1
    else:
#if there are no extra lines then read
        print(in_file.read())