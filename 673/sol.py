class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = [[(nums[0], 1)]]
        for i in range(1, len(nums)):
            num = nums[i]
            j = len(cnt) - 1
            while(j > -1):
                if num > cnt[j][0][0]:
                    break
                j -= 1
            if j == -1:
                cnt[0].insert(0, (num, 1))
            else:
                s = 0
                for ele, c in cnt[j]:
                    if ele >= num:
                        break
                    s += c
                if j == len(cnt) - 1:
                    cnt.append([(num, s)])
                else:
                    cnt[j+1].insert(0, (num, s))
        ans = 0
        for ele, c in cnt[-1]:
            ans += c
        return ans