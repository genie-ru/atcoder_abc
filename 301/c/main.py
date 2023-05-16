#参考
def can_win(S, T):
    replaceable = 'atcoder'
    S_counts = [0] * 8  # 各文字の出現回数を格納するリスト
    T_counts = [0] * 8

    for char in S:
        if char in replaceable:
            S_counts[replaceable.index(char)] += 1
        elif char == '@':
            S_counts[7] += 1

    for char in T:
        if char in replaceable:
            T_counts[replaceable.index(char)] += 1
        elif char == '@':
            T_counts[7] += 1

    for i in range(7):  # 特定の文字について比較し、@の数を調整
        if S_counts[i] < T_counts[i]:
            needed = T_counts[i] - S_counts[i]
            if S_counts[7] >= needed:
                S_counts[7] -= needed
            else:
                return 'No'
        elif T_counts[i] < S_counts[i]:
            needed = S_counts[i] - T_counts[i]
            if T_counts[7] >= needed:
                T_counts[7] -= needed
            else:
                return 'No'

    return 'Yes' if S_counts[7] == T_counts[7] else 'No'

S = input()
T = input()
print(can_win(S, T))
