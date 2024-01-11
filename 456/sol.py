class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = []
        highest = arr[0]
        for num in arr:
            lowest = num
            while(stack and stack[-1][1] > num):
                lowest, _ = stack.pop()
            highest = max(highest, num)
            stack.append([lowest, highest])
            #print(num, stack)
        return len(stack)