import sys
sys.setrecursionlimit(1000000)

N = int(input())
tree=[[] for _ in range(N)]
memo=[0]*101010

def dfs(node,parent):
    for to,dist in tree[node]:
        if to==parent:
            continue
        memo[to]=memo[node]+dist
        dfs(to,node)

for i in range(N-1):
    s,t,d=map(int,input().split())
    s-=1
    t-=1
    tree[s].append([t,d])
    tree[t].append([s,d])

dfs(0,-1)
for i in range(N):
    print(memo[i])
