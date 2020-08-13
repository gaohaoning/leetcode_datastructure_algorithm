#!/usr/bin/env python
# coding:utf-8

"""
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
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
"""
方法1: 笨方法
求得字符串后逆向切片，判断跟反转前是否相等
"""
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        c = []
        while head:
            c.append(head.val)
            head = head.next
            pass
        return c == c[::-1]

# ================================================================================
"""
方法2: 利用栈
"""
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []
        start = head
        while head:
            stack.append(head.val)
            head = head.next
        while start:
            if start.val != stack.pop():
                return False
            start = start.next
        return True

# ================================================================================
"""
方法3: 更优解法
O(n) 时间复杂度和 O(1) 空间复杂度:
设置快慢指针，当快指针走完时，慢指针刚好走到中点，随即原地将后半段反转。然后进行回文判断。 
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
             cur.next, pre, cur = pre, cur, cur.next  # !!!!!!!!!!
        return pre
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dummy = ListNode(None)
        dummy.next = head
        slow = dummy
        fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            pass
        # if fast:
        #     # 节点为偶数
        #     h1 = dummy.next
        #     h2 = self.reverseList(slow.next)
        #     pass
        # else:
        #     # 节点为奇数
        #     h1 = dummy.next
        #     h2 = self.reverseList(slow.next)
        #     pass
        h1 = dummy.next
        h2 = self.reverseList(slow.next)
        while h2:
            if h1.val != h2.val:
                return False
            h1 = h1.next
            h2 = h2.next
            pass
        return True
# ================================================================================


a1 = ListNode(1)
a2 = ListNode(2)
# a3 = ListNode(3)
a1.next = a2
# a2.next = a3


so = Solution()
print so.isPalindrome(a1)
# ================================================================================
