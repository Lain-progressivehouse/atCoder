def p_a():
    A, B = map(int, input().split())
    print(A * B if A < 10 and B < 10 else -1)


def p_b():
    N = int(input())
    for i in range(1, 10):
        for j in range(1, 10):
            if N == i * j:
                print("Yes")
                exit()
    print("No")


import math


def p_c():
    N = int(input())
    m = int(math.sqrt(N))

    for i in reversed(range(1, m + 1)):
        if N % i == 0:
            print(i + N // i - 2)
            break


def p_d():
    a, b, x = map(int, input().split())
    if 2 * x / a ** 2 >= b:
        h = b - x / a ** 2
        w = a / 2
        ans = math.degrees(math.atan(h / w))
    else:
        h = b
        w = 2 * x / (a * b)
        ans = math.degrees(math.atan(h / w))
    print(ans)


def p_e():
    n, k = map(int, input().split())
    *A, = map(int, input().split())
    *F, = map(int, input().split())
    A.sort()
    F.sort(reverse=True)

    def check(x):
        count = 0
        for a, f in zip(A, F):
            count += max(a - x // f, 0)
        return count <= k

    max_num = 0
    for a, f in zip(A, F):
        if max_num < a * f:
            max_num = a * f
    l, h = 0, max_num
    while l <= h:
        mid = (l + h) // 2
        if check(mid):
            h = mid - 1
        else:
            l = mid + 1
    print(h + 1)


def p_f():
    pass


if __name__ == '__main__':
    p_e()
