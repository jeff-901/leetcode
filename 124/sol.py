# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = root.val
        def dfs(node):
            if node is None:
                return 0
            left_val = max(dfs(node.left), 0)
            right_val = max(dfs(node.right), 0)
            self.ans = max(self.ans, right_val + left_val + node.val)
            return max(left_val, right_val) + node.val
        dfs(root)
        return self.ans