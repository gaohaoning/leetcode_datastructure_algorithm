#!/usr/bin/env python
# coding:utf-8

"""
创建链表
"""


def print_ll(head):
    s = ''
    while head:
        s += '%s' % head.val
        if head.next:
            s += '->'
        head = head.next
        pass
    print s
    pass


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# ================================================================================
# [1] 头插法
dummy = ListNode(None)
for n in range(10):
    node = ListNode(n)
    node.next = dummy.next
    dummy.next = node
    pass

print_ll(dummy.next)
# ================================================================================
# [2] 尾插法
dummy = ListNode(None)
cur = dummy
for n in range(10):
    cur.next = ListNode(n)
    cur = cur.next
    pass

print_ll(dummy.next)
# ================================================================================
# ================================================================================
