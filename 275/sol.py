class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations[-1] == 0:
            return 0
        n = len(citations)
        left = -1
        right = n - 1
        while(left < right - 1):
            middle = (left + right) // 2
            if citations[middle] >= n - middle:
                right = middle
            else:
                left = middle
        return n - right