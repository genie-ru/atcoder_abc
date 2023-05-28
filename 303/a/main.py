N = int(input())
S = input()
T = input()

S1 = S.replace('o', '0').replace('l', '1')
T1 = T.replace('o', '0').replace('l', '1')

if S1 == T1:
    print('Yes')
else:
    print('No')
