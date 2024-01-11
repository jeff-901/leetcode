class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        inventory.sort(reverse = True)
        cur = 0
        cur_level = inventory[0]
        cnt = 0
        ans = 0
        n = len(inventory)
        while(orders > 0):
            while(cur < n and inventory[cur] == cur_level):
                cur += 1
                cnt += 1
            if cur > n - 1:
                next_level = 0
            else:
                next_level = inventory[cur]
            diff = cur_level - next_level
            if orders > cnt * diff:
                orders -= cnt * diff
                ans += cnt * (cur_level + next_level + 1) * diff / 2
            else:
                diff = orders // cnt
                orders -= cnt * diff
                ans += cnt * (cur_level + cur_level - diff + 1) * diff / 2
                ans += (cur_level - diff) * orders
                orders = 0
            cur_level = next_level
            cur += 1
            cnt += 1
        return ans % (10**9+7)