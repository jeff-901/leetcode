class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = sum(nums)
        first = nums[:n//2]
        second = nums[n//2:]
        sum1 = [set() for _ in range(n//2+1)] 
        sum2 = [set() for _ in range(n//2+1)]
        sum1[0].add(0)
        sum2[0].add(0)
        for num in first:
            for j in range(n//2, 0, -1):
                for ele in sum1[j-1]:
                    sum1[j].add(num + ele)
            sum1[1].add(num)
        for num in second:
            for j in range(n//2, 0, -1):
                for ele in sum2[j-1]:
                    sum2[j].add(num + ele)
            sum2[1].add(num)
        for j in range(n//2+1):
            sum2[j] = sorted(sum2[j])
        ans = abs(sum(first) - sum(second))
        for i in range(n//2+1):
            for ele in sum1[i]:
                idx = bisect.bisect_left(sum2[n//2-i], (s//2) -  ele)
                if idx < len(sum2[n//2-i]):
                    ans = min(ans, abs(s - 2*(ele+sum2[n//2-i][idx])))
                if idx > 0:
                    ans = min(ans, abs(s - 2*(ele+sum2[n//2-i][idx-1])))
        return ans
