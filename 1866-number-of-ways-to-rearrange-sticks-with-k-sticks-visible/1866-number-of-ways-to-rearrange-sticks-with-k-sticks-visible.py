from functools import cache
class Solution:

    def rearrangeSticks(self, n: int, k: int) -> int:
        return helper(n,k) % (10 ** 9 + 7)
@cache
def helper( n, k):
    if n == k:
        return 1 
    if n <= 0 and k <= 0:
        return 0 
    return (helper(n-1,k-1) + (n-1)*helper(n-1,k))