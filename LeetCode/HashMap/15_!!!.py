#!/usr/bin/env python
# coding:utf-8

"""
15. 三数之和

给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


# ================================================================================
# (NOK)(执行时间过长，超出时间限制)
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         注意: 此处这个方法需要返回所有可能的组合
#         """
#         ret = []
#         used = {}
#         for i, x in enumerate(nums):
#             if target - x not in used:
#                 used[x] = i
#             else:
#                 ret.append([target - x, x])
#             pass
#         return ret
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         if len(nums) < 3:
#             return []
#         import copy
#         ret = []
#         nums.sort()
#         for i, x in enumerate(nums):
#             remained = copy.copy(nums)
#             remained.pop(i)
#             two_sum = self.twoSum(remained, 0 - x)
#             if two_sum:
#                 # 注意: 返回的三元组需要去重
#                 for l in two_sum:
#                     three = sorted([x, l[0], l[1]])
#                     if three not in ret:
#                         ret.append(three)
#             pass
#         return list(ret)
# ================================================================================

# ================================================================================
"""
思路1:
    (NOK, 超出时间限制)
    遍历数组，针对每个值，利用 LeetCode1 (两数之和) 的方法搜索可能的组合。
时间复杂度:
    O(n**2)
空间复杂度:
    O(n**2)
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = []
        used = set()
        # used = list()
        for x in nums:
            if target - x not in used:
                used.add(x)
                # used.append(x)
            else:
                used.remove(target - x)
                ret.append([target - x, x])
            pass
        return ret

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        for n in nums:
            import copy
            nums_others = copy.copy(nums)  # 注意: 此处要用 copy.copy，否则 list 对象被地址传递后，对新 list 的修改会影响原 list
            nums_others.remove(n)
            answers = self.twoSum(nums_others, 0 - n)
            # print n, answers
            if answers:
                for ans in answers:
                    ans.insert(0, n)
                    ans.sort()
                    if ans not in ret:
                        ret.append(ans)
            pass
        return ret

# ================================================================================
"""
参考网上的方法（此法不会超出时间限制）
需要记住并理解透彻！！！
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 3:
            return []
        #
        ret = []
        nums.sort()
        for i in range(length - 2):
            # ========== 这里是提交 LeetCode 不超时的关键
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                pass
            # ========== 这里是提交 LeetCode 不超时的关键
            # 注意: 对于已经排序的列表 nums，遍历时，针对每一个值 x，只需要在它后面寻找和是 target-x 的组合即可
            left, right = i + 1, length - 1
            while left < right:
                s = nums[left] + nums[right]
                if s < 0 - nums[i]:
                    left += 1
                elif s > 0 - nums[i]:
                    right -= 1
                else:
                    ret.append([nums[i], nums[left], nums[right]])
                    # ========== 这里是提交 LeetCode 不超时的关键
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        pass
                        # ========== 这里是提交 LeetCode 不超时的关键
                    pass
                pass
            pass
        return ret

# ================================================================================

"""
思路2（优化前）:
    排序，循环遍历，双指针夹逼
时间复杂度:
    O(nlogn + n*n) =
    O(n**2)
空间复杂度: 
    O(n + n*1) =
    O(n)
"""
"""
以下写法容易理解，也正确，但是提交 LeetCode 超时，需要进一步优化 !!!!!
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 3:
            return []
        #
        ret = []
        nums.sort()
        # 注意: 对于已经排序的列表 nums，遍历时，针对每一个值 x，只需要在它后面寻找和是 target-x 的组合即可
        for i, n in enumerate(nums):
            left, right = i + 1, length - 1
            while left < right:
                # print left, right
                s = nums[left] + nums[right]
                if s < 0 - n:
                    left += 1
                elif s > 0 - n:
                    right -= 1
                else:
                    # print n, left, right
                    if [n, nums[left], nums[right]] not in ret:
                        ret.append([n, nums[left], nums[right]])
                        pass
                    # 找到一个组合之后，不能直接退出，因为对于当前的 n 值，还可能存在其他的合法组合
                    # 必须移动 left，使得 left 指向一个跟当前 left 不同的值
                    # 例子: [-3, -2, 2, 3] 中和为 0 的组合，不止一对
                    left += 1
                pass
            pass
        return ret
# ================================================================================
"""
思路2（优化后）:
    排序，循环遍历，双指针夹逼
时间复杂度:
    O(nlogn + n*n) =
    O(n**2)
空间复杂度: 
    O(n + n*1) =
    O(n)
"""
"""
以下写法是，进一步优化之后的结果，可以提交 LeetCode 通过 !!!!!
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 3:
            return []
        nums.sort()
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
                if s < 0:
                    left += 1
                elif s > 0:
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

# ================================================================================
# ================================================================================


# nums = [2, 7, 3, 6, 11, 15]
# so = Solution()
# print so.twoSum(nums, 9)

# l = [-1,0,1,2,-1,-4]
# l = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
# l = [-1,0,1,2,-1,-4]
# l = [3,0,3,2,-4,0,-3,2,2,0,-1,-5]
# l = [-3, -2, -1, 0, 0, 0, 2, 2, 2, 3, 3]
l = [-4, -1, -1, 0, 1, 2]
so = Solution()
print so.threeSum(l)
# [[-3, 0, 3], [-5, 2, 3], [0, 0, 0], [-4, 2, 2]]
# [[-5, 2, 3], [-4, 2, 2], [-3, 0, 3], [0, 0, 0]]
