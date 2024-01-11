# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        stack = []
        for num in nums:
            if len(stack) > 0 and num > stack[-1].val:
                cur = stack.pop()
                while(len(stack) > 0 and num > stack[-1].val):
                    stack[-1].right = cur
                    cur = stack.pop()
                stack.append(TreeNode(val = num, left=cur))
            else:
                stack.append(TreeNode(val = num))
        cur = stack.pop()
        while(len(stack) > 0):
            stack[-1].right = cur
            cur = stack.pop()
        return cur