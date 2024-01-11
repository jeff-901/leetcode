# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        n = mountain_arr.length()
        left = 1
        right = n - 2
        peak = 0
        while(left <= right):
            mid = (left + right) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid - 1):
                right = mid - 1
            elif mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                peak = mid
                break
        left = 0
        right = peak
        while(left <= right):
            mid = (left + right) // 2
            if mountain_arr.get(mid) > target:
                right = mid - 1
            elif mountain_arr.get(mid) < target:
                left = mid + 1
            else:
                return mid
        left = peak + 1
        right = n - 1
        while(left <= right):
            mid = (left + right) // 2
            if mountain_arr.get(mid) > target:
                left = mid + 1
            elif mountain_arr.get(mid) < target:
                right = mid - 1
            else:
                return mid
        return -1
