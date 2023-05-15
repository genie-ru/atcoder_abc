N, A = int(input()), list(map(int, input().split()))
for i in range(N - 1):
    print(A[i], end=' ')
    if A[i] < A[i + 1]:
        for x in range(A[i] + 1, A[i + 1]):
            print(x, end=' ')
    else:
        for x in range(A[i] - 1, A[i + 1], -1):
            print(x, end=' ')
print(A[-1])
