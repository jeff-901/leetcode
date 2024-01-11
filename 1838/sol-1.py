class Solution(object):
    def maxFrequency(self, nums, k):
        i = 0
        nums.sort()
        for j in range(len(nums)):
            k=k+nums[j]
            if k< nums[j] * (j - i + 1):
                k -= nums[i]
                i += 1
        return j - i + 1