<<<<<<< HEAD
arr = [8, 3, 11, 4, 1]

for i in range(len(arr) - 1):
    min_index = i

    for j in range(i+1, len(arr)):
        if arr[j] < arr[i]:
            min_index = j

    if min_index != i:
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)

=======
arr = [8, 3, 11, 4, 1]

for i in range(len(arr) - 1):
    min_index = i

    for j in range(i+1, len(arr)):
        if arr[j] < arr[i]:
            min_index = j

    if min_index != i:
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)

>>>>>>> 1312bd05e7409623b975087289c2a084808808bd
