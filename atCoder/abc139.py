def p_a():
    S = input()
    T = input()

    ans = 0

    for s, t in zip(list(S), list(T)):
        if s == t:
            ans += 1

    print(ans)


def p_b():
    A, B = map(int, input().split())
    print((B - 2 + A) // (A - 1))


def p_c():
    N = int(input())
    H = list(map(int, input().split()))

    b = H[0] - 1
    now = 0
    m = 0

    for h in H:
        if b >= h:
            now += 1
            b = h
        else:
            if m < now:
                m = now
            now = 0
            b = h

    if m < now:
        m = now

    print(m)


def p_d():
    N = int(input())
    print(N * (N - 1) // 2)


"""
未AC
"""

from collections import deque


def p_e():
    N = int(input())
    A = [deque(map(lambda x: x - 1, map(int, input().split()))) for _ in range(N)]

    ans = 0
    while True:
        idx = []
        l = list(range(N))

        for i in l:
            if not A[i]:
                continue

            if i == A[A[i][0]][0]:
                idx.append(i)
                l.pop(A[i])

        if not idx:
            break

        for i in idx:
            A[i].popleft()
        ans += 1

    for a in A:
        if a:
            print(-1)
            exit()

    print(ans)


if __name__ == '__main__':
    p_e()
