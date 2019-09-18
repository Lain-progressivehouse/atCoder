def p_a():
    a, b, c = map(int, input().split())
    print(max(0, b + c - a))


def p_b():
    n = int(input())

    a = list(map(int, list(str(n))))
    a.reverse()

    ans = 0

    for i in range(len(a)):
        if i % 2 == 1:
            continue

        if i == len(a) - 1:
            ans += n - 10 ** i + 1
        else:
            ans += 9 * 10 ** i

    print(ans)


def p_c():
    n = int(input())
    H = list(map(int, input().split()))

    H.reverse()

    bf = 10 ** 9

    for h in H:
        if bf >= h:
            bf = h
        elif bf + 1 == h:
            pass
        else:
            print("No")
            exit()

    print("Yes")


from math import ceil, floor


def p_d():
    S = input()

    st = 0
    ans = []

    while st < len(S):

        rc = 0
        while st < len(S) and S[st] == "R":
            rc += 1
            st += 1

        lc = 0
        while st < len(S) and S[st] == "L":
            lc += 1
            st += 1

        l = ceil(rc / 2) + lc // 2
        r = rc // 2 + ceil(lc / 2)

        ans.extend([0] * (rc - 1))
        ans.append(l)
        ans.append(r)
        ans.extend([0] * (lc - 1))

    print(*ans)


from heapq import heappush, heappop


def get_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            heappush(divisors, -i)
            if i != n // i:
                heappush(divisors, -(n // i))

    return divisors


def p_e():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    sum_A = sum(A)

    divisors = get_divisors(sum_A)
    n = len(divisors)
    for _ in range(n):
        h = -heappop(divisors)
        sub_list = []
        for a in A:
            sub_list.append(a % h)

        x = sum(sub_list)
        sub_list.sort()
        print(sub_list)
        print("x: " + str(sum(sub_list)))
        print("h: " + str(h))
        print("-x // h: " + str(-x // h))
        print("sum(sub_list[:-x // h]): " + str(sum(sub_list[:-x // h])))

        # if x <= K * 2 and x % h == 0 and ():
        #     print(h)
        #     exit()
        if sum(sub_list[:-x // h]) <= K:
            print(h)
            exit()

    print(0)


if __name__ == '__main__':
    p_e()
