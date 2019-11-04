def p_a():
    pqr = list(map(int, input().split()))
    print(sum(pqr) - max(pqr))


def p_b():
    nb = int(input())
    wb = list(map(int, input().split()))
    current = 0
    ans = 10 ** 5
    for i in wb:
        current += i
        ans = min(ans, abs(sum(wb) - 2 * current))
    print(ans)


def p_c():
    nb, mb = map(int, input().split())
    mod = 10 ** 9 + 7
    ans = 1
    fb = [1, 1]
    current = 0
    for _ in range(mb):
        a = int(input())
        width = a - current - 1
        if width == -1:
            ans = 0
            break
        while width > len(fb) - 1:
            fb.append(fb[-1] + fb[-2])
        ans *= fb[width]
        current = a + 1
        ans %= mod
    width = nb - current
    while width > len(fb) - 1:
        fb.append(fb[-1] + fb[-2])
    ans *= fb[width]
    ans %= mod
    print(ans)


def p_d():
    hb, wb = map(int, input().split())
    t = [input() for _ in range(hb)]
    lb = [[0] * (wb + 2) for _ in range(hb + 2)]
    rb = [[0] * (wb + 2) for _ in range(hb + 2)]
    ub = [[0] * (wb + 2) for _ in range(hb + 2)]
    db = [[0] * (wb + 2) for _ in range(hb + 2)]
    for h in range(1, hb + 1):
        for w in range(1, wb + 1):
            if t[h - 1][w - 1] != "#":
                lb[h][w] = lb[h][w - 1] + 1
                ub[h][w] = ub[h - 1][w] + 1
            if t[hb - h][wb - w] != "#":
                rb[hb - h + 1][wb - w + 1] = rb[hb - h + 1][wb - w + 2] + 1
                db[hb - h + 1][wb - w + 1] = db[hb - h + 2][wb - w + 1] + 1
    ans = 0
    for h in range(1, hb + 1):
        for w in range(1, wb + 1):
            tmp = lb[h][w] + rb[h][w] + ub[h][w] + db[h][w]
            ans = max(ans, tmp - 3)
    print(ans)


def p_e():
    pass


def p_f():
    pass


if __name__ == '__main__':
    p_d()
