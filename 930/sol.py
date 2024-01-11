class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        l = []
        c = 0
        for a in nums:
            if a:
                l.append(c)
                c = 0
            else:
                c += 1
        l.append(c)
        res = 0
        if goal > 0:
            i = 0
            while i+goal < len(l):
                res += (l[i]+1) * (l[i+goal]+1)
                i += 1
        else:
            for c in l:
                res += c*(c+1)/2
        return res