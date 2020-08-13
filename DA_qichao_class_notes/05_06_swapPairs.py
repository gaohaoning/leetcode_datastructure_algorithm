#!/usr/bin/env python
# coding:utf-8

"""
数组 & 链表
Array & Linked List
"""

# ================================================================================
"""
LeetCode 24

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
给定 1->2->3->4->5, 你应该返回 2->1->4->3->5.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution(object):
#     def swapPairs(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         pointer = ListNode(None)
#         pre = pointer
#         pre.next = head
#         while pre.next and pre.next.next:
#             #
#             a = pre.next
#             b = a.next
#             #
#             a.next = b.next
#             b.next = a
#             pre.next = b
#             #
#             pre = a
#             pass
#         return pointer.next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pointer = ListNode(None)
        pre = pointer
        pre.next = head
        while pre.next and pre.next.next:
            #
            a, b = pre.next, pre.next.next
            #
            a.next, b.next, pre.next = b.next, a, b
            #
            pre = a
            pass
        return pointer.next

# ================================================================================
nextnode = None
# node_list = []
for n in range(5):
    node = ListNode(5-n)
    if n == 0:
        tail = node
    elif n == 4:
        head = node
    node.next = nextnode
    # node_list.append(node)
    nextnode = node
    pass


# 逐个打印链表节点的值
def print_ll(head):
    while head:
        print head.val
        head = head.next
        pass

# 反转前
print_ll(head)

# 反转
Solution().swapPairs(node)

# 反转后
print_ll(head)
# ================================================================================
