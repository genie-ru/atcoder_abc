N, A, B = map(int, (input().split()))
AB = A+B
C = list(map(int, input().split()))
ans = 0

for i in range(len(C)):
    if C[i] == AB:
        ans = i + 1
        break

print(ans)

