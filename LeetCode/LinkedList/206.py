#!/usr/bin/env python
# coding:utf-8

"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
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
# 方法1: 利用3个指针, 遍历操作
"""
时间复杂度：O(n)
空间复杂度：O(1)
"""
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre = None
        cur = head
        while cur:
            # [1]
            nn = cur.next
            cur.next = pre
            pre = cur
            cur = nn
            # [2]
            #  cur.next, pre, cur = pre, cur, cur.next  # !!!!!!!!!!
        return pre

# ================================================================================
# 方法2: 递归法
"""
时间复杂度：O(n)
空间复杂度：O(1)
"""
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        # 递归
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
# ================================================================================


# 构建单链表
head = ListNode(1)
pointer = head
for n in range(2, 8):
    head.next = ListNode(n)
    head = head.next
    pass

# 反转前
print_ll(pointer)

# 反转
head_new = Solution().reverseList(pointer)

# 反转后
print_ll(head_new)
# ================================================================================
