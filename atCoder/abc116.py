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
    li = []
    for _ in range(N):
        t, d = map(int, input().split())
        li.append((t, d))
    li.sort(key=lambda x: x[1], reverse=True)
    kind = set()
    ans = 0
    for i in range(K):
        ans += li[i][1]
        if li[i][0] not in kind:
            kind.add(li[i][0])
    ans += len(kind) ** 2
    print(ans)


if __name__ == '__main__':
    p_d()
