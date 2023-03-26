# paizaの模範解答に近い書き方

import sys
sys.setrecursionlimit(1000000)

def calc_revenue(kaisya_num,graph):
    if len(graph[kaisya_num]) == 0:
        graph[kaisya_num]=1
        return 1
    cnt=1
    for i in range(len(graph[kaisya_num])):
        cnt+=calc_revenue(graph[kaisya_num][i],graph)
    revenue[kaisya_num]=cnt
    return cnt

N ,Q=map(int,input().split())

revenue= [1] * (100001)
graph =[[] for _ in range(100001)]
for i in range(N-1):
    c,d=map(int,input().split())
    graph[c].append(d)

calc_revenue(0,graph)

for i in range(Q):
    print(revenue[int(input())])
