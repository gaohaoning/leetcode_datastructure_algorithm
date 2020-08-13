"""
栈 & 队列
Stack & Queue
"""

# ================================================================================
"""
LeetCode 232

使用栈实现队列的下列操作：

push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。
示例:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false
说明:

你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。
"""


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.stack_2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.stack_2:
            for n in range(len(self.stack)):
                self.stack_2.append(self.stack.pop())
                pass
        return self.stack_2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.stack_2:
            for n in range(len(self.stack)):
                self.stack_2.append(self.stack.pop())
                pass
        return self.stack_2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not (self.stack or self.stack_2)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# ================================================================================
"""
LeetCode 225

使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空
注意:

你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
"""


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self.queue = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        for n in range(len(self.queue) - 1):
            top = self.queue.popleft()
            self.queue.append(top)
        return self.queue.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        """
        Attention !!!
        top 时需要先 pop 出来，再 push 回去
        """
        value = self.pop()
        self.push(value)
        return value

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not len(self.queue)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# ================================================================================
