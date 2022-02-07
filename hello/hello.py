#!/usr/bin/python3
import sys

name = "xx"

print("Hello, what's your name?")
print("My name is", end=' ', flush=True)
name = sys.stdin.readline()

# name ended with a newline caracter, so I need to remove it.
name = name[:-1]
print("Hello " + name + ".")
