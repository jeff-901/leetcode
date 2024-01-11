class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(zip(nums2, nums1), reverse = True)
        ans = 0
        total = 0
        taken = []
        for i in range(k):
            total += nums[i][1]
            taken.append(nums[i][1])
        ans = total * nums[k-1][0]
        heapq.heapify(taken)
        for i in range(k, len(nums1)):
            total -= heapq.heappop(taken)
            total += nums[i][1]
            heapq.heappush(taken, nums[i][1])
            ans = max(ans, total * nums[i][0])
        return ans