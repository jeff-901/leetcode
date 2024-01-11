# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        queue = [root]
        start_null = False
        while(queue):
            next_queue = []
            while(queue):
                cur = queue.pop(0)
                if start_null:
                    if cur:
                        return False
                else:
                    if cur is None:
                        start_null = True
                    else:
                        next_queue.append(cur.left)
                        next_queue.append(cur.right)
            queue = next_queue
        return True
