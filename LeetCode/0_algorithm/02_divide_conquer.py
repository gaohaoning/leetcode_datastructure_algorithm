#!/usr/bin/env python
# coding:utf-8

"""
分治
    divide & conquer
"""
"""
分治 和 动态规划 区别:
    分治，是将问题划分为 [互不相交的] 子问题，递归的求解子问题，再将它们的解组合起来，求出原问题的解。
    动态规划，是应用于 [子问题重叠] 的情况，即不同的子问题具有公共的子子问题。(例如 Fibonacci）
"""


# ================================================================================
"""
分治代码模板
"""


def divide_conquer(problem, *params):
    """
    分治代码模板
    """
    # ============================== 递归终止条件
    # recursion terminator
    """
    if problem is None:
        print_result
        return
    """

    # ============================== 准备数据
    # ============================== 分割问题
    # prepare data
    # problem split
    """
    data = prepare_data(problem)
    sub_problems = split_problems(problem, data)
    """

    # ============================== 解决子问题
    # conquer sub_problems
    """
    sub_result0 = divide_conquer(sub_problems[0], p1, ...)
    sub_result1 = divide_conquer(sub_problems[1], p1, ...)
    sub_result2 = divide_conquer(sub_problems[2], p1, ...)
    """

    # ============================== 合并结果
    # merge sub_results
    """
    result = process_result(sub_result0, sub_result1, sub_result2, ...)
    """

# ================================================================================
# ================================================================================
# ================================================================================

