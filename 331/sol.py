class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder.split(",")
        n = len(preorder)
        def build(cur):
            if cur >= n or preorder[cur] == "#":
                return cur
            else:
                cur = build(cur + 1)
                cur = build(cur + 1)
                return cur
        return build(0) == n - 1

