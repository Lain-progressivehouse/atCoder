def main():
    n = int(input())
    a, b, c = list(map(int, input().split()))

    n_a = [i * a for i in range(1, n // a + 1)]
    n_b = [i * b for i in range(1, n // b + 1)]
    n_c = [i * c for i in range(1, n // c + 1)]

    print(len(set(n_a + n_b + n_c)))


def fizzbuzz():
    for i in range(100):
        print(i % 3 // 2 * "Fizz" + i % 5 // 4 * "Buzz" or i + 1)


if __name__ == '__main__':
    main()
