def p_a():
    S = input()

    if S == "Sunny":
        print("Cloudy")
    elif S == "Cloudy":
        print("Rainy")
    elif S == "Rainy":
        print("Sunny")


def p_b():
    S = input()

    f = True
    for i in range(len(S)):
        if i % 2 == 1:
            if S[i] == "R":
                f = False
        else:
            if S[i] == "L":
                f = False

    if f:
        print("Yes")
    else:
        print("No")


from collections import defaultdict


def p_c():
    N, K, Q = map(int, input().split())

    l = defaultdict(int)

    for _ in range(Q):
        A = int(input())
        l[A - 1] += 1

    for i in range(N):
        if K - Q + l[i] > 0:
            print("Yes")
        else:
            print("No")


from heapq import heappop, heappush
from math import ceil, floor


def p_d():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    H = []

    for a in A:
        heappush(H, a * -1)

    for _ in range(M):
        x = heappop(H)

        heappush(H, ceil(x / 2))

    ans = 0

    for a in H:
        ans -= a

    print(ans)


def p_e():
    N = int(input())
    S = input()

    l, r, ans = 0, 0, 0

    while r < N:
        if S[l:r] in S[r:N]:
            ans = max(ans, r - l)
            r += 1
        else:
            l += 1

    print(ans)


def p_f():
    N = int(input())
    A = list(map(int, input().split()))




if __name__ == '__main__':
    p_e()
