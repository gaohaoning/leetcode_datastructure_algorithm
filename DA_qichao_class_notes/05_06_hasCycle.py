#!/usr/bin/env python
# coding:utf-8

"""
数组 & 链表
Array & Linked List
"""

# ================================================================================
"""
LeetCode 141

给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# [1] 基础方法，遍历(OK)
# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         set_next = set()
#         pre = ListNode(None)
#         pre.next = head
#         while pre.next:
#             if pre.next not in set_next:
#                 set_next.add(pre.next)
#                 pre = pre.next
#             else:
#                 return True
#         return False


# [2] 快慢指针(OK)
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        while hasattr(fast, 'next') and hasattr(fast.next, 'next'):
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

# ================================================================================
# ================================================================================
