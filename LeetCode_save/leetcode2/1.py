#!/usr/bin/env python
# coding:utf-8

"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def length_of(linknode):
    length = 1
    while hasattr(linknode, 'next') and linknode.next is not None:
        length += 1
        linknode = linknode.next
    return length


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        answer = ListNode(0)
        answer_final = answer
        carry = 0
        while l1 and l2:
            sum = l1.val + l2.val + answer.val
            val = sum % 10
            carry = sum / 10
            answer.val = val
            l1 = l1.next
            l2 = l2.next
            if carry or l1 or l2:
                answer.next = ListNode(carry)
                answer = answer.next

        while l1:
            sum = l1.val + answer.val
            val = sum % 10
            carry = sum / 10
            answer.val = val
            l1 = l1.next
            if carry or l1:
                answer.next = ListNode(carry)
                answer = answer.next
                pass

        while l2:
            sum = l2.val + answer.val
            val = sum % 10
            carry = sum / 10
            answer.val = val
            l2 = l2.next
            if carry or l2:
                answer.next = ListNode(carry)
                answer = answer.next
                pass

        ret = []
        while answer_final:
            print answer_final.val
            ret.append(answer_final.val)
            answer_final = answer_final.next

        return ret


a1 = ListNode(2)
a2 = ListNode(4)
a3 = ListNode(3)
a1.next = a2
a2.next = a3

b1 = ListNode(5)
b2 = ListNode(6)
b3 = ListNode(4)
b1.next = b2
b2.next = b3

so = Solution()
so.addTwoNumbers(a1, b1)


# print length_of(a1)
# print length_of(b1)
