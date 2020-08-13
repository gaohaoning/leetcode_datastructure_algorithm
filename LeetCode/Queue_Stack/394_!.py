#!/usr/bin/env python
# coding:utf-8

"""
394. 字符串解码
难度
中等

给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例:

s = "3[a]2[bc]", 返回 "aaabcbc".
s = "3[a2[c]]", 返回 "accaccacc".
s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".
"""
# ================================================================================
"""
思路:
    涉及括号匹配，使用: 栈
时间复杂度:
    O()
空间复杂度: 
    O()
"""

"""
ord('0') = 48
ord('9') = 57
ord('A') = 65
ord('Z') = 90
ord('a') = 97
ord('z') = 122
ord('[') = 91
ord(']') = 93
"""


# 只能处理一位数字的版本


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack_count = []
        stack_str = []
        ret = ''
        for x in s:
            if 48 <= ord(x) <= 57:
                stack_count.append(int(x))
            elif x == '[':
                stack_str.append('')
            elif 65 <= ord(x) <= 90 or 97 <= ord(x) <= 122:
                if stack_str:
                    # 需要入栈
                    stack_str[-1] += x
                else:
                    # 不需要入栈，直接累加在结果里
                    ret += x
            elif x == ']':
                count = stack_count.pop()
                string = stack_str.pop()
                res = count * string
                if not stack_count and not stack_str:
                    ret += res
                elif stack_str:
                    stack_str[-1] += res
                    pass
                pass
            pass
        return ret


# 能够处理多位数字的版本


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack_count = []
        stack_str = []
        ret = ''
        is_pre_num = False  # 表示前一位是否为数字，用以处理多位数字的情况
        for x in s:
            if 48 <= ord(x) <= 57:
                if is_pre_num:
                    stack_count[-1] = 10 * stack_count[-1] + int(x)
                    pass
                else:
                    stack_count.append(int(x))
                    pass
                is_pre_num = True
            else:
                is_pre_num = False
                if x == '[':
                    stack_str.append('')
                elif 65 <= ord(x) <= 90 or 97 <= ord(x) <= 122:
                    if stack_str:
                        # 需要入栈
                        stack_str[-1] += x
                    else:
                        # 不需要入栈，直接累加在结果里
                        ret += x
                elif x == ']':
                    count = stack_count.pop()
                    string = stack_str.pop()
                    res = count * string
                    if not stack_count and not stack_str:
                        ret += res
                    elif stack_str:
                        stack_str[-1] += res
                        pass
                    pass
                pass
            pass
        return ret


# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================
# ================================================================================


so = Solution()

# print so.decodeString("3[a2[c]]")

# print so.decodeString("3[a]2[bc]")

# print so.decodeString("2[abc]3[cd]ef")
# abcabccdcdcdef
# abcabccdcdcdef

# print so.decodeString("10[leetcode]")

print so.decodeString("3[a]2[b4[F]c]")
# aaabFFFFcbFFFFc
