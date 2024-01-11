class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        left = 1
        right = maxSum
        right_part = n - index - 1
        while(left <= right):
            mid = (left + right) // 2
            s = 0
            if mid >= index + 1:
                s += (mid * 2 - index) * (index + 1) / 2
            else:
                s += (mid + 1) * mid / 2 + (index + 1 - mid)
            if mid - 1 >= right_part:
                s += ((mid - 1) * 2 - (right_part - 1)) * right_part / 2
            else:
                s += mid * (mid - 1) / 2 + (right_part - (mid - 1))
            if s > maxSum:
                right = mid - 1
            else:
                left = mid + 1
        return right