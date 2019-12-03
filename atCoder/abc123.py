def p_a():
    x = [int(input()) for _ in range(5)]
    k = int(input())
    print("Yay!" if x[4] - x[0] <= k else ":(")


def p_b():
    x = [int(input()) for _ in range(5)]
    m = 10
    idx = -1
    for i, e in enumerate(x):
        tmp = int(str(e)[-1])
        if tmp == 0:
            continue
        if m > tmp:
            m = tmp
            idx = i
    ans = 0
    for i, e in enumerate(x):
        if i == idx:
            ans += e
        else:
            ans += (e + 9) // 10 * 10

    print(ans)


def p_c():
    n = int(input())
    city = [int(input()) for _ in range(5)]
    m = min(city)
    print(4 + (n + m - 1) // m)


def p_d():
    x, y, z, k = map(int, input().split())
    candles = []
    for i in range(3):
        *tmp, = map(int, input().split())
        tmp.sort(reverse=True)
        candles.append(tmp)
        # candles.append(deque(tmp))
    c = []
    for i in range(x):
        for j in range(y):
            c.append(candles[0][i] + candles[1][j])
    c.sort(reverse=True)
    ans = []
    for _c in c[:k]:
        for i in candles[2][:min(z, k)]:
            ans.append(_c + i)
    ans.sort(reverse=True)
    print("\n".join(map(str, ans[:k])))


if __name__ == '__main__':
    p_d()
