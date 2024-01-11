# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        
        def find_h(node):
            if node is None:
                return -1
            return max(find_h(node.left), find_h(node.right)) + 1
        h = find_h(root)
        n = 2**(h+1) - 1
        self.ans = [["" for _ in range(n)] for _ in range(h+1)]
        self.ans[0][(n-1)/2] = str(root.val)
        def dfs(node, r, c):
            if node.left:
                c_l = c-2**(h-r-1)
                self.ans[r+1][c_l] = str(node.left.val)
                dfs(node.left, r+1, c_l)
            if node.right:
                c_r = c+2**(h-r-1)
                self.ans[r+1][c_r] = str(node.right.val)
                dfs(node.right, r+1, c_r)
        dfs(root, 0, (n-1)/2)
        return self.ans