class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left = 0
        n = len(arr)
        right = n - 1
        while(left <= right):
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        idx = left
        if left == n or (right != -1 and arr[left] - x >= x - arr[right]):
            idx = right
        start = idx - k + 1
        if start < 0:
            start = 0
        while(start + k < n and x - arr[start] > arr[start+k] - x):
            start += 1
        return arr[start: start+k]