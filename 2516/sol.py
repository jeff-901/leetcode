class Solution(object):
    def takeCharacters(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cnt = [0, 0, 0]
        for ele in s:
            cnt[ord(ele) - 97] += 1
        for i in range(3):
            cnt[i] -= k
            if cnt[i] < 0:
                return -1
        start = 0
        n = len(s)
        for end in range(n):
            cnt[ord(s[end]) - 97] -= 1
            if cnt[0] < 0 or cnt[1] < 0 or cnt[2] < 0:
                cnt[ord(s[start]) - 97] += 1
                start += 1
        return n - (end - start + 1)