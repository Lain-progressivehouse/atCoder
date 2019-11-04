def p_a():
    x, a = map(int, input().split())
    print(0 if x < a else 10)


def p_b():
    n, x = map(int, input().split())
    v = 0
    ans = 1
    for i in list(map(int, input().split())):
        v += i
        if v <= x:
            ans += 1
        else:
            break
    print(ans)


def p_c():
    W, H, x, y = map(int, input().split())
    is1 = (W / 2 == x) and (H / 2 == y)
    print(W * H / 2, 1 if is1 else 0)


def p_d():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    st = 0
    ed = 0
    sum_value = 0
    ans = 0
    while ed <= N:
        if K <= sum_value:
            ans += N + 1 - ed
            sum_value -= a[st]
            st += 1
        else:
            if ed < N:
                sum_value += a[ed]
            ed += 1
    print(ans)


def p_e():
    pass


def p_f():
    pass


if __name__ == '__main__':
    p_d()
