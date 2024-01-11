# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 1
        def dfs(node):
            if node is None:
                return 0
            left_val = dfs(node.left)
            right_val = dfs(node.right)
            res = 1
            if left_val and node.left.val == node.val:
                res += left_val
            else:
                left_val = 0
            if right_val and node.right.val == node.val:
                res += right_val
            else:
                right_val = 0
            self.ans = max(self.ans, res)
            return 1 + max(left_val, right_val)
        dfs(root)
        return self.ans - 1