class Solution(object):
    def maximumRows(self, matrix, numSelect):
        """
        :type matrix: List[List[int]]
        :type numSelect: int
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        rows = []
        zero_row = 0
        for i in range(m):
            mask = 0
            for j in range(n):
                if matrix[i][j]: 
                    mask |= 1 << j
            if mask:
                rows.append(mask)
            else:
                zero_row += 1
        ans = 0
        for selection in combinations(range(n), numSelect):
            mask = 0
            for col in selection:
                mask |= 1 << col
            cnt = 0
            for row_mask in rows:
                if row_mask & mask == row_mask:
                    cnt += 1
            ans = max(ans, cnt)
        return ans + zero_row