class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        """
        :type fruits: List[List[int]]
        :type startPos: int
        :type k: int
        :rtype: int
        """
        cnt = 0
        ans = 0
        left = 0
        n = len(fruits)
        while(left < n and fruits[left][0] < startPos - k):
            left += 1
        right = n - 1
        while(right > -1 and fruits[right][0] > startPos + k):
            right -= 1
        for end in range(left, right + 1):
            pos, val = fruits[end]
            cnt += val
            while(abs(pos - fruits[left][0]) + min(pos-startPos, abs(startPos-fruits[left][0])) > k):
                cnt -= fruits[left][1]
                left += 1
            ans = max(ans, cnt)
        return ans