#!/usr/bin/env python
# coding:utf-8

"""
重排链表

给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
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
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        deq = []
        while head:
            deq.append(head)
            head = head.next
            pass
        cur = deq.pop(0)
        while deq:
            cur.next = deq.pop()
            cur = cur.next
            if deq:
                cur.next = deq.pop(0)
                cur = cur.next
            pass
        # 注意: 不要忘了新链表的尾结点处理
        cur.next = None
        return
# ================================================================================
# ================================================================================


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a1.next = a2
a2.next = a3
a3.next = a4

print_ll(a1)
so = Solution()
so.reorderList(a1)
print_ll(a1)
# ================================================================================
