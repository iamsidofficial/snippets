def solve():



        
def main():
    
    T = 1
    T ,= inp()

    for _ in range(T):
        x = solve()

        if x is not None:
            print(x)
    

from sys import stdin, stdout
from bisect import bisect, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop
from itertools import accumulate
from functools import lru_cache
from math import ceil, comb, factorial, gcd, isqrt, lcm, sqrt


input = lambda : stdin.readline().rstrip('\r\n')
inp = lambda dtype=int : list(map(dtype, input().split()))
flush = stdout.flush
convert = lambda data, sep='\n' : sep.join(map(str, data))

main()






