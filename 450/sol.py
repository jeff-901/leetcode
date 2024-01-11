# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        p = TreeNode(0, root, None)
        head = p
        node = root
        while(node and node.val != key):
            p = node
            if key < node.val:
                node = node.left
            else:
                node = node.right
        if node is None:
            return head.left
        if node.left is None:
            if p.left == node:
                p.left = node.right
            else:
                p.right = node.right
        elif node.right is None:
            if p.left == node:
                p.left = node.left
            else:
                p.right = node.left
        else:
            cur = node.right
            cur_p = node
            while(cur.left):
                cur_p = cur
                cur = cur.left
            if cur_p == node:
                cur_p.right = cur.right
            else:
                cur_p.left = cur.right
            cur.left = node.left
            cur.right = node.right
            if p.left == node:
                p.left = cur
            else:
                p.right = cur
        return head.left