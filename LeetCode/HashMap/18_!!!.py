#!/usr/bin/env python
# coding:utf-8

"""
18. 四数之和
难度
中等

给定一个包含 n 个整数的数组 nums 和一个目标值 target，
判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？
找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
# ================================================================================
"""
思路:
    排序，循环遍历，调用 LeetCode15(三数之和) 的方法
时间复杂度:
    nlogn + n * O(n**2) =
    O(n**3)
空间复杂度: 
    O(n + n * n) =
    O(n**2)
"""


class Solution(object):
    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        """
        时间复杂度:
            O(n*n) =
            O(n**2)
        空间复杂度: 
            O(1)
        """
        length = len(nums)
        if length < 3:
            return []
        # nums.sort()  # ######################### 外层已经排序过，此处不必重新排序
        ret = []
        # 注意: 对于已经排序的列表 nums，遍历时，针对每一个值 x，只需要在它后面寻找和是 target-x 的组合即可
        for i, n in enumerate(nums):
            # ------------------------------ 这里是提交 LeetCode 不超时的关键
            # 重复的值，不需要重复寻找另外两个数
            if i > 0 and n == nums[i - 1]:
                continue
                pass
            # ------------------------------ 这里是提交 LeetCode 不超时的关键
            left, right = i + 1, length - 1
            while left < right:
                s = n + nums[left] + nums[right]
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    ret.append([n, nums[left], nums[right]])
                    # 找到符合条件的两个数后，也要移动指针，继续寻找其他符合条件的数对
                    left += 1
                    # ------------------------------ 这里是提交 LeetCode 不超时的关键
                    # 找到一个组合之后，不能直接退出，因为对于当前的 n 值，还可能存在其他的合法组合
                    # 必须移动 left，使得 left 指向一个跟当前 left 不同的值
                    # 例子: [-3, -2, 2, 3] 中和为 0 的组合，不止一对
                    #
                    # 右移 left 使得下一个 left 与当前值不同
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                        pass
                    # ------------------------------ 这里是提交 LeetCode 不超时的关键
                pass
            pass
        return ret

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        """
        需要注意:
            list.remove() 结果是 None, 执行的结果是改变了原 list
            list.extend() 结果是 None, 执行的结果是改变了原 list
        """
        length = len(nums)
        if length < 4:
            return []
        #
        ret = []
        nums.sort()
        for i, n in enumerate(nums):
            # ------------------------------ 对于相等的 n 值，不必重复计算
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                pass
            # ------------------------------ 对于相等的 n 值，不必重复计算
            # ------------------------------ 注意: 确定一个值，找剩余3个数时，直接寻找这个值后面的子数组即可，不再需要包含前面的元素
            # import copy
            # ns = copy.copy(nums)
            # ns.remove(n)
            # list_3 = self.threeSum(ns, target - n)
            # ------------------------------ 注意: 确定一个值，找剩余3个数时，直接寻找这个值后面的子数组即可，不再需要包含前面的元素
            list_3 = self.threeSum(nums[i + 1:], target - n)
            # ------------------------------ 注意: 确定一个值，找剩余3个数时，直接寻找这个值后面的子数组即可，不再需要包含前面的元素
            if list_3:
                for l3 in list_3:
                    ret.append([n] + l3)
                    pass
                pass
            pass

        # 检查是否有重复的 4 元组
        # for l in sorted([sorted(l) for l in ret]):
        #     print l
        #     pass
        # 检查是否有重复的 4 元组
        return ret

# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================


so = Solution()
# nums = [1,0,-1,0,-2,2]
nums = [-2, -1, 0, 0, 1, 2]
target = 0
print so.fourSum(nums, target)
