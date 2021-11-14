class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        """
        :type encodedText: str
        :type rows: int
        :rtype: str
        """
        l = len(encodedText)
        if l == 0:
            return ""
        col = l // rows
        ans = ["" for _ in range((col - rows + 1) * rows + rows - 1)]
        c = 0
        r = 0
        for ele in encodedText:
            if r - c < 1 and c - r <= col - rows + 1:
                ans[(c - r) * rows + r] = ele
            c += 1
            if c == col:
                r += 1
                c = 0
        return "".join(ans).rstrip()
