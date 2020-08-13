#!/usr/bin/env python
# coding:utf-8

"""
反转链表 II

反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
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
            nn = cur.next
            cur.next = pre
            pre = cur
            cur = nn
        return pre
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not m >= 1 or not n >= m:
            return head
        dummy = ListNode(None)
        dummy.next = head
        slow = dummy
        fast = head
        for _ in range(n - m):
            fast = fast.next
            pass
        for _ in range(m - 1):
            slow = slow.next
            fast = fast.next
            pass
        # 此时 slow 为第 m-1 个，fast 为第 n 个
        nn = fast.next
        fast.next = None
        head_new = self.reverseList(slow.next)
        slow.next.next = nn
        slow.next = head_new
        #
        return dummy.next


# ================================================================================
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
head_new = Solution().reverseBetween(pointer, 2, 4)

# 反转后
print_ll(head_new)
# ================================================================================
