def p_a():
    a, p = map(int, input().split())
    print((3 * a + p) // 2)


def p_b():
    n = int(input())
    sp = []
    for i in range(n):
        tmp = input().split()
        sp.append((tmp[0], int(tmp[1]), i + 1))
    sp.sort(key=lambda x: x[1], reverse=True)
    sp.sort(key=lambda x: x[0])
    print(*[x[2] for x in sp])


def p_c():
    n, m = map(int, input().split())
    s = [list(map(int, input().split()))[1:] for _ in range(m)]
    *p, = map(int, input().split())
    b = []
    for _s in s:
        bit = 0
        for i in _s:
            bit += (1 << (i - 1))
        b.append(bit)
    ans = 0
    for i in range(1 << n):
        for j, k in enumerate(b):
            if bin(i & k).count("1") & 1 != p[j]:
                break
        else:
            ans += 1
    print(ans)


from bisect import bisect_left


def p_d():
    n, k = map(int, input().split())
    *v, = map(int, input().split())
    ans = 0
    for _l in range(k + 1):
        for _r in range(k - _l + 1):
            if _l + _r > n:
                break
            d = k - (_l + _r)
            s = v[:_l] + v[n - _r:]
            s.sort()
            d = min(len(s), d)
            ans = max(ans, sum(s[bisect_left(s, 0, 0, d):]))

    print(ans)


def p_e():
    pass


def p_f():
    pass


if __name__ == '__main__':
    p_d()
