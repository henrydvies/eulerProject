def multiplesBelow(n=1000):
    multiples = []
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)
    return sum(multiples)


print(multiplesBelow(1000))

# 233168