class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        cnt = 0
        start = 0
        n = len(answerKey)
        for end in range(n):
            if answerKey[end] == "T":
                cnt += 1
            if cnt > k:
                if answerKey[start] == "T":
                    cnt -= 1
                start += 1
        ans = n - start
        cnt = 0
        start = 0
        for end in range(n):
            if answerKey[end] == "F":
                cnt += 1
            if cnt > k:
                if answerKey[start] == "F":
                    cnt -= 1
                start += 1
        ans = max(ans, n - start)
        return ans