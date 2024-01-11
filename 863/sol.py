# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        self.parents = []
        self.t = None
        def search(node):
            
            if node is None:
                return False
            # print(node.val, target.val)
            if node.val == target.val:
                self.t = node
                return True
            self.parents.append(node)
            if search(node.left):
                return True
            if search(node.right):
                return True
            self.parents.pop()
            return False
        search(root)
        self.s = []
        def add(node, k):
            if node is None:
                return
            if k == 0:
                self.s.append(node.val)
                return
            add(node.left, k - 1)
            add(node.right, k - 1)
        # print(self.parents, self.t)
        add(self.t, k)
        while(self.parents):
            k -= 1
            if k == 0:
                self.s.append(self.parents.pop().val)
                break
            if self.t == self.parents[-1].left:
                self.t = self.parents.pop()
                add(self.t.right, k - 1)
            else:
                self.t = self.parents.pop()
                add(self.t.left, k - 1)
        return self.s