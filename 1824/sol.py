class Solution(object):
    def minSideJumps(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: int
        """
        dp = [1, 0, 1]
        for i in range(2, len(obstacles)):
            if obstacles[i-1] != 0:
                need_jump = obstacles[i-1] - 1
                if obstacles[i] != need_jump + 1:
                    left = (need_jump - 1) % 3
                    right = (need_jump + 1) % 3
                    if obstacles[i] == left + 1:
                        dp[need_jump] = dp[right] + 1
                    elif obstacles[i] == right + 1:
                        dp[need_jump] = dp[left] + 1
                    else:
                        dp[need_jump] = min(dp[left], dp[right]) + 1
        return min(dp)