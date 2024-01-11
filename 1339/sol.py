# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.subtree_sum = []
        def sum_of_tree(node):
            if node is None:
                return 0
            s = node.val
            s += sum_of_tree(node.left)
            s += sum_of_tree(node.right)
            self.subtree_sum.append(s)
            return s
        total_sum = sum_of_tree(root)
        ans = 0
        for ele in self.subtree_sum:
            ans = max(ans, ele * (total_sum - ele))
        return ans % 1000000007
