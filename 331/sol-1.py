class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        leaf_node = 1
        preorder = preorder.split(",")
        n = len(preorder)
        for i, val in enumerate(preorder):
            if val == "#":
                leaf_node -= 1
            else:
                leaf_node += 1
            if leaf_node == 0 and i != n-1:
                return False
        return leaf_node == 0