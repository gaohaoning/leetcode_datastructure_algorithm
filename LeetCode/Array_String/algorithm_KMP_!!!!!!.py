#!/usr/bin/env python
# coding:utf-8

"""
算法原理讲解参考:
    https://www.zhihu.com/question/21923021/answer/281346746
    https://blog.csdn.net/f1033774377/article/details/82556438
"""

"""
字符串匹配:
    目标串(主串): 长度为 m
    模式串(子串): 长度为 n

模式匹配/串匹配/子串定位运算:
    一般表示:
        S 表示目标串
        T 表示模式串
    将从 目标串S 中查找 模式串T 的过程称为模式匹配。
"""

"""
字母缩写:

KMP:
    Knuth-Morris-Pratt
    (发明者: D.E.Knuth，J.H.Morris，V.R.Pratt)
PMT:
    Partial Match Table
    (部分匹配表)
"""
# ================================================================================
"""
KMP 算法:
    KMP 算法是一种改进的字符串匹配算法，由D.E.Knuth，J.H.Morris，V.R.Pratt同时发现，因此人们称它为克努特——莫里斯——普拉特操作（简称KMP算法）。
    算法关键: 利用匹配失败后的信息，尽量减少模式串与主串的匹配次数以达到快速匹配的目的。
    具体实现: 实现一个next()函数，函数本身包含了模式串的局部匹配信息。
    时间复杂度: O(m+n)
    空间复杂度: O(n)
"""

"""
KMP 算法思想:
    在每一趟匹配过程中出现字符不等时，不需要回退主串的指针，
    而是利用已经得到前面“部分匹配”的结果，将模式串向右滑动若干个字符后，继续与主串中的当前字符进行比较。 
"""
"""
KMP 算法思想:
    KMP算法的核心是寻找模式串本身的规律。
    在该算法中表现为反映该规律的next数组。
    next数组的作用是在每次失配时，模式串根据next数组对应位置上的值回溯模式串索引的位置。
    next数组的求法也是KMP算法的精华所在。 
"""
# ================================================================================
"""
KMP 算法详解:

前缀：指的是字符串的子串中从原串最前面开始的子串，如 abcdef 的前缀有：a,ab,abc,abcd,abcde
后缀：指的是字符串的子串中在原串结尾处结尾的子串，如 abcdef 的后缀有：f,ef,def,cdef,bcdef

F数组（也被称为 next数组) (即部分匹配表 PMT):
    F(i) 表示的是：
        前i的字符组成的这个子串，前缀集合与后缀集合的交集中，最长元素的长度。
    例如:
        模式串：'aababaaba'
        前缀集合：{'a','aa','aab','aaba','aabab','aababa','aababaa','aababaab'}
        后缀集合：{'ababaaba','babaaba','abaaba','baaba','aaba','aba','ba','a'}
        交集：{'a', 'aaba'}
        最长元素是 'aaba'，长度是 4
    例如:
        模式串：'abababca'
        前缀集合：{'a','ab','aba','abab','ababa','ababab','abababc'}
        后缀集合：{'bababca','ababca','babca','abca','bca','ca','a'}
        交集：{'a'}
        最长元素是 'a'，长度是 1
"""

"""
F数组实例:
    char:  a b a b a b c a
    index: 0 1 2 3 4 5 6 7
    PMT:   0 0 1 2 3 4 0 1
    F(i): -1 0 0 1 2 3 4 0
"""

"""
一些约定:
    1.所有的字符串从 0 开始编号。
    2.F数组（即其他文章中的next数组），F[i]表示 0~i 的字符串的最长相同前缀后缀的长度。
"""
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
"""
以下是 KMP 算法的原理代码
"""

def get_prefix_postfix_common_length_max(s='abababca'):
    """
    求一个字符串，前缀集合和后缀集合的交集，最长字符串的长度
    """
    prefix = {s[:i + 1] for i in range(len(s) - 1)}
    postfix = {s[i + 1:] for i in range(len(s) - 1)}
    common = prefix & postfix
    length = max([len(x) for x in common]) if common else 0
    return length


