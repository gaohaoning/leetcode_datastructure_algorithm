#!/usr/bin/env python
# coding:utf-8

"""
621. 任务调度器
难度
中等

给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。

然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的最短时间。

示例 1：

输入: tasks = ["A","A","A","B","B","B"], n = 2
输出: 8
执行顺序: A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
注：

任务的总个数为 [1, 10000]。
n 的取值范围为 [0, 100]。
"""


# ================================================================================
"""
（此解法错误，需要学习）
"""
# from collections import deque, Counter
# class Solution(object):
#     def reorder(self, tasks):
#         counter = Counter(tasks)
#         tasks_new = []
#         while tasks:
#             # for t in filter(lambda key: counter[key], counter.keys()):
#             for t in sorted(
#                 filter(lambda key: counter[key], counter.keys()),
#                 key=lambda x: counter[x],
#                 reverse=True
#             ):
#                 tasks.remove(t)
#                 tasks_new.append(t)
#                 counter[t] -= 1
#             pass
#         return tasks_new
#
#     def findTaskInList(self, deq, tasks):
#         for t in tasks:
#             if t not in deq:
#                 return t
#         return None
#
#     def leastInterval(self, tasks, n):
#         """
#         :type tasks: List[str]
#         :type n: int
#         :rtype: int
#         """
#         """
#         注意:
#         初始时应该让 tasks 中的任务尽可能分散排列, 而且要按出现频次从大到小
#         例:
#         A A B B C
#         应该排列成
#         A B C A B
#         而不是
#         A C B A B
#         而不是
#         A C A B B
#         """
#         # task  # 用来实际操作
#         counter = Counter(tasks)  # 用来计数
#         queue = deque()  # 队列长度不超过n
#         duration = 0
#         tasks = self.reorder(tasks)
#         print tasks
#         while tasks:
#             task = self.findTaskInList(queue, tasks)
#             if task:
#                 tasks.remove(task)
#                 counter[task] -= 1
#                 pass
#             queue.append(task)
#             len(queue) > n and queue.popleft()
#             duration += 1
#             pass
#         return duration


# ================================================================================
"""
思路:
    [1]优先安排需要执行次数最多的任务, 其余任务插空
        需要最少的任务时间 total =（最多任务数-1）*（n + 1） + （相同最多任务的任务个数）
    [2]注意任务种类数 > n 的情况，按照上面的方式计算，会有一些任务没有被安排完，这种情况下:
        假设频率小的字母数量很多, 即 len(counter.keys()) > n 
            频率大于1时, 将频率小的字母穿插进来
            频率等于1时, 直接加到末尾即可
        结果取: max(len(tasks), total)
"""
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n == 0:
            return len(tasks)
        #
        from collections import Counter
        counter = Counter(tasks)
        most = max(counter.values())
        # print most
        num_most = 0
        for k, v in counter.iteritems():
            if v == most:
                num_most += 1
                pass
            pass
        total = (most - 1) * (n + 1) + num_most
        return max(total, len(tasks))


# ================================================================================
"""
更优化的写法
"""

"""
思路:
    (统一安排)
    (具体看代码)
时间复杂度:
    O(n)
空间复杂度: 
    O(1)
"""


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n == 0:
            return len(tasks)
        # 任务代码范围 A~Z 使用 ord 值表示
        schedule = [0] * 26
        for t in tasks:
            schedule[ord(t) - ord('A')] += 1
            pass
        # 频率最高的任务，频率
        most_count = max(schedule)
        # 频率最高的任务，个数
        most_count_same = 0
        for c in schedule:
            if c == most_count:
                most_count_same += 1
                pass
            pass
        return max(
            len(tasks),
            (n + 1) * (most_count - 1) + most_count_same
        )

# ================================================================================

so = Solution()

# print so.leastInterval(["A","B","C","A","B"], 2)

# print so.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2)

# print so.leastInterval(["A","A","A","B","B","B"], 0)

# print so.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2)

# print so.leastInterval(list('AAAABBBBCCCCDD'), 2)

print so.leastInterval(list('AAAABBBCCDDFFG'), 2)


# ================================================================================

