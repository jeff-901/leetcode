class Solution(object):
    def getXORSum(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        xora = 0
        for num in arr1:
            xora ^= num
        xorb = 0
        for num in arr2:
            xorb ^= num
        return xora & xorb