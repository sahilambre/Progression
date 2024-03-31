def pattern9(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1) + " " * (n -i))
    for j in range(n, 0, -1):
        print(" " * (n - j) + "*" * (2 * j - 1) + " " * (n - j))


pattern9(5)