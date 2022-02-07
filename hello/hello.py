#!/usr/bin/python3
import sys

name = "xx"

print("Hello, what's your name?")
print("My name is", end=' ', flush=True)
#print("name: ")
name = sys.stdin.readline()

print("Hello", name, ".", end='')
