#!/usr/bin/env python
# coding:utf-8

"""
删除排序链表中的重复元素 II

给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3

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
# 方法1 (比较笨)(OK)
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        需要注意的特殊情况:
            1.去重后变成空链表
            2.重复的值出现3次
        """
        if not head:
            return head
        l = []
        s = set()
        cur = head
        while cur:
            v = cur.val
            cur = cur.next
            if v not in s:
                l.append(v)
                s.add(v)
            else:
                if v in l:
                    l.remove(v)
                    pass
                pass
            pass
        # 注意: 特殊情况,去重后变成空链表
        if not l:
            return None
        #
        first = ListNode(l[0])
        cur = first
        for n in range(1, len(l)):
            cur.next = ListNode(l[n])
            cur = cur.next
            pass
        return first
# ================================================================================
# 方法2 (更优解)
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        需要注意的特殊情况:
            1.去重后变成空链表
            2.重复的值出现3次
                2.1 重复的值出现3次或以上，而且位于末端
        """
        if not head or not head.next:
            return head
        #
        h = ListNode(None)
        h.next = head
        pre = h
        cur = head
        while cur and cur.next:
            if pre.next.val != cur.next.val:
                pre = cur
                cur = cur.next
            else:
                while cur.next and pre.next.val == cur.next.val:
                    cur = cur.next
                    pass
                pre.next = cur.next
                cur = cur.next
                pass
            pass
        return h.next

# ================================================================================


a1 = ListNode(1)
a2 = ListNode(1)
a1.next = a2


so = Solution()
print_ll(a1)
a1 = so.deleteDuplicates(a1)
print_ll(a1)

