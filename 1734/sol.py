class Solution(object):
    def decode(self, encoded):
        """
        :type encoded: List[int]
        :rtype: List[int]
        """
        xor = 0
        n = len(encoded) + 1
        for num in range(1, n+1):
            xor ^= num
        for i in range(1, n-1, 2):
            xor ^= encoded[i]
        ans = [xor]
        for code in encoded:
            xor ^= code
            ans.append(xor)
        return ans