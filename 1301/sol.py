class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        n = len(board)
        dp = [[0, 1]] * n
        dp[-1] = [1, 1]
        for col in range(n-2, -1, -1):
            if board[-1][col] == 'X':
                break
            dp[col] = [dp[col+1][0] + int(board[-1][col]), 1]
        for row in range(n-2, -1, -1):
            last = dp[n-1][0]
            last_cnt = dp[n-1][1]
            if board[row][n-1] == "X" or board[row+1][n-1] == "X":
                dp[n-1] = [0, 1]
            else:
                dp[n-1] = [dp[n-1][0] + int(board[row][n-1]), 1]
            for col in range(n-2, -1, -1):
                if board[row][col] == "X":
                    last = dp[col][0]
                    last_cnt = dp[col][1]
                    dp[col] = [0, 1]
                    continue
                elif board[row][col] == "E":
                    num = 0
                else:
                    num = int(board[row][col])
                max_num = dp[col+1][0]
                cnt = dp[col+1][1]
                if last > max_num:
                    max_num = last
                    cnt = last_cnt
                elif last == max_num:
                    cnt += last_cnt
                if dp[col][0] > max_num:
                    max_num = dp[col][0]
                    cnt = dp[col][1]
                elif dp[col][0] == max_num:
                    cnt += dp[col][1]
                last, last_cnt = dp[col]
                if max_num == 0:
                    dp[col] = [0, 1]
                else:
                    dp[col] = [max_num + num, cnt % 1000000007]
        if dp[0][0] == 0:
            return [0, 0]
        dp[0][0] -= 1
        return dp[0]