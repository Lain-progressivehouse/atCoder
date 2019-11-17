def p_a():
    n, k = map(int, input().split())
    s = input()
    print(s[:k - 1] + str.lower(s[k - 1]) + s[k:])


def p_b():
    s = input()
    if 1 <= int(s[0:2]) < 13:
        if 1 <= int(s[2:4]) < 13:
            print("AMBIGUOUS")
        else:
            print("MMYY")
    else:
        if 1 <= int(s[2:4]) < 13:
            print("YYMM")
        else:
            print("NA")


def p_c():
    n, k = map(int, input().split())
    ans = 0
    m = min(n, k - 1)
    for i in range(1, m + 1):
        x = 0
        while k > i << x:
            x += 1
        ans += (1 / n) * (1 / (1 << x))
    if m == k - 1:
        ans += (n - k + 1) / n

    print(ans)


def p_d():
    pass


def p_e():
    pass


def p_f():
    pass


if __name__ == '__main__':
    p_c()
