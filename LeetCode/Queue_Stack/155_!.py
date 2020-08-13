#!/usr/bin/env python
# coding:utf-8

"""
155. 最小栈
难度
简单

设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
"""
# ================================================================================
"""
思路:
    借用一个辅助栈 min_stack，用于存储 stack 中最小值。
    
    min_stack的作用是对stack中的元素做标记，标记的原则是min_stack中元素一定是降序的（栈底最大栈顶最小）。
    换个角度理解，min_stack等价于遍历stack所有元素，把升序的数字都删除掉，留下一个从栈底到栈顶降序的栈。
    本题要求获取最小值的复杂度是O(1)，因此须构建辅助栈，在push与pop的过程中始终保持辅助栈为一个降序栈。
        
时间复杂度(获取最小值):
    O(1)
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        """

        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
            pass

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            if self.stack.pop() == self.min_stack[-1]:
                self.min_stack.pop()
                pass
            pass

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1] if self.stack else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
