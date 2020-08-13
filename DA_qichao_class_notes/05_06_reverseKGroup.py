#!/usr/bin/env python
# coding:utf-8

"""
数组 & 链表
Array & Linked List
"""

# ================================================================================
"""
LeetCode 25

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


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def is_need_reverse(self, head, k):
        # 判断以 head 为头结点的子链表，是否需要翻转
        for n in range(k):
            if head is None:
                return False
            head = head.next
        return True

    def reverseList(self, before ,head, k):
        # 翻转一个大链表的 从 head 开始的 k 个节点
        # before: head 的前一个节点
        prev, cur = before, head
        for n in range(k):
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
            if n == k - 1:
                head.next = cur
                before.next = prev
            pass
        # 翻转后子链表的 头、尾、尾的下一个节点
        return prev, head, cur

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        head_real = head
        need_reverse = self.is_need_reverse(head, k)
        if need_reverse:
            before = ListNode(None)
            head_begin, head_end, head_next = self.reverseList(before, head, k)
            head_real = head_begin
            #
            while self.is_need_reverse(head_next, k):
                head_begin, head_end, head_next = self.reverseList(head_end, head_next, k)
                pass
        return head_real
# ================================================================================


length = 7
k = 3

# 构建单链表
nextnode = None
for n in range(length):
    node = ListNode(length-n)
    if n == 0:
        tail = node
    elif n == length - 1:
        head = node
    node.next = nextnode
    nextnode = node
    pass


# 逐个打印链表节点的值
def print_ll(head):
    while head:
        print head.val
        head = head.next
        pass
    print

# 反转前
print_ll(head)

head_new = head
for i in range(k - 1):
    head_new = head_new.next

# 反转
Solution().reverseKGroup(node, k)

# 反转后
print_ll(head_new)
# ================================================================================
# ================================================================================
