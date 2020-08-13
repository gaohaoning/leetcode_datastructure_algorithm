#!/usr/bin/env python
# coding:utf-8

"""
数组 & 链表
Array & Linked List
"""

# ================================================================================
"""
LeetCode 142

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# [1] 快慢指针(OK)
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        while hasattr(fast, 'next') and hasattr(fast.next, 'next'):
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                # slow 和 fast 相遇后，分别以 head 和 相遇点 为起点，每次走一步，在第 N 步后相遇，则 N 即为入环节点
                start1 = head  # 从头部开始走
                start2 = fast  # 从相遇点开始走
                while start1 != start2:
                    start1 = start1.next
                    start2 = start2.next
                return start1
                pass
        return None


# [2] 基础方法，遍历(OK)
# class Solution(object):
#     def detectCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         list_node = []
#         pre = ListNode(None)
#         pre.next = head
#         while pre.next:
#             if pre.next not in list_node:
#                 list_node.append(pre.next)
#                 pre = pre.next
#             else:
#                 return pre.next
#         return None
# ================================================================================
# ================================================================================
