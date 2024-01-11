import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        min_hp = []
        for i in range(min(k, len(nums1))):
            min_hp.append((nums1[i] + nums2[0], i, 0))
        n = len(nums2)
        ans = []
        while(k > 0 and min_hp):
            val, i, j = heapq.heappop(min_hp)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heapq.heappush(min_hp, (nums1[i] + nums2[j + 1], i, j + 1))
            k -= 1
        return ans