class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        arr.sort()
        n = len(arr)
        prefix = [0]
        for i in range(n):
            prefix.append(prefix[-1] + arr[i])
        if prefix[-1] <= target:
            return arr[-1]
        left = 0
        right = arr[-1]
        left_diff = target
        right_diff = prefix[-1] - target
        mi = target
        ans = left
        while(left <= right):
            mid = (left + right) // 2
            idx = bisect.bisect_left(arr, mid)
            s = prefix[idx] + (n - idx) * mid
            if s < target:
                if target - s < mi:
                    ans = mid
                    mi = target - s
                left = mid + 1
            else:
                right = mid - 1
        idx = bisect.bisect_left(arr, left)
        s = prefix[idx] + (n - idx) * left
        if abs(target - s) < mi:
            ans = left
        return ans