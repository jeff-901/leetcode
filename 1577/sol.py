class Solution(object):
    def numTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        ans = 0
        h1={}
        for ele in nums1:
            h1[ele] = h1.get(ele, 0) + 1
        for ele in nums2:
            target = ele ** 2
            for key in h1:
                if key == ele and h1[key] > 1:
                    ans += h1[key] * (h1[key] - 1) / 2
                elif key < ele:
                    if target % key == 0:
                        ans += h1.get(target//key, 0) * h1[key]
        h2={}
        for ele in nums2:
            h2[ele] = h2.get(ele, 0) + 1
        for ele in nums1:
            target = ele ** 2
            for key in h2:
                if key == ele and h2[key] > 1:
                    ans += h2[key] * (h2[key] - 1) / 2
                elif key < ele:
                    if target % key == 0:
                        ans += h2.get(target//key, 0) * h2[key]
        return ans
