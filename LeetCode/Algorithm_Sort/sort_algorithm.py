#!/usr/bin/env python
# coding:utf-8

"""
排序算法
"""

def timeit(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        stop = time.time()
        delta = stop - start
        print 'duration = %s' % delta
        return ret
    return wrapper
# ================================================================================
"""
冒泡
    时间: n**2
    空间: 1
"""

@timeit
def bubble(nums):
    length = len(nums)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                pass
            pass
        pass
    return nums
# ================================================================================
"""
选择
    时间: n**2
    空间: 1
"""

@timeit
def select(nums):
    length = len(nums)
    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if nums[j] < nums[min_index]:
                min_index = j
                pass
            pass
        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]
        pass
    return nums
# ================================================================================
"""
插入
    时间: n**2
    空间: 1
"""

@timeit
def insert(nums):
    length = len(nums)
    for i in range(length):
        current = nums.pop(i)
        # j 的范围: 0 ~ i, 如此才能判断是否已经移至有序子数组的尾部
        for j in range(i + 1):
            if j == i or current < nums[j]:
                nums.insert(j, current)
                break
            pass
        pass
    return nums
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================


import random
array = [random.randint(0, 1000) for _ in range(1000)]
print array


def test_sort(func):
    func(array)
    print array


if __name__ == '__main__':
    test_sort(bubble)
    test_sort(select)
    test_sort(insert)
    pass
