import heapq
class Solution(object):
    def getNumberOfBacklogOrders(self, orders):
        """
        :type orders: List[List[int]]
        :rtype: int
        """
        buys = []
        sells = []
        for price, amount, order in orders:
            if order == 0:
                if not sells or sells[0][0] > price:
                    heapq.heappush(buys, [-price, amount])
                else:
                    while amount > 0 and sells and sells[0][0] <= price:
                        if amount < sells[0][1]:
                            sells[0][1] -= amount
                            amount = 0
                        else:
                            amount -= sells[0][1]
                            heapq.heappop(sells)
                    if amount > 0:
                        heapq.heappush(buys, [-price, amount])
            else:
                if not buys or -buys[0][0] < price:
                    heapq.heappush(sells, [price, amount])
                else:
                    while amount > 0 and buys and -buys[0][0] >= price:
                        if amount < buys[0][1]:
                            buys[0][1]-=amount
                            amount=0
                        else:
                            amount-=buys[0][1]
                            heapq.heappop(buys)
                    if amount > 0:
                        heapq.heappush(sells, [price, amount])
        total = 0
        for _, amount in buys:
            total += amount
        total %= 10**9+7
        for _, amount in sells:
            total += amount
        total %= 10**9+7
        return total
                