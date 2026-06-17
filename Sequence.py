def triangle(n):
    if n == 0:
        return 0
    return 2 + triangle(n-1)

print(triangle(2))