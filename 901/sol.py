class StockSpanner(object):

    def __init__(self):
        self.stack=[(-1, 100001)]
        self.idx = -1
    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.idx += 1
        while(self.stack[-1][1] <= price):
            self.stack.pop()
        self.stack.append((self.idx, price))
        return self.idx - self.stack[-2][0]
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)