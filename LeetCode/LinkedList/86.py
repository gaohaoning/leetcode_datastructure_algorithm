#!/usr/bin/env python
# coding:utf-8

"""
分隔链表

给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
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
# 方法1 (OK)
class Solution(object):
    def deleteNode(self, pre_node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        pre_node.next = pre_node.next.next

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        #
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy
        #
        dummy_small = ListNode(None)
        head_small = dummy_small
        while pre.next:
            if pre.next.val < x:
                head_small.next = ListNode(pre.next.val)
                head_small = head_small.next
                self.deleteNode(pre)
                pass
            else:
                pre = pre.next
            pass
        head_small.next = dummy.next
        return dummy_small.next


# ================================================================================
# 方法2 (OK)
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        head1 = dummy_1 = ListNode(None)
        head2 = dummy_2 = ListNode(None)
        while head:
            if head.val < x:
                head1.next = ListNode(head.val)
                head1 = head1.next
            else:
                head2.next = ListNode(head.val)
                head2 = head2.next
                pass
            head = head.next
            pass
        head1.next = dummy_2.next
        return dummy_1.next
# ================================================================================
# ================================================================================
