class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        h = math.floor(math.log(label, 2)) + 1
        ans = [label]
        if h % 2 == 0:
            label = 2**h - label + 2**(h-1) - 1
        h -= 1
        while(h > 0):
            if h % 2:
                # odd
                label = int(label // 2)
                ans.insert(0, label)
            else:
                #even
                label = int(label // 2)
                ans.insert(0, int(2**h - label + 2**(h-1) - 1))
            h -= 1
        return ans