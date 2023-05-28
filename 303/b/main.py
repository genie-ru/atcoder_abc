N, M = map(int, input().split())

a = []
for _ in range(M):
    row = list(map(int, input().split()))
    a.append(row)

ans = 0

for i in range(1, N):
    for j in range(i + 1, N + 1):
        flag = False
        for k in range(M):
            for l in range(N - 1):
                if a[k][l] == i and a[k][l + 1] == j:
                    flag = True
                if a[k][l] == j and a[k][l + 1] == i:
                    flag = True
        if not flag:
            ans += 1

print(ans)
