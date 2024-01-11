class Solution(object):
    def maxProduct(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        palindrome = []
        for i in range(1, 2**n):
            cur = ""
            for j in range(n):
                if i & (1 << j):
                    cur += s[j]
            left = 0
            right = len(cur) - 1
            flag = True
            while(left < right):
                if cur[left] != cur[right]:
                    flag = False
                left += 1
                right -= 1
            if flag:
                palindrome.append((len(cur), i))
        palindrome.sort(reverse = True)
        ans = 1
        for i in range(len(palindrome)):
            for j in range(i+1, len(palindrome)):
                product = palindrome[i][0] * palindrome[j][0]
                if product <= ans:
                    break
                if not (palindrome[i][1] & palindrome[j][1]):
                    ans = max(ans, product)
        return ans