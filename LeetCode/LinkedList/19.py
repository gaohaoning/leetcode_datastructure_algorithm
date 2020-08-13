#!/usr/bin/env python
# coding:utf-8

"""
删除链表的倒数第N个节点

给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？
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
# 方法1: 需要遍历2次(OK)
class Solution(object):
    def length(self, head):
        if not head:
            return 0
        cur = head
        n = 1
        while cur.next:
            cur = cur.next
            n += 1
            pass
        return n

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = self.length(head)
        # 注意极限条件: 链表为空 or 删除的节点为倒数第n个(第一个)
        if l == 0:
            return None
        if n == l:
            return head.next
        #
        pre = None
        cur = head
        for i in range(l - n):
            pre = cur
            cur = cur.next
            pass
        # 删除节点
        pre.next = cur.next
        return head
# ================================================================================
# 方法2: 使用一趟扫描实现(OK)
# 这个属于笨方法, 不提倡, 需要改进 !!!
class Solution(object):
    def is_del_node(self, node, n):
        for i in range(n):
            node = node.next
        return node is None

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 链表为空
        if not head:
            return head
        pre = None
        cur = head
        while not self.is_del_node(cur, n):
            pre = cur
            cur = cur.next
            pass
        if pre:
            # 指针有过移动, 即需要删除的不是头结点
            pre.next = cur.next
        else:
            # 指针没有移动过, 即需要删除的就是头结点
            head = head.next
        return head

# ================================================================================
# 方法3: 使用一趟扫描实现(最优解)(OK)
"""
最优解:
    本题需要维护两个指针，pre和end。
    一开始初始化时使得pre指针指向链表头节点，end指针指向pre+n的节点位置。
    然后同时往后移动pre和end指针位置，使得end指针指向最后一个节点，那么pre指针指向的则是end-n的节点位置
    （即倒数第n个元素的前一个节点），则将其删除。

链表长度为n时，算法复杂度O(n)。
"""
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 链表为空
        if not head:
            return head
        # 链表不为空
        start = head
        stop = head
        for i in range(n):
            stop = stop.next
            pass
        # 如果 stop 是 None, 说明需要删除的是第一个节点（倒数第n个）
        if not stop:
            return head.next
        # 同步移动 start 和 stop
        while stop.next:
            start = start.next
            stop = stop.next
            pass
        # start 和 stop 同步移动至 stop.next 为 None，则需要删除的节点是 start.next
        start.next = start.next.next
        return head
# ================================================================================
