class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        one_group = collections.deque()
        one_group.append(-1)
        for idx, num in enumerate(nums):
            if num == 1:
                continue
            else:
                if len(one_group) == k + 1:
                    ans = max(ans, idx - one_group[0] - 1)
                    one_group.popleft()
                one_group.append(idx)
        ans = max(ans, len(nums) - one_group[0] - 1)
        return ans