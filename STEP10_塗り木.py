N = int(input())
tree=[[] for _ in range(N)]
for i in range(N-1):
    s,t=map(int,input().split())
    s-=1
    t-=1
    tree[s].append(t)
    tree[t].append(s)

ans=3
def dfs(cur,parent,tree):
    global ans
    for i in range(len(tree[cur])):
        next_cur=tree[cur][i]
        if next_cur==parent:
            continue
        ans*=2
        ans%= 1000000007
        dfs(next_cur,cur,tree)

dfs(0,-1,tree)
print(ans)
