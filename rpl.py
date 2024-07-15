from sys import argv
from argparse import ArgumentParser
from replace import manager

parser = ArgumentParser(description="Your command-line application")
parser.add_argument("-m", "--message", required=False, help="The message to be used")
parser.add_argument("-n", "--name", required=False, help="The name to be used")
args = parser.parse_args()
message = args.message
name = args.name
print(message)
print(name)



# python rpl.py file_address destination -attr ... -ign ... run
