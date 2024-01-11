import math
class Solution(object):
    def largestComponentSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        parents = [_ for _ in range(n)]
        size = [1 for _ in range(n)]
        ans = 1
        
        def find(idx):
            if parents[idx] == idx:
                return idx
            parents[idx] = find(parents[idx])
            return parents[idx]

        def get_prime_set(start, num):
            res = set()
            for i in range(start, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    num //= i
                    while(num > 1 and num % i == 0):
                        num //= i
                    res.add(i)
                    if num > 1:
                        res = res.union(get_prime_set(i+1, num))
                    return res 
            return {num}

        primes = {}
        for i in range(n):
            for prime in get_prime_set(2, nums[i]):
                if prime in primes:
                    primes[prime].append(i)
                else:
                    primes[prime] = [i]

        for prime in primes:
            cur_idx = primes[prime][0]
            cur_p = find(cur_idx)
            for j in range(1, len(primes[prime])):
                j_p = find(primes[prime][j])
                if cur_p == j_p: continue
                parents[j_p] = cur_p
                size[cur_p] += size[j_p]
                ans = max(ans, size[cur_p])

        return ans