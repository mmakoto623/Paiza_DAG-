N,M,B = map(int,input().split())

block=[[False ]*N for _ in range(M)] 
for _ in range(B):
    X,Y = map(int,input().split())
    block[Y-1][X-1] = True
    
dp=[[0]*N for _ in range(M)]

dp[0][0]=1
for y in range(M):
	for x in range(N):
		if block[y][x] == True :
			continue
		if (x+1 < N) and (block[y][x+1]==False):
			dp[y][x+1] = (dp[y][x+1]+dp[y][x]) % 1000000007
		if (y+1 < M) and (block[y+1][x]==False):
			dp[y+1][x] = (dp[y+1][x]+dp[y][x]) % 1000000007

print(dp[M-1][N-1])

