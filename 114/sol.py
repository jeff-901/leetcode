# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        stack = [None]
        cur = root
        while(cur):
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                cur.right = cur.left
                tmp = cur.left
                cur.left = None
                cur = tmp
            else:
                cur.right = stack[-1]
                cur = stack.pop()
        return root