def get_F(string='abababca'):
    """
    F数组/next数组 的求法:
    从模式字符串的第一位(注意，不包括第0位)开始对自身进行匹配运算。
    在任一位置，能匹配的最大长度就是当前位置的 F/next 值。
    """
    """
    F数组实例:
        char:  a b a b a b c a
        index: 0 1 2 3 4 5 6 7
        PMT:   0 0 1 2 3 4 0 1
        F(i): -1 0 0 1 2 3 4 0
    """
    pmt = []
    for i in range(len(string)):
        pmt.append(
            get_prefix_postfix_common_length_max(
                string[:i + 1]
            )
        )
        pass
    print pmt
    # [0, 0, 1, 2, 3, 4, 0, 1]
    f = [-1] + pmt[:len(string) - 1]
    # [-1, 0, 0, 1, 2, 3, 4, 0]
    return f


# def pattern_matching(s='ababababca', t='abababca'):
#     """
#     模式匹配: 暴力求解（笨方法）
#     """
#     ret = -1
#     for i in range(len(s) - len(t) + 1):
#         is_match = True
#         for j in range(len(t)):
#             if not s[i + j] == t[j]:
#                 is_match = False
#                 break
#             pass
#         if is_match:
#             return i
#         pass
#     return ret


def pattern_matching(s='ababababca', t='abababca'):
    """
    KMP 算法 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    """
    f_array = get_F(t)
    # print f_array
    # [-1, 0, 0, 1, 2, 3, 4, 0]
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        """
        j == -1 表示从模式串起点开始重新匹配
        s[i] == t[j] 表示运用 KMP 算法，省略了一些比较步骤后，下一个字符串匹配成功
        """
        if j == -1 or s[i] == t[j]:
            i += 1
            j += 1
        else:
            # 保持 i 指针不动，然后将 j 指针指向模式字符串的第 next[j] 位
            j = f_array[j]
        pass
    if j == len(t):
        return i - j
    else:
        return -1

# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
"""
以下是 KMP 算法的原理代码（简化版）!!!!!!!!!!!!!!!!!!!!!!!!!
"""


def get_F(t='abababca'):
    """
    求 F/next 数组
    """
    """
    求next数组的过程，完全可以看成字符串匹配的过程，即：
        以模式字符串为主字符串，
        以模式字符串的前缀为目标字符串，
        一旦字符串匹配成功，那么当前的next值就是匹配成功的字符串的长度。
    具体来说，
        就是从模式字符串的第一位(注意，不包括第0位)开始对自身进行匹配运算。
        在任一位置，能匹配的最长长度就是当前位置的next值。
    """
    # [-1, 0, 0, 1, 2, 3, 4, 0]
    # F数组，第0位永远是 -1
    f = [-1]
    # 目标串的指针: i
    # 模式串的指针: j
    i = 0
    j = -1
    while i < len(t):
        if j == -1 or t[i] == t[j]:
            i += 1
            j += 1
            f.append(j)
            # print i, j, f
        else:
            j = f[j]
            # print i, j, f
            pass
        pass
    """
    1 0 [-1, 0]
    1 -1 [-1, 0]
    2 0 [-1, 0, 0]
    3 1 [-1, 0, 0, 1]
    4 2 [-1, 0, 0, 1, 2]
    5 3 [-1, 0, 0, 1, 2, 3]
    6 4 [-1, 0, 0, 1, 2, 3, 4]
    6 2 [-1, 0, 0, 1, 2, 3, 4]
    6 0 [-1, 0, 0, 1, 2, 3, 4]
    6 -1 [-1, 0, 0, 1, 2, 3, 4]
    7 0 [-1, 0, 0, 1, 2, 3, 4, 0]
    8 1 [-1, 0, 0, 1, 2, 3, 4, 0, 1]
    """
    return f


def pattern_matching(s='ababababca', t='abababca'):
    """
    KMP 算法 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    """
    f_array = get_F(t)
    # print f_array
    # [-1, 0, 0, 1, 2, 3, 4, 0]
    # [-1, 0, 0, 1, 2, 3, 4, 0, 1]
    # 目标串的指针: i
    # 模式串的指针: j
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        """
        j == -1
            表示从模式串起点开始重新匹配
        s[i] == t[j]
            表示运用 KMP 算法，省略了一些比较步骤后，下一个字符串匹配成功
        """
        if j == -1 or s[i] == t[j]:
            i += 1
            j += 1
        else:
            # 保持 i 指针不动，然后将 j 指针指向模式字符串的第 next[j] 位
            j = f_array[j]
        pass
    if j == len(t):
        return i - j
    else:
        return -1
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================


if __name__ == '__main__':
    s = 'ababababca'
    t = 'abababca'
    print pattern_matching(s, t)
    # should be: 2