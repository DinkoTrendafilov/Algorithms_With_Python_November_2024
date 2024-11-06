def drawing(n):
    if n == 0:
        return

    print("*" * n)
    drawing(n - 1)
    print("#" * n)


num = int(input())
drawing(num)
