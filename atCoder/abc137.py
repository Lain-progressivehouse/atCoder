def p_a():
    a, b = map(int, input().split())
    a1 = a * b
    a2 = a + b
    a3 = a - b

    print(max([a1, a2, a3]))


def p_b():
    a, b = map(int, input().split())

    ans = []
    for i in range(b - a + 1, b + a):
        ans.append(str(i))

    print(" ".join(ans))


from collections import Counter


def p_c():
    n = int(input())
    ans = 0

    l = ["".join(sorted(input())) for _ in range(n)]

    a = Counter(l).values()

    for i in a:
        ans += sum(range(i))

    print(ans)


from heapq import heappop, heappush


def p_d():
    n, m = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]

    ab.sort()
    ans = 0
    j = 0
    H = []

    for i in range(1, m + 1):
        while j < n and ab[j][0] <= i:
            heappush(H, -ab[j][1])
            j += 1

        if H:
            ans -= heappop(H)

    print(ans)


from collections import defaultdict


def p_e():
    N, M, P = map(int, input().split())
    abc = [tuple(map(int, input().split())) for _ in range(M)]
    li = defaultdict(set)

    for i in range(M):
        li[abc[i][0]].append((abc[i][1], -(abc[i][2] - P)))

    li_ans = defaultdict()
    li_ans[1] = 0
    li_top = [1]
    lt = []
    bf_n = -1
    while li_top and li_top != lt:
        lt = li_top.copy()
        li_top = []
        if N in li_ans.keys():
            bf_n = li_ans[N]

        for i in lt:
            for e in li[i]:
                if not e[0] in li_ans.keys():
                    li_ans[e[0]] = e[1] + li_ans[i]
                    li_top.append(e[0])
                else:
                    if li_ans[e[0]] > e[1] + li_ans[i]:
                        li_ans[e[0]] = e[1] + li_ans[i]
                        li_top.append(e[0])

    if li_top == lt and bf_n != li_ans[N]:
        print(-1)
    else:
        print(max(0, -li_ans[N]))


if __name__ == '__main__':
    p_e()
