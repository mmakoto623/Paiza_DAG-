import sys
sys.setrecursionlimit(1000000)

def job_memo(job):
    relation=[[] for _ in range(100001)]
    memo = [-1] * (100001)
    for i in range(k):
        j,w=map(int,input().split())
        relation[w-1].append(j-1)
        for j in range(N):
            if len(relation[j])!=0:
                relation[j]=sorted(relation[j])

    def _job(job):
        if memo[job]!=-1:
            return memo[job]
        if len(relation[job])==0:
            memo[job]=1
            return 1
        cnt=0
        for i in range(len(relation[job])):
            cnt += _job(relation[job][i])
            cnt %= 1000000007
        memo[job] = cnt
        return cnt
        
    return _job(job)

N,k = map(int,input().split())
print(job_memo(N-1))
