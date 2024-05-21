
def fibSeq(n=4000000):
    total = 0
    fib = [1,2]
    while fib[-1] <n:
        nextFib = fib[-1] + fib[-2]
        fib.append(nextFib)
        if nextFib % 2 == 0:
            total += nextFib
    return total


print(fibSeq())

# 4613732