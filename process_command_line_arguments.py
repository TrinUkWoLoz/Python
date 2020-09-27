#!/usr/bin/python3.8

#Module
import argparse

#Variable (parser) = module.class(ArgumentParser)
parser = argparse.ArgumentParser()

#Module.populate_parser(add_argument)
#parser 1-3 require at least 2 integers parser 4-7 take 1 or more
parser.add_argument('integers', metavar='N', type=int, nargs='+')
parser.add_argument('-f', '--foo', help='foo help')
parser.add_argument('-b', '--bar', help='bar help')
parser.add_argument('-z', '--baz', help='baz help')
parser.add_argument('-t', '--turn-on', action='store_true')
parser.add_argument('-x', '--exclude', action='store_false')
parser.add_argument('-s', '--start', action='store_true')

#variable(args) = module.convert the args at the command-line into an object with attributes(parse_args)
args = parser.parse_args()

print(args)







