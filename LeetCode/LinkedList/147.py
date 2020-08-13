#!/usr/bin/env python
# coding:utf-8

"""
对链表进行插入排序

插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。


插入排序算法：

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。


示例 1：

输入: 4->2->1->3
输出: 1->2->3->4
示例 2：

输入: -1->5->3->4->0
输出: -1->0->3->4->5
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
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        dummy_new = ListNode(None)
        dummy_new.next = None
        while head:
            cur = head
            head = head.next
            start = dummy_new
            # 需要分别考虑插入位置: 头数、中部、尾部
            while start.next and start.next.val < cur.val:
                start = start.next
                pass
            tail = start.next
            start.next = cur
            cur.next = tail
            #
            pass
        return dummy_new.next
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
b = so.insertionSortList(a1)
print_ll(b)
# ================================================================================
