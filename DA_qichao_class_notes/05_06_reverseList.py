#!/usr/bin/env python
# coding:utf-8

"""
数组 & 链表
Array & Linked List
"""

# ================================================================================
"""
LeetCode 206

反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, cur = None, head
        while cur:
            # [1]
            # next_node = cur.next
            # cur.next = prev
            # prev = cur
            # cur = next_node
            # [2]
            cur.next, prev, cur = prev, cur, cur.next  # !!!!!!!!!!
            pass
        return prev


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
Solution().reverseList(node)

# 反转后
print_ll(tail)
# ================================================================================
# ================================================================================
