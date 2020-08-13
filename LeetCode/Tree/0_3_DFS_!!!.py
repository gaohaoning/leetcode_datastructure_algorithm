#!/usr/bin/env python
# coding:utf-8

"""
(Demo)
DFS 遍历算法，搜索指定的值
"""

# ================================================================================
"""
二叉树节点定义
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        pass

    def neighbors(self):
        if not self.left and not self.right:
            return []
        elif not self.left and self.right:
            return [self.right]
        elif self.left and not self.right:
            return [self.left]
        elif self.left and self.right:
            return [self.left, self.right]
    pass

# ================================================================================
"""
DFS
    (使用系统栈，隐式栈)
"""


visited = set()
def dfs(root, target):
    visited.add(root)
    print 'visited', root.val
    if root.val == target:
        return True
    for node in root.neighbors():
        if node not in visited:
            ret = dfs(node, target)
            if ret:
                return ret
        pass
    pass


# ================================================================================
"""
DFS
    (自己实现，显式栈)
"""
"""
思路:
    1. 栈初始化；
    2. 
        输出起始顶点 root；
        起始顶点 root 标记为已访问；
        起始顶点 root 入栈；
    3.重复以下操作直至栈空:
        3.1 取栈顶元素（不出栈）
        3.2 判断栈顶元素是否存在未被访问的邻节点 node ？
                Yes: 
                    输出 node；
                    node 标记为已访问；
                    node 入栈。
                    break (不处理其他邻节点 node_next)
                No:  栈顶元素出栈
"""


def dfs(root, target):
    """
    逻辑与递归解决方案完全相同,
    只是使用 [while循环] 和 [栈] 来模拟递归期间的系统调用栈
    """
    # 记录已访问节点
    visited = set()
    # (显式)栈
    stack = list()
    # 起始顶点标记为已访问
    visited.add(root)
    print 'visited', root.val
    # 起始顶点入栈
    stack.append(root)
    print 'stack: ', [n.val for n in stack]
    # 重复处理直至栈为空
    while stack:
        # 取栈顶元素（不出栈）
        cur = stack[-1]
        if cur.val == target:
            return True
        #
        if not cur.neighbors() or all(
                map(
                    lambda x: x in visited,
                    cur.neighbors()
                )
        ):
            """
            # 栈顶元素不存在未被访问的邻节点
            """
            stack.pop()
            print 'stack: ', [n.val for n in stack]
        else:
            """
            # 栈顶元素存在未被访问的邻节点
            """
            for node in cur.neighbors():
                if node not in visited:
                    # 标记已访问
                    visited.add(node)
                    print 'visited', node.val
                    # 节点入栈
                    stack.append(node)
                    print 'stack: ', [n.val for n in stack]
                    break  # DFS 的关键所在 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    pass
                pass
            pass
    return False


# ================================================================================


a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(4)
a5 = TreeNode(5)

a1.left = a2
a1.right = a3
a2.left = a4
a4.left = a5

visited = set()
print dfs(a1, 5)
# visited 1
# visited 2
# visited 4
# visited 5
# True

visited = set()
print dfs(a1, 3)
# visited 1
# visited 2
# visited 4
# visited 5
# visited 3
# True
