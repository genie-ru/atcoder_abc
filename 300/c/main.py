H,W=map(int,input().split())
S=[input() for _ in range(H)]
ans=[0]*(min(H,W)+1)

for ij in range(H+W):
  T="".join([S[i][ij-i] for i in range(H) if 0<=ij-i<W])
  for c in map(len,T.split(".")): ans[c//2]+=1

print(*ans[1:])
