class Solution(object):
    def closestToTarget(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        ans = abs(arr[0] - target)
        val = set()
        for i in range(len(arr)):
            num = arr[i]
            last_val = val.copy()
            val = {num}
            ans = min(ans, abs(num - target))
            for ele in last_val:
                ans = min(ans, abs((ele&arr[i]) - target))
                val.add(ele&arr[i])
        return ans