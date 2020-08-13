#!/usr/bin/env python
# coding:utf-8

"""
剑指Offer
面试题26：复杂链表的复制
"""
"""
复制带随机指针的链表

示例：

输入：
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

解释：
节点 1 的值是 1，它的下一个指针和随机指针都指向节点 2 。
节点 2 的值是 2，它的下一个指针指向 null，随机指针指向它自己。

提示：
你必须返回给定头的拷贝作为对克隆列表的引用。
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


# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
# ================================================================================
# ================================================================================
"""
思路:
先遍历一遍一遍创建节点, 用一个 dict 记录旧节点和新节点对应关系
再遍历一遍，给新节点的 next 和 random 赋值
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dict_old_new = {}
        a = head
        b = head
        while a:
            dict_old_new[a] = Node(a.val, None, None)
            a = a.next
            pass
        while b:
            dict_old_new[b].next = dict_old_new.get(b.next)
            dict_old_new[b].random = dict_old_new.get(b.random)
            b = b.next
            pass
        return dict_old_new.get(head)
# ================================================================================
# ================================================================================
# ================================================================================
