class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        count= [1 for _ in range(len(nums))]
        parent=[None for _ in range(len(nums))]
        best = 0
        for i in range(1, len(nums)):
            j = 0
            while(nums[i] >= nums[j] * 2):
                if nums[i] % nums[j]==0 and count[j] + 1 > count[i]:
                    parent[i] = j
                    count[i] = count[j]+1
                j += 1
            if count[best] < count[i]:
                best = i
        ans = []
        while(best != None):
            ans.append(nums[best])
            best = parent[best]
        return ans