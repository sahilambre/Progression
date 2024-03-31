def pattern11(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j % 2, end="")

        print('')

pattern11(5)