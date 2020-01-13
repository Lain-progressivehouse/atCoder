def p_a():
    a, b, c = map(int, input().split())
    print(a * b // 2)


def p_b():
    s = int(input())
    u = {s}
    for i in range(1, 1000001):
        if s & 1 == 0:
            s //= 2
        else:
            s = 3 * s + 1
        if s in u:
            print(i + 1)
            exit()
        else:
            u.add(s)


def p_c():
    n = int(input())
    *H, = map(int, input().split())
    ans = 0
    while sum(H) > 0:
        bf = False
        st = 0
        while H[st] == 0:
            st += 1
        for i in range(st, n):
            if H[i] == 0:
                if bf:
                    ans += 1
                bf = False
            else:
                H[i] -= 1
                bf = True
                if i == n - 1:
                    ans += 1
    print(ans)


def p_d():
    N, K = map(int, input().split())
    inf = 10 ** 18
    sushi = [[-inf] for _ in range(N)]
    max_kind = -1
    for _ in range(N):
        t, d = map(int, input().split())
        sushi[t - 1].append(d)
        if max_kind < t:
            max_kind = t
    for i in range(max_kind):
        sushi[i].sort(reverse=True)
    sushi.sort(key=lambda x: x[0], reverse=True)

    que = []
    res = 0
    for i in range(K):
        res += sushi[i][0]
        for j in sushi[i][1:]:
            que.append(j)
    que.sort()
    cur = res
    res += K ** 2
    for var in range(1, K)[::-1]:
        a = que.pop()
        b = sushi[var][0]
        cur += a - b
        res = max(res, cur + var ** 2)
    print(res)


if __name__ == '__main__':
    p_d()
