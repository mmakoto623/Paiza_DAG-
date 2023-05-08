import sys
sys.setrecursionlimit(1000000)

N,M = map(int,input().split())
tree=[[] for _ in range(N)]
for _ in range(M):
    s,t=map(int,input().split())
    tree[s-1].append(t-1)
    tree[t-1].append(s-1)

def dfs(node,parent,memo):
    for to in tree[node]:
        if to == parent:
            continue
        memo[to]=memo[node]+1
        dfs(to,node,memo)
 
#最初の頂点から最も遠い頂点を探す
memo0=[0] * 101010
dfs(0,-1,memo0)
max_value = max(memo0)
max_value_index = memo0.index(max_value)

#最初の頂点から最も遠い頂点から最も遠い頂点まで距離を計算する
memo1=[0] * 101010
dfs(max_value_index,-1,memo1)
print(max(memo1))
