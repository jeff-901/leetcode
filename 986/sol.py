class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        left = 0
        right = 0
        while(left < len(firstList) and right < len(secondList)):
            a1, a2 = firstList[left]
            b1, b2 = secondList[right]
            start = max(a1, b1)
            if a2 < b2:
                end = a2
                left += 1
            else:
                end = b2
                right += 1
            if start <= end:
                ans.append([start, end])
        return ans
            