# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverFromPreorder(self, traversal):
        """
        :type traversal: str
        :rtype: TreeNode
        """
        def build(d, idx):
            num = ""
            while(idx < len(traversal) and traversal[idx] != "-"):
                num += traversal[idx]
                idx += 1
            node = TreeNode(int(num))
            next_d = 0
            while(idx < len(traversal) and traversal[idx] == "-"):
                idx += 1
                next_d += 1
            if next_d == d + 1:
                node.left, idx = build(d + 1, idx)
            else:
                return node, idx - next_d
            next_d = 0
            while(idx < len(traversal) and traversal[idx] == "-"):
                idx += 1
                next_d += 1
            # print(node.val, "right", next_d)
            if next_d == d + 1:
                node.right, idx = build(d + 1, idx)
                return node, idx
            return node, idx - next_d
        return build(0, 0)[0]