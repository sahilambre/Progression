def pattern7(n):
    for i in range(1, n + 1):
        print( " " * (n - i) + (2 * i - 1) * "*" + " " * (n - i) )

pattern7(5)