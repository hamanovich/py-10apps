def factorial(n):
    if n == 1:
        return 1

    return factorial(n-1) * n


print('5!={:,}, 3!={:,}, 10!={:,}'.format(
    factorial(5),
    factorial(3),
    factorial(10)
))


def fibonacci(limit):
    nums = []

    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current
        nums.append(current)

    return nums


for n in fibonacci(100):
    print(n, end=', ')
print()


def fibonacci_co():
    current = 0
    next = 1

    while True:
        current, next = next, next + current
        yield current


for n in fibonacci_co():
    if n > 10000:
        break
    print(n, end=', ')
