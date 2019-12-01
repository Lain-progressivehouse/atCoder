def p_a():
    m1, d1 = map(int, input().split())
    m2, d2 = map(int, input().split())
    print(0 if m1 == m2 else 1)


def p_b():
    n = int(input())
    for i in range(50000):
        if int(i * 1.08) == n:
            print(i)
            exit()
    print(":(")


def p_c():
    x = int(input())
    n = x // 100
    if x - (n * 100) <= 5 * n:
        print(1)
    else:
        print(0)


from collections import Counter
from collections import defaultdict


def p_d():
    n = int(input())
    *s, = map(int, input())
    nums = Counter(s)
    ans = 0
    alr_1 = set()
    for i in range(n - 2):
        nums[s[i]] -= 1
        if s[i] in alr_1:
            continue
        alr_1.add(s[i])
        alr_2 = set()
        tmp = defaultdict(int)
        for j in range(i + 1, n - 1):
            nums[s[j]] -= 1
            tmp[s[j]] += 1
            if s[j] in alr_2:
                continue
            alr_2.add(s[j])
            for key in nums.keys():
                if nums[key] == 0:
                    continue
                # print(s[i], s[j], key)
                ans += 1
        for key in tmp.keys():
            nums[key] += tmp[key]
    print(ans)


def p_e():
    n = int(input())
    *A, = map(int, input().split())
    mod = 1000000007
    dp = [0] * 3
    ans = 1
    for a in A:
        num = 0
        flg = True
        # print(dp)
        for j in range(3):
            if dp[j] == a:
                if flg:
                    dp[j] += 1
                    flg = False
                num += 1
        ans *= num
        ans %= mod

    print(ans)


def p_f():
    t1, t2 = map(int, input().split())
    a1, a2 = map(int, input().split())
    b1, b2 = map(int, input().split())

    # aの方がt1のときに先行している
    if a1 < b1:
        a1, b1 = b1, a1
        a2, b2 = b2, a2

    dif1 = a1 * t1 - b1 * t1
    dif2 = (b1 * t1 + b2 * t2) - (a1 * t1 + a2 * t2)
    # print(dif1)
    # print(dif2)
    if dif2 < 0:
        print(0)
        exit()
    if dif2 == 0:
        print("infinity")
        exit()
    if dif1 % dif2 == 0:
        print(dif1 // dif2 * 2)
    else:
        print((dif1 + dif2) // dif2 * 2 - 1)


if __name__ == '__main__':
    p_f()
