#!/usr/bin/env python
# coding:utf-8

"""
739. 每日温度
难度
中等

根据每日 气温 列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
"""
# ================================================================================
# """
# 笨方法（不推荐）
# """
# class Solution(object):
#     def dailyTemperatures(self, T):
#         """
#         :type T: List[int]
#         :rtype: List[int]
#         """
#         ret = []
#         for n in range(len(T)):
#             count = 0
#             is_found = False
#             for x in T[n+1:]:
#                 count += 1
#                 if x > T[n]:
#                     is_found = True
#                     ret.append(count)
#                     break
#                 pass
#             if not is_found:
#                 ret.append(0)
#             pass
#         return ret
# ================================================================================
"""
思路:
    单调栈
    
具体方法:
    维护单调栈(存储数组下标)，后入栈的元素总比栈顶元素小。
        比对当前元素与栈顶元素的大小
            若当前元素 < 栈顶元素：入栈
            若当前元素 > 栈顶元素：弹出栈顶元素，记录两者下标差值即为所求天数

时间复杂度:
    O(n)
空间复杂度: 
    O(n)
"""


class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        # 结果数组(初始元素全为0)
        ret = [0 for _ in range(len(T))]
        # stack 用于存储数组下标
        stack = []
        for i, x in enumerate(T):
            if stack:
                # 如果待加的值比栈顶元素大，则栈内所有比待加元素小的下标，都可以计算其在结果数组中的值。
                while stack and x > T[stack[-1]]:
                    ret[stack[-1]] = i - stack[-1]
                    stack.pop()
                    pass
                # 如果待加的值比栈顶元素小，则一直向栈中积累。
                stack.append(i)
                pass
            # 如果待加的值比栈顶元素小(或栈为空)，则一直向栈中积累。
            else:
                stack.append(i)
                pass
            pass
        return ret
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================


so = Solution()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print so.dailyTemperatures(temperatures)
# [1, 1, 4, 2, 1, 1, 0, 0]