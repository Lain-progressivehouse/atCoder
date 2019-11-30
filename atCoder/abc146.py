def p_a():
    t = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    s = input()
    print(7 - t.index(s))


def p_b():
    t = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    n = int(input())
    s = input()
    for i in list(s):
        print(t[(t.index(i) + n) % len(t)], end="")
    print()


def p_c():
    a, b, x = map(int, input().split())
    i = min((x + a) // a, 100000000)
    ans = a * i + b * len(str(i))
    i -= (ans-x)//a+10
    for j in reversed(range(1, i+1)):
        ans = a * j + b * len(str(j))
        if ans < x:
            if ans < 1000000000:
                print(j)
            else:
                print(1000000000)
            exit()
    print(0)



def p_d():
    n = int(input())
    t = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        t[a - 1].append(b - 1)
        t[b - 1].append(a - 1)
    num = 0
    t_size = []
    for i in range(n):
        num = max(num, len(t[i]))
        t_size.append((len(t[i]), i))
    t_size.sort(reverse=True)
    # print(num)
    # print(t_size)
    # print(t)
    color = [-1] * n
    for size, i in t_size:
        if size == 1:
            continue
        li = []
        for j in t[i]:
            if color[j] != -1:
                li.append(color[j])
                continue
            for k in range(1, num + 1):
                if k not in li:
                    color[j] = k
                    li.append(k)
                    break
    print("\n".join(map(str, color)))


def p_e():
    pass


def p_f():
    pass


if __name__ == '__main__':
    p_c()
