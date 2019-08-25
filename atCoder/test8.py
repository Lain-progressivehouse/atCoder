def problem_a():
    n, k = map(int, input().split())
    s = input()
    print(s[:k - 1] + s[k - 1].lower() + s[k:])


def problem_b():
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
