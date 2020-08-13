#!/usr/bin/env python
# coding:utf-8

"""
862. 和至少为 K 的最短子数组
难度
困难

返回 A 的最短的非空连续子数组的长度，该子数组的和至少为 K 。

如果没有和至少为 K 的非空子数组，返回 -1 。



示例 1：

输入：A = [1], K = 1
输出：1
示例 2：

输入：A = [1,2], K = 4
输出：-1
示例 3：

输入：A = [2,-1,2], K = 3
输出：3


提示：

1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9
"""


# ================================================================================
"""
参考: 官方解答
Time Complexity: O(N), where N is the length of A.
Space Complexity: O(N) 
"""
"""
Intuition
    We can rephrase this as a problem about the prefix sums of A. Let P[i] = A[0] + A[1] + ... + A[i-1]. 
    We want the smallest y-x such that y > x and P[y] - P[x] >= K.
    Motivated by that equation, let opt(y) be the largest x such that P[x] <= P[y] - K. We need two key observations:
    
    [1] If x1 < x2 and P[x2] <= P[x1], then opt(y) can never be x1, 
        as if P[x1] <= P[y] - K, then P[x2] <= P[x1] <= P[y] - K but y - x2 is smaller. 
        This implies that our candidates x for opt(y) will have increasing values of P[x].
    [2] If opt(y1) = x, then we do not need to consider this x again. 
        For if we find some y2 > y1 with opt(y2) = x, 
        then it represents an answer of y2 - x which is worse (larger) than y1 - x.


Algorithm
    Maintain a "monoqueue" of indices of P: 
    a deque of indices x_0, x_1, ... such that P[x_0], P[x_1], ... is increasing.
    
    When adding a new index y, we'll pop x_i from the end of the deque so that P[x_0], P[x_1], ..., P[y] will be increasing.
    
    If P[y] >= P[x_0] + K, then (as previously described), we don't need to consider this x_0 again, 
    and we can pop it from the front of the deque.
"""
from collections import deque
class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        N = len(A)
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        #Want smallest y-x with Py - Px >= K
        ans = N+1 # N+1 is impossible
        monoq = deque() #opt(y) candidates, represented as indices of P
        for y, Py in enumerate(P):
            #Want opt(y) = largest x with Px <= Py - K
            while monoq and Py <= P[monoq[-1]]:
                monoq.pop()

            while monoq and Py - P[monoq[0]] >= K:
                ans = min(ans, y - monoq.popleft())

            monoq.append(y)

        return ans if ans < N+1 else -1
# ================================================================================
"""
要求:
时间复杂度 O(n)
空间复杂度 O(n)
"""
"""
知识点

单调队列
    单调队列一般是具有单调性的队列。
    单调队列有单调递增和单调递减两种，一般来讲，队列的队首是整个队列的最大值或最小值。
    单调队列可以解决许多问题，而且可以用来优化动态规划(DP)。

单调队列的实现步骤：
    若队列为空，将A[i]从队尾入队
    若队列不为空，将比A[i]大的元素都从队尾弹出，然后把A[i]入队
    若队列不为空，且A[i]大于队尾，则直接从队尾把A[i]入队

单调队列有许多作用：
    可以求出一个数组内第一个大于等于一个数 x 的数
    也可以通过维护单调性，解决一些区间内最小或最大的问题
"""
"""
思路:
[1] 问题转化:
求出前 n 项和的列表 sums, 则问题转化为:
a<b, sums(b)-sums(a)>=K, 求 min(b-a)
[2] 问题求解:
(用双端队列 deque)维护一个单调队列（monotone queue）
枚举 sums，每次将 i 入队 queue, 需要保持 i 对应的 sums[i] 组成单调队列:
    a.如果 sum[i] <= sums[queue[-1]], queue 队尾元素弹出;
    b.如果满足了 sum[i] - sum[queue[0]] >= K, 记录距离 i - queue[0], 同时弹出 queue[0]
"""


# from collections import deque
# class Solution(object):
#     def shortestSubarray(self, A, K):
#         """
#         :type A: List[int]
#         :type K: int
#         :rtype: int
#         """
#         if not A or K <= 0:
#             return -1
#         #
#         length = len(A)
#         sums = [0]
#         for x in A:
#             sums.append(sums[-1] + x)
#             pass
#         ret = length + 1
#         queue = deque()
#         for i, sum in enumerate(sums):
#             while queue and sum <= sums[queue[-1]]:
#                 queue.pop()
#             while queue and sum - sums[queue[0]] >= K:
#                 x = queue.popleft()
#                 ret = min(ret, i - x)
#             queue.append(i)
#             pass
#         return ret if ret < length + 1 else -1


"""
思路:
    滑动窗口(单调队列)
时间复杂度:
    O(n)
空间复杂度: 
    O(n)
"""


class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if not A or K <= 0:
            return -1
        # 前 n 项和的列表 sums (需要搞成长度是 n+1 的列表)
        sums = [0]
        for x in A:
            sums.append(sums[-1] + x)
            pass
        #
        from collections import deque
        queue = deque()
        length = len(A)
        ret = length + 1
        # 维护单调队列（monotone queue）
        for i, s in enumerate(sums):
            while queue and s < sums[queue[-1]]:
                queue.pop()
                pass
            while queue and s - sums[queue[0]] >= K:
                x = queue.popleft()
                ret = min(ret, i - x)  # !!!!!!!!!!
                pass
            queue.append(i)
            pass
        return ret if ret <= length else -1

# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================


so = Solution()
print so.shortestSubarray(
    [1,2,-4,3,5,7],
    6
)
# 1
