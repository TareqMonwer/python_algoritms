def bubble_sort(arr):
    """
    :param arr: List of numbers.
    :return : Sorted list of numbers.
    """

    for i in range(len(arr) - 1, 0, -1):
        # Looping through lest item to second 1st array item.
        # print("index i: " + str(i))
        for j in range(i):
            # Comparing the current index value with the rest.
            # print("index j: " + str(j))
            # print("j={}, j+1={}".format(arr[j], arr[j+1]))
            # Checking adjacent items.
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
        # print()
    return arr


if __name__ == "__main__":
    # bubble_sort([5, 8, 11, 3, 9, 2, 3, 1])
    print(bubble_sort([5, 8, 11, 3, 9, 2, 3, 1]))
