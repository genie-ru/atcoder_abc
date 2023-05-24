A, B = int(input().split())
while A <= B:
    if A % 3 == 0:
        print(A)
        break
    A += 1