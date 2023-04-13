import sys
sys.setrecursionlimit(1000000)

N = int(input())
tree=[[] for _ in range(N)]
for i in range(N-1):
    s,t=map(int,input().split())
    s-=1
    t-=1
    tree[s].append(t)
    tree[t].append(s)

def painttree():
    def dfs(cur,parent,tree,cnt):
        for i in range(len(tree[cur])):
            next_cur=tree[cur][i]
            if next_cur==parent:
                continue
            cnt*=2
            cnt%= 1000000007
            cnt=dfs(next_cur,cur,tree,cnt)
        return cnt
    
    return dfs(0,-1,tree,3)

print(painttree())
