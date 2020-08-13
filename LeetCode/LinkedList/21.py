#!/usr/bin/env python
# coding:utf-8

"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# [1] 需要额外存储空间(OK)
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = l1
        s2 = l2
        dummy = ListNode(None)
        cur = dummy
        while s1 or s2:
            if s2 is None or (s1 and s1.val <= s2.val):
                cur.next = ListNode(s1.val)
                s1 = s1.next
                pass
            elif s1 is None or (s2 and s1.val > s2.val):
                cur.next = ListNode(s2.val)
                s2 = s2.next
                pass
            cur = cur.next
        return dummy.next


# [2] 不占用额外空间(OK)
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = l1
        pre = dummy
        cur = l1
        while l2:
            if cur is None or l2.val < cur.val:
                l2_next = l2.next
                l2.next = cur
                pre.next = l2
                pre = pre.next
                l2 = l2_next
            else:
                pre = pre.next
                cur = cur.next
            pass
        return dummy.next


# ================================================================================


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(4)
a1.next = a2
a2.next = a3

b1 = ListNode(1)
b2 = ListNode(3)
b3 = ListNode(4)
b1.next = b2
b2.next = b3

so = Solution()
so.mergeTwoLists(a1, b1)
