#!/usr/bin/env python
# coding:utf-8

"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# ================================================================================
# 方法1 笨方法, 需要额外空间(OK)
"""
对于多路归并排列，可以使用优先队列解决。
依次将list中的ListNode弹出，然后一次添加到一个优先队列中，
最后将优先队列中ListNode依次弹出，并且添加到result中即可。
"""
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        if not lists:
            return None
        # 优先队列
        heap = []
        for i, h in enumerate(lists):
            while h:
                heapq.heappush(heap, h.val)
                h = h.next
                pass
            pass
        if not heap:
            return None
        #
        node = ListNode(heapq.heappop(heap))
        head = node
        while heap:
            node.next = ListNode(heapq.heappop(heap))
            node = node.next
            pass
        return head

# ================================================================================
# 方法2(调用合并2个链表的函数进行 reduce 操作)
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 需要额外加入对链表为空列表([])的处理
        if not l1:
            return l2
        elif not l2:
            return l1
        #
        dummy = ListNode(None)
        dummy.next = l1
        pre = dummy
        cur = l1
        while l2:
            if cur is None or l2.val < cur.val:
                l2_next = l2.next
                l2.next = cur
                pre.next = l2
                pre = pre.next
                l2 = l2_next
            else:
                pre = pre.next
                cur = cur.next
            pass
        return dummy.next
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        ret = reduce(self.mergeTwoLists, lists)
        return ret

# ================================================================================
# 方法3(两两合并)
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 需要额外加入对链表为空列表([])的处理
        if not l1:
            return l2
        elif not l2:
            return l1
        #
        dummy = ListNode(None)
        dummy.next = l1
        pre = dummy
        cur = l1
        while l2:
            if cur is None or l2.val < cur.val:
                l2_next = l2.next
                l2.next = cur
                pre.next = l2
                pre = pre.next
                l2 = l2_next
            else:
                pre = pre.next
                cur = cur.next
            pass
        return dummy.next
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        #
        length = len(lists)
        n_groups = length / 2 + 1 if length % 2 else length / 2
        #
        head = lists[0]
        while length > 1:
            lists_new = []
            for n in range(n_groups):
                # head = lists_new.append(self.mergeTwoLists(lists[2*n], lists[2*n + 1]))
                head = self.mergeTwoLists(lists[2*n], lists[2*n + 1] if 2*n+1 < length else None)
                lists_new.append(head)
                pass
            lists = lists_new
            length = len(lists)
            n_groups = length / 2 + 1 if length % 2 else length / 2
            pass
        return head
# ================================================================================
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
# ================================================================================


a1 = ListNode(1)
a2 = ListNode(4)
a3 = ListNode(5)
a1.next = a2
a2.next = a3

b1 = ListNode(1)
b2 = ListNode(3)
b3 = ListNode(4)
b1.next = b2
b2.next = b3

c1 = ListNode(2)
c2 = ListNode(6)
c1.next = c2

print_ll(a1)
print_ll(b1)
print_ll(c1)

so = Solution()
merged = so.mergeKLists([a1, b1, c1])
print_ll(merged)

merged = so.mergeKLists([])
print_ll(merged)

merged = so.mergeKLists([[]])
print_ll(merged)
