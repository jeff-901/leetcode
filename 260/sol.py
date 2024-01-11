class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor ^= num
        right_most_bit = xor & -xor
        xor_1 = 0
        for num in nums:
            if num & right_most_bit:
                xor_1 ^= num
        return [xor_1, xor^xor_1]