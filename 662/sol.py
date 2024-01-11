# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.children = []
        if root is None:
            return 0
        self.ans = 1
        def dfs(node, d, val):
            if node is None:
                return 
            if len(self.children) <= d:
                self.children.append(val)
            else:
                self.ans = max(self.ans, val - self.children[d] + 1)
            dfs(node.left, d+1, val*2)
            dfs(node.right, d+1, val*2 + 1)
        dfs(root, 0, 1)
        return self.ans