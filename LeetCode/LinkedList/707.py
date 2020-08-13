#!/usr/bin/env python
# coding:utf-8

"""
设计链表的实现。

您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。
val 是当前节点的值，next 是指向下一个节点的指针/引用。
如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。

在链表类中实现这些功能：

get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。
deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。


示例：

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1,2);   //链表变为1-> 2-> 3
linkedList.get(1);            //返回2
linkedList.deleteAtIndex(1);  //现在链表是1-> 3
linkedList.get(1);            //返回3


提示：

所有值都在 [1, 1000] 之内。
操作次数将在  [1, 1000] 之内。
请不要使用内置的 LinkedList 库。
"""


def print_ll(ll):
    head = ll.dummy.next
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
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList(object):
    """
    注意:
    任何操作，都要考虑 dummy 和 tail 这2个指针的处理!
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dummy = ListNode(None)
        self.tail = None

    def getNode(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        pointer = self.dummy.next
        for n in range(index):
            # 注意: pointer 必须为非空节点
            # 注意: pointer.next 不为 None 时，才能在指针后移后取数值
            if pointer and pointer.next:
                pointer = pointer.next
            else:
                return -1
            pass
        return pointer

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        # 需要处理特殊情况: 初始空链表
        pointer = self.dummy.next
        if pointer is None:
            return -1
        #
        for n in range(index):
            # 注意: pointer 必须为非空节点
            # 注意: pointer.next 不为 None 时，才能在指针后移后取数值
            if pointer and pointer.next:
                pointer = pointer.next
            else:
                return -1
            pass
        return pointer.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        node = ListNode(val)
        node.next = self.dummy.next
        self.dummy.next = node
        if not self.tail:
            self.tail = node

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        node = ListNode(val)

        if not self.tail:
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        # 需要考虑在第 0 个节点前插入的情况，此时用 self.getNode(-1) 无法获取前驱节点
        if index == 0:
            self.addAtHead(val)
            return
        #
        pre = self.getNode(index - 1)
        cur = self.getNode(index)
        # 需要处理插入时，index 超过链表长的情况
        if cur == -1:
            # 找不到节点的情况有2种:
            # [1] index 超限
            # [2] index == 表长(如果 index 等于链表的长度，则该节点将附加到链表的末尾)
            if pre != -1:  # (index 等于链表的长度)
                self.addAtTail(val)
                pass
            else:
                return
        node = ListNode(val)
        # 如果 index 大于链表长度，则不会插入节点。
        if cur == -1:
            return
        node.next = cur
        pre.next = node

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        cur = self.getNode(index)
        if cur == -1:
            return
        pre = self.getNode(index - 1)
        pre.next = cur.next
        # 注意: 删除节点时，也要记得处理尾节点
        if self.tail == cur:
            self.tail = pre

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# ================================================================================
# 测试代码(已验证通过)

# linkedList = MyLinkedList()
# print_ll(linkedList)
# linkedList.addAtHead(1)
# print_ll(linkedList)
# linkedList.addAtTail(3)
# print_ll(linkedList)
# linkedList.addAtIndex(1, 2)
# print_ll(linkedList)
# print linkedList.get(1)
# print_ll(linkedList)
# linkedList.deleteAtIndex(1)
# print_ll(linkedList)
# print linkedList.get(1)
# ================================================================================
# 测试代码(已验证通过)

# ll = MyLinkedList()
# # ll.addAtHead(None)
# ll.addAtHead(1)
# ll.addAtIndex(1, 2)
# print ll.get(0)
# print ll.get(3)
# print ll.get(2)
# ================================================================================
# 测试代码(已验证通过)

# ll = MyLinkedList()
# print ll.get(0)
# ll.addAtIndex(1, 2)
# print_ll(ll)
# print ll.get(0)
# print ll.get(1)
# ll.addAtIndex(0, 1)
# ll.get(0)
# ll.get(1)
# ================================================================================
# 测试代码(已验证通过)

# ll = MyLinkedList()
# ll.addAtHead(1)
# print_ll(ll)
#
# ll.addAtIndex(1, 2)
# print_ll(ll)
#
# print ll.get(1)
# print ll.get(0)
# print ll.get(2)
# ================================================================================
# 测试代码(已验证通过)

ll = MyLinkedList()


ll.addAtHead(8)
ll.get(1)
ll.addAtTail(81)
ll.deleteAtIndex(2)
ll.addAtHead(26)
ll.deleteAtIndex(2)
ll.get(1)

print ll.tail.val

print '=============================='
print_ll(ll)
print '=============================='

ll.addAtTail(24)
ll.addAtHead(15)
ll.addAtTail(0)
ll.addAtTail(13)
ll.addAtTail(1)
ll.addAtIndex(6, 33)
print '=============================='
print_ll(ll)
print '=============================='

print ll.get(6)

# ll.addAtIndex(2, 91)
# ll.addAtHead(82)
# ll.deleteAtIndex(6)
# ll.addAtIndex(4, 11)
# ll.addAtHead(3)
# ll.addAtIndex(7, 14)
# ll.deleteAtIndex(1)
# print ll.get(6)
# ll.addAtTail(99)
# ll.deleteAtIndex(11)
# ll.deleteAtIndex(7)
# ll.addAtTail(5)
# ll.addAtTail(92)
# ll.addAtIndex(7, 92)
# ll.addAtHead(57)
# print ll.get(2)
# print ll.get(6)
# ll.addAtTail(39)
# ll.addAtTail(51)
# ll.addAtTail(3)
# ll.addAtTail(22)
# ll.addAtIndex(5, 26)
# ll.addAtIndex(9, 52)
# ll.addAtHead(69)
# ll.addAtIndex(5, 58)
# ll.addAtTail(79)
# ll.addAtHead(7)
# ll.addAtHead(41)
# ll.addAtHead(33)
# ll.addAtHead(88)
# ll.addAtHead(44)
# ll.addAtHead(8)
# ll.addAtTail(72)
# ll.addAtHead(93)
# ll.deleteAtIndex(18)
# ll.addAtHead(1)
# print ll.get(9)
# ll.addAtHead(46)
# print ll.get(9)
# ll.addAtHead(92)
# ll.addAtHead(71)
# ll.addAtHead(69)
# ll.addAtIndex(11, 54)
# ll.deleteAtIndex(27)
# ll.addAtTail(83)
# ll.deleteAtIndex(12)
# print ll.get(20)
# ll.addAtIndex(19, 97)
# ll.addAtHead(77)
# ll.addAtTail(36)
# ll.deleteAtIndex(3)
# ll.addAtHead(35)
# ll.addAtIndex(16, 68)
# ll.deleteAtIndex(22)
# ll.deleteAtIndex(36)
# ll.deleteAtIndex(17)
# ll.addAtHead(62)
# ll.addAtTail(89)
# ll.addAtTail(61)
# ll.addAtHead(6)
# ll.addAtTail(92)
# ll.addAtIndex(28, 69)
# ll.deleteAtIndex(23)
# ll.deleteAtIndex(28)
# ll.addAtIndex(7, 4)
# ll.addAtHead(0)
# ll.addAtHead(24)
# ll.addAtTail(52)
# print ll.get(1)
# ll.addAtIndex(23, 3)
# print ll.get(7)
# ll.addAtHead(6)
# ll.addAtHead(68)
# ll.addAtHead(79)
# ll.addAtIndex(45, 90)
# ll.addAtIndex(41, 52)
# print ll.get(28)
# ll.addAtHead(25)
# print ll.get(9)
# print ll.get(32)
# ll.addAtTail(11)
# ll.addAtHead(90)
# ll.addAtHead(24)
# ll.addAtTail(98)
# ll.addAtTail(36)
# print ll.get(34)
# ll.addAtTail(26)
# ================================================================================
