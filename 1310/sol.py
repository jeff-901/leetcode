class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1]
        arr.append(0)
        return [arr[r] ^ arr[l-1] for l, r in queries]