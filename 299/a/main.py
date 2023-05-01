n = int(input())
s = input()

# 文字列sが2つの|で囲まれた領域内にちょうど1つの*があるかどうかを判定する
if s.count('|') == 2 and s.count('*') == 1 and s.index('*') > s.index('|') and s.rindex('*') < s.rindex('|'):
    print('in')
else:
    print('out')
