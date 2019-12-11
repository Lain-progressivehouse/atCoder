def p_a():
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print((H - h) * (W - w))


def p_b():
    n, m, c = map(int, input().split())
    *b, = map(int, input().split())
    ans = 0
    for i in range(n):
        *a, = map(int, input().split())
        tmp = c
        for _a, _b in zip(a, b):
            tmp += _a * _b
        if tmp > 0:
            ans += 1
    print(ans)


def p_c():
    n, m = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    ab.sort()
    ans = 0
    for i in range(n):
        a, b = ab[i]
        b = min(m, b)
        ans += a * b
        m -= b
        if m == 0:
            break
    print(ans)


def p_d():
    L, R = map(int, input().split())

    def f(x):
        tmp = 0
        if not (x & 1):
            tmp = x
            x -= 1
        x = 0 if (x - 3) % 4 == 0 else 1
        return x + tmp

    print(f(L - 1) ^ f(R))


if __name__ == '__main__':
    p_d()
