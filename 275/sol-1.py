class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations[-1] == 0:
            return 0
        n = len(citations)
        left = 0
        right = n
        while(left < right):
            middle = (left + right) // 2
            if citations[middle] >= n - middle:
                right = middle
            else:
                left = middle + 1
        return n - right