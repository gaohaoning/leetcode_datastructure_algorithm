#!/usr/bin/env python
# coding:utf-8

"""
旋转链表

给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
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
    def lentgh(self, head):
        if not head:
            return 0
        l = 1
        while head.next:
            head = head.next
            l += 1
            pass
        return l
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        """
        注意:
        不要去实际移动指针，而是现在数学层面计算有效的k值.
        避免k较大时出现内存问题
        """
        if not head:
            return head
        #
        l = self.lentgh(head)
        k = k % l
        if k == 0:
            return head
        #
        dummy = ListNode(None)
        dummy.next = head
        cur = head
        for _ in range(k):
            if cur.next:
                cur = cur.next
            else:
                cur = head
                pass
            pass
        #
        while cur.next:
            head = head.next
            cur = cur.next
            pass
        head_new = head.next
        cur.next = dummy.next
        head.next = None
        return head_new


# ================================================================================
# ================================================================================
# ================================================================================


a0 = ListNode(0)
a1 = ListNode(1)
a2 = ListNode(2)

a0.next = a1
a1.next = a2


print_ll(a0)

so = Solution()
an = so.rotateRight(a0, 4)
# an = so.rotateRight(a0, 2000000000)

print_ll(an)
