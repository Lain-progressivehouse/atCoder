def p_a():
    n, a, b = map(int, input().split())
    if (b - a) & 1 == 0:
        print((b - a) // 2)
        exit()
    print((b - a - 1) // 2 + min(a - 1, n - b) + 1)


if __name__ == '__main__':
    p_a()
