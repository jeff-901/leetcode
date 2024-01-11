class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        inventory.sort(reverse = True)
        left = 1
        right = max(inventory)
        while(left <= right):
            mid = (left + right) // 2
            total_order = 0
            for ele in inventory:
                if ele >= mid:
                    total_order += ele - mid + 1
                else:
                    break
            if total_order < orders:
                right = mid - 1
            else:
                left = mid + 1
        total_order = 0
        ans = 0
        for ele in inventory:
            if ele >= right:
                ans += (ele + right) * (ele - right + 1) / 2
                total_order += ele - right + 1
        ans -= right * (total_order - orders)
        return ans % (10**9+7)