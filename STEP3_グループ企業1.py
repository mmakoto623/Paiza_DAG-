import sys
sys.setrecursionlimit(1000000)

profit= [1] * (100001)
def calc():

    def _calc(kaisya_num,group):
        if len(group[kaisya_num]) == 0:
            group[kaisya_num]=1
            return 1
        cnt=1
        for i in range(len(group[kaisya_num])):
            cnt+=_calc(group[kaisya_num][i],group)
        profit[kaisya_num]=cnt
        return cnt

    group =[[] for _ in range(100001)]
    for i in range(N-1):
        c,d=map(int,input().split())
        group[c].append(d)
    return _calc(0,group)

N ,Q=map(int,input().split())

calc()

for i in range(Q):
    print(profit[int(input())])
