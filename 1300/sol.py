class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        arr.sort()
        n = len(arr)
        i = 0
        while(i < n and (n-i) * arr[i] < target):
            target -= arr[i]
            i += 1
        if i == n:
            return arr[-1]
        res = target // (n - i)
        if target - res * (n-i) <= (n-i) //2:
            return res
        else:
            return res + 1