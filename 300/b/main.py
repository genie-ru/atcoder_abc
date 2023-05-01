H, W = map(int, input().split())
A = [input() for _ in range(H)]
B = [input() for _ in range(H)]
for s in range(H):
    for t in range(W):
        ok = 1
        for i in range(H):
            for j in range(W):
                if A[(i - s + H) % H][(j - t + W) % W] != B[i][j]:
                    ok = 0
        if ok:
            print("Yes")
            exit(0)
print("No")
