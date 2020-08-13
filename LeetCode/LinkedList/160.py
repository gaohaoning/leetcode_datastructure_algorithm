#!/usr/bin/env python
# coding:utf-8

"""
编写一个程序，找到两个单链表相交的起始节点。

注意：

如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
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
# 方法1
"""
求相交结点的思路:
求出链表长度的差值，长链表的指针先想后移动lenA-lenB。然后两个链表一起往后走，若结点相同则第一个相交点。
"""
def length(ln):
    if not ln:
        return 0
    count = 1
    while ln.next:
        count += 1
        ln = ln.next
        pass
    return count

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1 = length(headA)
        l2 = length(headB)
        if l1 >= l2:
            big, small = headA, headB
        else:
            big, small = headB, headA
            pass
        delta = abs(l1 - l2)
        for n in range(delta):
            big = big.next
            pass
        while big != small:
            big = big.next
            small = small.next
            # 如果没有交点，big 和 small 会同时到达尾部
            if not big:
                return None
            pass
        return big

# ================================================================================
# 方法2(牛逼)
"""
2个链表，任意一个走到头后，从另一个的头开始走，这样2个链表必然会同步走到相遇点
"""
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        s1 = headA
        s2 = headB
        while s1 is not s2:
            """
            此处用于做判断的是 s1 而不是 s1.next
            目的是: 对于不相交的两个链表，让他们俩最终共同走到 None
            如果用 s1.next 做判断，则两个不想交链表，永远无法停止跳跃
            """
            """
            即: 对于不想交的两个链表，交点是 None
            """
            # 走法1: 永远走不到尾部节点的 next(None)
            # s1 = s1.next if s1.next else headB
            # s2 = s2.next if s2.next else headA
            # 走法2: 每个链表都走到尾部节点的 next(None)，下一步再到另一个链表头部
            s1 = s1.next if s1 else headB
            s2 = s2.next if s2 else headA
            pass
        return s1

# ================================================================================
a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a1.next = a2
a2.next = a3

b1 = ListNode(4)
b2 = ListNode(5)
# b1.next = a3
b1.next = b2

so = Solution()
print_ll(a1)
print_ll(b1)

print '... start'
ret = so.getIntersectionNode(a1, b1)
print '... stop'
print ret.val if ret else None
