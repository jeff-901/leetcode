class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        max_from_left = [arr[0]]
        l = len(arr)
        for i in range(1, len(arr)):
            max_from_left.append(max(max_from_left[-1], arr[i]))
        min_from_right = arr[-1]
        ans = 0
        for i in range(l-2, -1, -1):
            if min_from_right >= max_from_left[i]:
                ans += 1
            min_from_right = min(min_from_right, arr[i])
        return ans + 1