#!/usr/bin/env python
# coding:utf-8

"""
Using Lists as Queues
    It is also possible to use a list as a queue, however, lists are not efficient for this purpose.
    While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow.
    (because all of the other elements have to be shifted by one)

To implement a queue, use [collections.deque] which was designed to have fast appends and pops from both ends.
"""
"""
append(x)
    Add x to the right side of the deque.

appendleft(x)
    Add x to the left side of the deque.

extend(iterable)
    Extend the right side of the deque by appending elements from the iterable argument.

extendleft(iterable)
    Extend the left side of the deque by appending elements from iterable.
    Note, the series of left appends results in reversing the order of elements in the iterable argument.

pop()
    Remove and return an element from the right side of the deque. If no elements are present, raises an IndexError.

popleft()
    Remove and return an element from the left side of the deque. If no elements are present, raises an IndexError.

rotate(n)
    Rotate the deque n steps to the right.
    If n is negative, rotate to the left.
    Rotating one step to the right is equivalent to: d.appendleft(d.pop()).
"""

# [deque][list-like container with fast appends and pops on either end]
from collections import deque


deq = deque(range(5))
print deq
# deque([0, 1, 2, 3, 4])

deq.pop()
print deq
# deque([0, 1, 2, 3])

deq.popleft()
print deq
# deque([1, 2, 3])

deq.append(9)
print deq
# deque([1, 2, 3, 9])

deq.appendleft(-1)
print deq
# deque([-1, 1, 2, 3, 9])

deq.rotate(1)
print deq
# deque([9, -1, 1, 2, 3])

deq.rotate(-2)
print deq
# deque([1, 2, 3, 9, -1])
