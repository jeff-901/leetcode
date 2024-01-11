class Solution(object):
    def judgePoint24(self, cards):
        """
        :type cards: List[int]
        :rtype: bool
        """
        def check(cards):
            ops = [operator.add, operator.sub, operator.mul, operator.truediv]
            for op1 in ops:
                for op2 in ops:
                    for op3 in ops:
                        try:
                            if abs(op1(cards[0], op2(cards[1], op3(cards[2], cards[3]))) - 24) < 0.1:
                                return True
                        except:
                            pass
                        try:
                            if abs(op1(cards[0], op3(cards[3], op3(cards[1], cards[2]))) - 24) < 0.1:
                                return True
                        except:
                            pass
                        try:
                            if abs(op2(op1(cards[0], cards[1]), op3(cards[2], cards[3])) - 24) < 0.1:
                                
                                return True
                        except:
                            pass
                        try:
                            if abs(op3(op2(op1(cards[0], cards[1]), cards[2]), cards[3]) - 24) < 0.1:
                                return True
                        except:
                            pass
                        try:
                            if abs(op3(op1(op2(cards[1], cards[2]), cards[0]), cards[3]) - 24) < 0.1:
                                return True
                        except:
                            pass
            return False
        for p in permutations(cards):
            if check(p):
                return True
        return False
