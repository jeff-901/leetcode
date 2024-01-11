class Solution(object):
    def minAbsDifference(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        n = len(nums)
        first = nums[:n//2]
        second = nums[n//2:]
        sum1, sum2 = set(), set()
        for num in first:
            sum1.update({num + ele for ele in sum1})
            sum1.add(num)
        for num in second:
            sum2.update({num + ele for ele in sum2})
            sum2.add(num)
        sum2.add(0)
        ans = abs(goal)
        sum2 = sorted(sum2)
        idx = bisect.bisect_left(sum2, goal)
        if idx < len(sum2):
            ans = min(ans, abs(goal - sum2[idx]))
        ans = min(ans, abs(goal - sum2[idx-1]))
        for num in sum1:
            idx = bisect.bisect_left(sum2, goal - num)
            if idx < len(sum2):
                ans = min(ans, abs(goal - num - sum2[idx]))
            ans = min(ans, abs(goal - sum2[idx-1] - num))
        return ans
