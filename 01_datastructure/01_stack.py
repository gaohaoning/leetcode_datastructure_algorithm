#!/usr/bin/env python
# coding:utf-8

"""
Using Lists as Stacks
    To add an item to the top of the stack, use append().
    To retrieve an item from the top of the stack, use pop() without an explicit index.
"""

stack = range(10)
print stack

print stack.pop()
print stack

print stack.append(99)
print stack
