# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        self.ans = []
        self.n = len(voyage)
        if root.val != voyage[0]:
            return [-1]
        self.idx = 0
        def dfs(node):
            if self.idx == self.n - 1:
                return True
            if not node.left and not node.right:
                return
            elif not node.left:
                if node.right.val == voyage[self.idx+1]:
                    self.idx += 1
                    dfs(node.right)
            elif not node.right:
                if node.left.val == voyage[self.idx+1]:
                    self.idx += 1
                    dfs(node.left)
            else:
                if node.left.val == voyage[self.idx+1]:
                    self.idx += 1
                    dfs(node.left)
                    if node.right.val == voyage[self.idx+1]:
                        self.idx += 1
                        dfs(node.right)
                elif node.right.val == voyage[self.idx+1]:
                    self.idx += 1
                    self.ans.append(node.val)
                    dfs(node.right)
                    if node.left.val == voyage[self.idx+1]:
                        self.idx += 1
                        dfs(node.left)

        dfs(root)
        if self.idx != self.n - 1:
            return [-1]
        return self.ans