# n = 5
# first = 0
# second = 1

# for i in range(2, n + 1):
#     nth = first + second
#     first = second
#     second = nth
#     print(second)


def fibonacci(n):
    print("Trying to find fibonacci for", n)
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)


# def test_fibonacci():
#     assert fibonacci(1) == 1
#     assert fibonacci(2) == 1
#     assert fibonacci(5) == 5
#     assert fibonacci(6) == 8


# Test with enumerate function.
def test_fibonacci():
    fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for n, f in enumerate(fib):
        assert fibonacci(n + 1) == f 


if __name__ == "__main__":
    print("5th fibonacci number is", fibonacci(5))