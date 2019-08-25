def p_a():
    S = int(input())
    max_v = 10 ** 9

    if S > max_v:
        x2 = (S + max_v - 1) // max_v
        x3 = max_v * x2 - S
        print("0 0 " + str(x2) + " 1 " + str(x3) + " " + str(max_v))
    else:
        print("0 0 1 0 0 " + str(S))


def p_b():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    hoge = [[] for _ in range(200001)]

    for i in range(N):
        hoge[A[i]].append(i)
    NEXT = [-1] * N
    for i in hoge:
        for j in range(-len(i), 0):
            NEXT[i[j]] = i[j + 1]

    i = 1
    p = 0
    while i < K:
        # print(i,p)
        if NEXT[p] <= p:
            i += 1
        if NEXT[p] == N - 1:
            i += 1
        p = (NEXT[p] + 1) % N
        if p == 0:
            i = ((K - 1) // (i - 1)) * (i - 1) + 1
    while p < N:
        if NEXT[p] <= p:
            print(A[p], end=" ")
            p += 1
        else:
            p = NEXT[p] + 1
    print()


if __name__ == '__main__':
    p_b()
