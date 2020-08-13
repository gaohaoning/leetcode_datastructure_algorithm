#!/usr/bin/env python
# coding:utf-8

"""
奇偶链表

给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

示例 1:

输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL
示例 2:

输入: 2->1->3->5->6->4->7->NULL
输出: 2->3->6->7->1->5->4->NULL
说明:

应当保持奇数节点和偶数节点的相对顺序。
链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
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
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        注意: 尾结点 next 要置空
        """
        if not head or not head.next:
            return head
        odd = head_odd = head
        even = head_even = head.next
        while odd.next.next and even.next.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd = odd.next
            even = even.next
            pass
        if not odd.next.next:
            # 节点个数为偶数
            odd.next = head_even
            even.next = None
            pass
        elif not even.next.next:
            # 节点个数为奇数
            odd.next = odd.next.next
            odd = odd.next
            odd.next = head_even
            even.next = None
            pass
        return head_odd


# ================================================================================
# ================================================================================
a0 = ListNode(0)
a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)

a0.next = a1
a1.next = a2
a2.next = a3
a3.next = a4


print_ll(a0)

so = Solution()
an = so.oddEvenList(a0)

print_ll(an)
# ================================================================================
