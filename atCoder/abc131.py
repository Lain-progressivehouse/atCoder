def p_a():
    n = input()
    b = ""
    for i in n:
        if b == i:
            print("Bad")
            exit()
        b = i
    print("Good")


def p_b():
    N, L = map(int, input().split())
    a = list(range(L, N + L))
    print(a)
    print(sum(a) - min(a, key=abs))


def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)


def p_c():
    A, B, C, D = map(int, input().split())
    A -= 1
    gcd_value = gcd(max(C, D), min(C, D))
    lcm_value = C * D // gcd_value
    print(B - A - B // C + A // C - B // D + A // D + B // lcm_value - A // lcm_value)


def p_d():
    N = int(input())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])
    n = 0
    for a, b in AB:
        n += a
        if n > b:
            print("No")
            exit()
    print("Yes")


def p_e():
    pass


def p_f():
    pass


if __name__ == '__main__':
    p_d()
