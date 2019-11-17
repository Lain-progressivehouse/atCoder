def warshall_floyd(cost, num_v):
    """
    ワーシャルフロイド法
    :param cost: 隣接行列
    :param num_v: 頂点数
    :return: 各頂点からの最短距離
    """
    for k in range(num_v):
        for i in range(num_v):
            for j in range(num_v):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    return cost


import itertools


def abc073_d():
    n, m, r = map(int, input().split())
    *r, = map(int, input().split())
    inf = float("inf")
    cost = [[inf] * n for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        cost[a - 1][b - 1] = c
        cost[b - 1][a - 1] = c
    for i in range(n):
        cost[i][i] = 0

    cost = warshall_floyd(cost, n)
    ans = inf
    for permutation in itertools.permutations(r):
        c = 0
        b = permutation[0]
        for i in permutation[1:]:
            c += cost[b - 1][i - 1]
            b = i
        ans = min(ans, c)
    print(ans)


if __name__ == '__main__':
    abc073_d()
