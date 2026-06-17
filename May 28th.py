def print_stars(n):
    if n == 0:
        return

    print("*" * n)
    print_stars(n - 1)


print_stars(5)