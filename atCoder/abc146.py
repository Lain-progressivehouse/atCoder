def p_a():
    t = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    s = input()
    print(7 - t.index(s))


def p_b():
    t = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    n = int(input())
    s = input()
    for i in list(s):
        print(t[(t.index(i) + n) % len(t)], end="")
    print()


def p_c():
    a, b, x = map(int, input().split())
    m = 1
    M = 10 ** 9
    while m <= M:
        mid = (m + M) // 2
        ans = a * mid + b * len(str(mid))
        if ans > x:
            M = mid - 1
        else:
            m = mid + 1
    print(mid if ans <= x else mid - 1)


def p_d():
    n = int(input())
    t = [[] for _ in range(n)]
    for i in range(n - 1):
        a, b = map(int, input().split())
        t[a - 1].append((i, b - 1))
    q = [(0, -1)]
    ans = [-1] * (n - 1)
    while q:
        print(ans)
        x, c0 = q.pop()
        c = 1
        for i, y in t[x]:
            if c == c0:
                c += 1
            ans[i] = c
            q.append((y, c))
            c += 1
    print(max(ans))
    for a in ans:
        print(a)


"""
E問題: 各要素の累積和の-1のmod kを計算することで
kまでの範囲で同じ値が存在する数の分だけansに追加する
"""

from collections import deque
from collections import defaultdict


def p_e():
    n, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    for i in range(n):
        a[i + 1] = (a[i + 1] + a[i] - 1) % k
    d = defaultdict(int)
    d[0] = 1
    q = deque()
    ans = 0
    for i in range(1, n + 1):
        if i - k >= 0:
            d[a[i - k]] -= 1
        ans += d[a[i]]
        d[a[i]] += 1
    print(ans)


"""
F問題: reverseして貪欲にすれば辞書順になる
"""


def p_f():
    n, m = map(int, input().split())
    *s, = map(int, input())
    s.reverse()
    i = 0
    ans = []
    while i + m < n:
        for j in reversed(range(i + 1, i + m + 1)):
            if s[j] == 0:
                ans.append(j - i)
                i = j
                break
        else:
            print(-1)
            exit()
    ans.append(n - i)
    print(*reversed(ans))


if __name__ == '__main__':
    p_f()
