class Solution(object):
    def latestDayToCross(self, row, col, cells):
        """
        :type row: int
        :type col: int
        :type cells: List[List[int]]
        :rtype: int
        """
        n = row*col
        parents = [-1 for _ in range(n+2)]
        def index(r, c):
            return r * col + c

        def find(idx):
            if parents[idx] == idx:
                return idx
            parents[idx] = find(parents[idx])
            return parents[idx]
        
        parents[n] = n
        parents[n+1] = n+1

        for i, (r, c) in enumerate(reversed(cells)):
            r -= 1
            c -= 1
            cur_idx = index(r, c)
            if r == 0:
                parents[cur_idx] = n
            elif r == row - 1:
                parents[cur_idx] = n + 1
            else:
                parents[cur_idx] = cur_idx
            cur_p = parents[cur_idx]
            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0 <= nr < row and 0 <= nc < col and parents[index(nr, nc)] != -1:
                    np = find(index(nr, nc))
                    if cur_p + np == 2 * n + 1:
                        return n - i - 1
                    if cur_p == n or cur_p == n + 1:
                        parents[np] = cur_p
                    else:
                        parents[cur_p] = np
                        cur_p = np
        return 0
