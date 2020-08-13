#!/usr/bin/env python
# coding:utf-8

"""
k个一组翻转链表

给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
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
class Solution(object):
    """
    """
    def is_need_reverse(self, head, k):
        # 注意极端情况: [1]k == 1 [2]head 为空
        if k == 1 or not head:
            return False
        for n in range(k - 1):
            head = head.next
            if head is None:
                return False
            pass
        return True

    def reverseList(self, prior, head, k):
        pre = None
        cur = head
        for i in range(k):
            nn = cur.next
            cur.next = pre
            pre = cur
            cur = nn
            pass
        if prior:
            prior.next = pre  # 当前小组的头结点
        head.next = cur  # 下一个小组的头结点
        # 返回: 翻转后的 头结点、尾结点、下一个小组的头结点
        return pre, head, head.next

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 一次翻转都不需要
        if not self.is_need_reverse(head, k):
            return head
        # 至少需要一次翻转
        head_new, tail_new, head_next = self.reverseList(None, head, k)
        head_first = head_new
        while self.is_need_reverse(head_next, k):
            head_new, tail_new, head_next = self.reverseList(tail_new, head_next, k)
            pass
        return head_first

# ================================================================================
# 测试代码

length = 7
k = 3

# 构建单链表
head = ListNode(1)
pointer = head
for n in range(2, 8):
    head.next = ListNode(n)
    head = head.next
    pass

# 反转前
print_ll(pointer)

head_new = pointer
for i in range(k - 1):
    head_new = head_new.next

# 反转
Solution().reverseKGroup(pointer, k)

# 反转后
print_ll(head_new)
# ================================================================================
# ================================================================================
