class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        n = len(position)
        if m == 2:
            return position[-1] - position[0]
        left = 1
        right = position[-1] - position[0]
        while(left <= right):
            mid = (left + right) // 2
            cur = position[0]
            balls = 1
            for i in range(1,n):
                if position[i] - cur >= mid:
                    balls += 1
                    cur = position[i]
            if balls >= m:
                left = mid + 1
            else:
                right = mid - 1
        return right