# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        self.h = {0: 1}
        self.ans = 0
        def dfs(node, val):
            if node is None:
                return
            val += node.val
            self.ans += self.h.get(val - targetSum, 0)
            self.h[val] = self.h.get(val, 0) + 1
            dfs(node.left, val)
            dfs(node.right, val)
            self.h[val] -= 1
        dfs(root, 0)
        return self.ans
