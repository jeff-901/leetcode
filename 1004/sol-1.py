class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        cnt = 0
        one_group = collections.deque()
        one_sum = 0
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                one_group.append(cnt)
                one_sum += cnt
                cnt = 0
                if len(one_group) == k + 1:
                    ans = max(ans, one_sum + k)
                    one_sum -= one_group.popleft()
        one_group.append(cnt)
        one_sum += cnt
        ans = max(ans, one_sum + len(one_group) - 1)
        return ans