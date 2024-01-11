class Solution(object):
    def smallestSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        mask = [0 for _ in range(31)]
        for i in range(n-1, -1, -1):
            num = bin(nums[i])[2:]
            for bit in range(1, len(num)+1):
                if num[-bit] == "1":
                    mask[bit-1] = i
            nums[i] = max(1, max(mask) - i + 1)
        return nums