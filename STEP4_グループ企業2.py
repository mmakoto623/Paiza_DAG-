import sys
sys.setrecursionlimit(1000000)

maxprofit= [-1] * (100001)
def calc(n):

    profit= [1] * (100001)
    group =[[] for _ in range(100001)]

    def _calc(kaisya_num,group):
        if maxprofit[kaisya_num] != -1:
            return maxprofit[kaisya_num]
        x = profit[kaisya_num]
        for i in range(len(group[kaisya_num])):
            x = max(x,_calc(group[kaisya_num][i],group))
        maxprofit[kaisya_num]=x
        return x

    R=[int(i) for i in input().split()]
    for i in range(n):
        profit[i] = R[i]

    for i in range(n-1):
        c,d=map(int,input().split())
        group[c].append(d)

    return _calc(0,group)

N ,Q=map(int,input().split())
calc(N)

for i in range(Q):
    print(maxprofit[int(input())])
