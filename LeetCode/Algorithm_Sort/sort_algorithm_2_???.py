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
桶排序
    时间: 
    空间: 
"""

@timeit
def bucket(nums):
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
# ================================================================================


import random
array = [random.randint(0, 1000) for _ in range(1000)]
print array


def test_sort(func):
    func(array)
    print array


if __name__ == '__main__':
    test_sort(bucket)
    pass