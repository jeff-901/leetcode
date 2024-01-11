class Solution(object):
    def wonderfulSubstrings(self, word):
        cnt, ans, mask = [1] + [0] * 1023, 0, 0
        for ch in word:
            mask ^= 1 << (ord(ch) - ord('a'))
            ans += cnt[mask]
            for n in range(10):
                ans += cnt[mask ^ 1 << n]
            cnt[mask] += 1
        return ans
            