#!/usr/bin/python3
import sys

name = ""

print("Hello, what's your name?")
print("name: ", end='')
name = sys.stdin.readline

print("Hello ", name)
