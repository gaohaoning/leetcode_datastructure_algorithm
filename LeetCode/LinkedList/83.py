#!/usr/bin/env python
# coding:utf-8

"""
删除排序链表中的重复元素

给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3

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


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        pre = head
        cur = head.next
        s = set([head.val])
        while cur:
            if cur.val in s:
                pre.next = cur.next
                cur = cur.next
            else:
                s.add(cur.val)
                pre = cur
                cur = cur.next
            pass
        return head


# ================================================================================


a1 = ListNode(1)
a2 = ListNode(1)
a3 = ListNode(4)
a1.next = a2
a2.next = a3

b1 = ListNode(1)
b2 = ListNode(3)
b3 = ListNode(4)
b1.next = b2
b2.next = b3

so = Solution()
print_ll(a1)
so.deleteDuplicates(a1)
print_ll(a1)

