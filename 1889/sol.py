class Solution(object):
    def minWastedSpace(self, packages, boxes):
        """
        :type packages: List[int]
        :type boxes: List[List[int]]
        :rtype: int
        """
        packages.sort()
        ans = float("inf")
        n = len(packages)
        cache = {}
        for box_arr in boxes:
            box_arr.sort()
            last_left = -1
            s_box = 0
            if box_arr[-1] < packages[-1]:
                continue
            for i in range(len(box_arr)):
                box = box_arr[i]
                if last_left >= n - 1:
                    break
                if box in cache:
                    right = cache[box]
                else:
                    right = n - 1
                    left = last_left + 1
                    while(left <= right):
                        mid = (left + right) // 2
                        if packages[mid] <= box:
                            left = mid + 1
                        else:
                            right = mid - 1
                    cache[box] = right
                s_box += box * (right - last_left)
                last_left = right
            ans = min(ans, s_box)
        return (ans-sum(packages)) % (10**9+7) if ans < float("inf") else -1