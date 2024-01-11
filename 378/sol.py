class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        left = matrix[0][0]
        right = matrix[-1][-1]
        n = len(matrix)
        while(left <= right):
            mid = (left + right) // 2
            cnt = 0
            i = 0
            j = n - 1
            while(i < n):
                while(j > -1 and matrix[i][j] > mid):
                    j -= 1
                cnt += j + 1
                i += 1
            if cnt < k:
                left = mid + 1
            else:
                right = mid - 1
        return left