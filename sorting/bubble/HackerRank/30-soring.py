n = int(input().strip())
a = list(map(int, input().strip().split(' ')))


def asc_bubble(a):
    data = {"swap": 0, "first": None, "last": None}

    n = len(a)

    for i in range(0, n):
        for j in range(0, n-i-1):
            if a[j] > a[j + 1]:
                data["swap"] += 1
                a[j], a[j + 1] = a[j + 1], a[j]
    data["first"], data["last"] = a[0], a[n - 1]
    data["a"] = a
    return data

result = asc_bubble(a)
print(f"Aaay is sorted in {result['swap']} swaps.")
print(f"First Element: {result['first']}")
print(f"Last Element: {result['last']}")
