class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cnt = [0 for _ in range(26)]
        start = 0
        n = len(s)
        max_cnt = 0
        for end in range(n):
            idx = ord(s[end]) - 65
            cnt[idx] += 1
            if cnt[idx] > cnt[max_cnt]:
                max_cnt = idx
            if end - start - cnt[max_cnt] + 1 > k:
                cnt[ord(s[start]) - 65] -= 1
                if start == max_cnt:
                    max_ = 0
                    for i in range(26):
                        if cnt[i] > max_:
                            max_ = cnt[i]
                            max_cnt = i
                start += 1
        return n - start
