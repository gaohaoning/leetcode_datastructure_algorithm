"""
栈 & 队列
Stack & Queue
"""

# ================================================================================
"""
LeetCode 20

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""

# 时间复杂度 O(n)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        hash = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        for c in s:
            if c not in hash:
                stack.append(c)
            elif len(stack) == 0 or stack.pop() != hash[c]:
                return False
            pass
        # return False if stack else True
        return not stack
# ================================================================================
# 时间复杂度 O(n^2)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while len(s):
            before = len(s)
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
            after = len(s)
            if before == after:
                break
                pass
            pass
        return len(s) == 0
# ================================================================================
