#!/usr/bin/env python
# coding:utf-8

"""
优先队列
Priority Queue

正常入，按照优先级出
"""

# ================================================================================
"""
heapq
    This module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm.

        Heaps are binary trees for which every parent node has a value less than or equal to any of its children. 
        This implementation uses arrays for which:    heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2]
        for all k, counting elements from zero. 
        For the sake of comparison, non-existing elements are considered to be infinite. 
        The interesting property of a heap is that its smallest element is always the root, heap[0].
        
        The API below differs from textbook heap algorithms in two aspects: 
            (a) We use zero-based indexing. 
                This makes the relationship between the index for a node and the indexes for its children slightly less obvious, 
                but is more suitable since Python uses zero-based indexing. 
            (b) Our pop method returns the smallest item, not the largest 
                (called a “min heap” in textbooks; a “max heap” is more common in texts because of its suitability for in-place sorting).
        
        These two make it possible to view the heap as a regular Python list without surprises: 
            heap[0] is the smallest item, 
            heap.sort() maintains the heap invariant!
            
        To create a heap, 
            use a list initialized to [], 
            or you can transform a populated list into a heap via function heapify().
"""
"""
由于 Python 只提供 heapq （小顶堆）
需要使用大顶堆时，通过将小顶堆的元素取反来实现！
"""
"""
时间复杂度:
    向堆中插入1个元素(堆内已有 n 个元素)，时间复杂度：
        O(logn)
    从堆中删除1个元素(堆内已有 n 个元素)，时间复杂度：
        O(logn)
    构建堆(有 n 个元素)，时间复杂度：
        自顶向下: O(n * logn)
        自下向上: O(n)
    堆排序(Heap Sort)，时间复杂度：
        O(n * logn)
"""
# ================================================================================
"""
LeetCode 703

数据流中的第K大元素

设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。

你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用 KthLargest.add，返回当前数据流中第K大的元素。

示例:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
说明: 
你可以假设 nums 的长度≥ k-1 且k ≥ 1。
"""


import heapq
from Queue import PriorityQueue


class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = nums
        self.size = len(nums)
        # ATTENTION: Not This
        # self.heap = heapq.heapify(nums)
        # ATTENTION: This
        # 本质上是 list 排序
        heapq.heapify(self.heap)
        while self.size > k:
            heapq.heappop(self.heap)
            self.size -= 1

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.size < self.k:
            heapq.heappush(self.heap, val)
            self.size += 1
        else:
            # self.size == k
            # [1]
            # if val > self.heap[0]:
            #     heapq.heapreplace(self.heap, val)
            # [2]
            heapq.heappushpop(self.heap, val)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# ================================================================================
"""
LeetCode 239

滑动窗口最大值

给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口 k 内的数字。滑动窗口每次只向右移动一位。

返回滑动窗口最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
注意：

你可以假设 k 总是有效的，1 ≤ k ≤ 输入数组的大小，且输入数组不为空。

进阶：

你能在线性时间复杂度内解决此题吗？
"""

# 基础方法(OK)
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        from collections import deque
        dq = deque(nums[:k])
        nums = nums[k:]
        ret = [max(dq)]
        for n in range(len(nums)):
            dq.popleft()
            dq.append(nums[n])
            ret.append(max(dq))
            pass
        return ret


# 优化方法(尚未理解)
# class Solution(object):
#     def maxSlidingWindow(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#         if not nums:
#             return []
#         # 存储双向队列的索引比存储元素更方便，因为两者都能在数组解析中使用。
#         window = []
#         ret = []
#         for i, x in enumerate(nums):
#             # print '=============================='
#             # print window
#             # print ret
#             # print '=============================='
#             # 窗口移动时，删除略过的元素索引
#             if i >= k and window[0] <= i - k:
#                 window.pop(0)
#                 pass
#             while window and nums[window[-1]] <= x:
#                 window.pop()
#                 pass
#             window.append(i)
#             if i >= k - 1:
#                 ret.append(nums[window[0]])
#             pass
#         return ret


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 处理特殊情况
        if not nums or not k:
            return []
        if k == 1:
            return nums

        # 队列清理方法
        def clean_deque(queue, i):
            # [1] 删除窗口移走的元素索引
            if queue and queue[0] == i - k:
                queue.popleft()
                pass
            # [2] 删除所有小于当前元素的元素索引
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
                pass
            pass

        # 双端队列用于存储数组的索引（比直接存储元素值更方便）
        # 双端队列初始化 & ret 数组初始化
        import collections
        deq = collections.deque()
        max_index = 0
        for i in range(k):
            clean_deque(deq, i)
            deq.append(i)
            #
            if nums[i] > nums[max_index]:
                max_index = i
                pass
            pass
        ret = [nums[max_index]]

        # 滑动窗口，计算输出数组
        # ( deq 这个双端队列，首元素一定是当前窗口中最大值的索引 )
        for i in range(k, len(nums)):
            clean_deque(deq, i)
            deq.append(i)
            ret.append(nums[deq[0]])
            # print '=============================='
            # print deq
            # print [nums[j] for j in deq]
            # print ret
            # print '=============================='
            pass

        return ret



# ================================================================================
# ================================================================================

so = Solution()
print so.maxSlidingWindow([1, 3, 2, 5, 4], 3)
# [3, 5, 5]

print so.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
# [3, 3, 5, 5, 6, 7]
