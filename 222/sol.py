# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def find(val):
            bin_str = bin(val)[3:]
            cur = root
            for i in range(len(bin_str)):
                if bin_str[i] == "0":
                    cur = cur.left
                else:
                    cur = cur.right
                if cur is None:
                    return False
            return True
        if root is None:
            return 0
        if root.left is None:
            return 1
        cur = root 
        left = 1
        while(cur):
            left = cur.val
            cur = cur.left
        right = 50000
        while left <= right:
            mid = (left + right) // 2
            if find(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right