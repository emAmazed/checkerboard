#!/usr/local/bin/python3.4
import sys

header = "++++ Hello Dev Meeting Python Exercise 101 ++++"

# print something
print("+" * len(header))
print(header)
print("+" * len(header))

'''
# Strings have various escapes.
print("Hi\nthere,\thow \141\x72\145\x20you?")

# Raw strings ignore them.
print(r"Hi\nthere,\thow \141\x72\145\x20you?")

# Very useful when building file paths on Windows.
badpath = 'C:\that\new\stuff.txt';
print(badpath)
path = r'C:\that\new\stuff.txt';
print(path)

# input/output
f = open('worksheet','r')
print(f.read())

f = open('worksheet','r')
line = f.readline()
while line:
  print(line)
  line = f.readline()

line = sys.stdin.readline()

while line:
  print(line)
  line = sys.stdin.readline()
'''

# print out a checker board
while True:
  matrix = input("number of row/column?\n")
  print( int(matrix) * "+")


