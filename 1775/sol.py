class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        nums1_cnt = [0, 0, 0, 0, 0, 0]
        nums2_cnt = [0, 0, 0, 0, 0, 0]
        s1 = 0
        s2 = 0
        for num1 in nums1:
            s1 += num1
            nums1_cnt[num1-1] += 1
        for num2 in nums2:
            s2 += num2
            nums2_cnt[num2-1] += 1
        if s1 > s2:
            tmp = s1
            s1 = s2
            s2 = tmp
            tmp = nums1_cnt[:]
            nums1_cnt = nums2_cnt
            nums2_cnt = tmp[:]
        ans = 0
        for i in range(5):
            available = nums1_cnt[i] + nums2_cnt[5-i]
            cnt = (s2 - s1 + (4-i)) // (5 - i)
            s1 += (5-i) * available
            if s1 < s2:
                ans += available
            else:
                ans += cnt
                break
        if s1 < s2:
            return -1
        return ans