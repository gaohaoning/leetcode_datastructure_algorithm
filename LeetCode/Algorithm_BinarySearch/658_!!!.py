#!/usr/bin/env python
# coding:utf-8

"""
658. 找到 K 个最接近的元素
难度
中等

给定一个排序好的数组，两个整数 k 和 x，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。如果有两个数与 x 的差值一样，优先选择数值较小的那个数。

示例 1:

输入: [1,2,3,4,5], k=4, x=3
输出: [1,2,3,4]


示例 2:

输入: [1,2,3,4,5], k=4, x=-1
输出: [1,2,3,4]


说明:

k 的值为正数，且总是小于给定排序数组的长度。
数组不为空，且长度不超过 10^4
数组里的每个元素与 x 的绝对值不超过 10^4


更新(2017/9/19):
这个参数 arr 已经被改变为一个整数数组（而不是整数列表）。 请重新加载代码定义以获取最新更改。
"""


# ================================================================================
"""
思路:
    二分查找找到最接近的值；
    以最接近值为中心向两侧扩张（注意边界问题）。
"""
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # x 落在 arr 的取值范围之外，则只取边缘的 k 个值即可
        if x < arr[0]:
            return arr[:k]
        elif x > arr[-1]:
            return arr[-k:]
        # arr 的长度小于等于 k, 则直接返回 arr
        if len(arr) <= k:
            return arr
        #
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right)/2
            if arr[mid + 1] < x:
                # 注意: 此处应为 < 而不是 <=（此处易出错）
                left = mid + 1
            elif arr[mid] > x:
                # 注意: 此处应为 > 而不是 >= (此处易出错)
                right = mid
            else:
                print 'mid', mid
                # x 落在了 mid 和 mid+1 之间(包含边界)
                nearest = mid if x - arr[mid] <= arr[mid + 1] - x else mid + 1
                print 'nearest', nearest
                # 找到了最接近的点 nearest 之后，向两边搜索 k - 1 个值（需要注意边界）
                start, stop = nearest, nearest + 1
                for _ in range(k - 1):
                    # ------------------------------------------------------------
                    # 注意: 这里要考虑 start = 0 时, 不能继续向左移动(start - 1), 这样会移动到列表尾部
                    # if stop >= len(arr) or x - arr[start - 1] <= arr[stop] - x:
                    #     start -= 1
                    # elif start <= 0 or x - arr[start - 1] > arr[stop] - x:
                    #     stop += 1
                    # ------------------------------------------------------------
                    # 注意1:为了避免 start = 0 后继续向左移动，此处先判断向右移动的情况
                    # 然后用 else 概括向左移动的情况
                    # 注意2:判断条件时要充分考虑边界情况
                    if start <= 0 or (stop < len(arr) and x - arr[start - 1] > arr[stop] - x):
                        stop += 1
                    else:
                        start -= 1
                    # ------------------------------------------------------------
                    pass
                    print start, stop
                return arr[start: stop]


# ================================================================================
# ================================================================================
# ================================================================================

# so = Solution()
# print so.findClosestElements([1,2,3,4,5], 4, 3)
# [1, 2, 3, 4]

# so = Solution()
# print so.findClosestElements([0,1,2,2,2,3,6,8,8,9], 5, 9)
# [3, 6, 8, 8, 9]

# so = Solution()
# print so.findClosestElements([1,2,3,4,5], 4, -1)
# [1, 2, 3, 4]

# so = Solution()
# print so.findClosestElements([0,1,1,1,2,3,6,7,8,9], 9, 4)
# [0, 1, 1, 1, 2, 3, 6, 7, 8]


# so = Solution()
# print so.findClosestElements([0,1,2,2,2,3,6,8,8,9], 5, 9)
# [3, 6, 8, 8, 9]
