# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = [None]
        ans = None
        while(root):
            stack.append(root)
            root = root.left
        ans = stack.pop()
        cur = ans
        while(stack):
            if cur.right:
                tmp = cur.right
                while(tmp):
                    stack.append(tmp)
                    tmp = tmp.left
            cur.left = None
            cur.right = stack[-1]
            cur = stack.pop()

        return ans
