def qingwa(n):
    if n == 1:
        return 1
    else:
        return 2* qingwa(n-1)
print(qingwa(10))

