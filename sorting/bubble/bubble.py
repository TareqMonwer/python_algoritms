def bubble_sort(L):
    """Sorts (small to large) an array by L 
    using bubble sort algorithm.

    Args:
        L ([array]): [sorted or unsorted array]
    """

    n = len(L)

    for i in range(0, n):
        for j in range(0, n-i-1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]


if __name__ == "__main__":
    L = [8, 2, 33, 4, 1]
    print("Before ordering: ", L)
    bubble_sort(L)
    print("After ordering: ", L)
