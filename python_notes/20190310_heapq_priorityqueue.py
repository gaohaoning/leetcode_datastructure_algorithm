#!/usr/bin/env python
# coding:utf-8

"""
Python 笔记
"""

# ================================================================================
"""
堆 & 优先队列
heapq & Queue.PriorityQueue

（优先队列 Queue.PriorityQueue 本身也是基于 heapq 实现的）
"""

import heapq
from Queue import PriorityQueue
# ================================================================================

def heapsort(iterable):
    # 由于 heap 是通过 list 实现的，我们可以直接用 list 创建 heap：
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]


print heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])

# ================================================================================
"""
queue.PriorityQueue 实际上只是对 heapq 的简单封装，直接使用其 heappush/heappop 方法：
"""

pq = PriorityQueue()
pq.put((2, 'C'))
pq.put((1, 'Python'))
pq.put((3, 'Js'))
print("Inside PriorityQueue: ", pq.queue)  # 内部存储
while not pq.empty():
    print(pq.get()[1])
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
