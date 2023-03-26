import sys
sys.setrecursionlimit(1000000)

N = int(input())
def fib_memo(n):
    memo = [-1] * (n+1)
    def _fib(n):
        if n == 0 or n==1:
            memo[n]=n
            return memo[n]
        elif memo[n] != -1:
            return memo[n]
        else:
            tmp = _fib(n-1) + _fib(n-2)
            if tmp >1000000007:
                tmp=tmp%1000000007
            memo[n] = tmp
            return memo[n]
    return _fib(n)
print(fib_memo(N))
