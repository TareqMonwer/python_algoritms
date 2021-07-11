
def merge_sorted_lists(list_one, list_two):
    sorted_list = []
    i = j = 0
    while i < len(list_one) and j < len(list_two):
        if list_one[i] <= list_two[j]:
            sorted_list.append(list_one[i])
            i += 1
        else:
            sorted_list.append(list_two[j])
            j += 1

    while i < len(list_one):
        sorted_list.append(list_one[i])
        i += 1
    while j < len(list_two):
        sorted_list.append(list_two[j])
        j += 1
    return sorted_list


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge_sorted_lists(left_sorted, right_sorted)

if __name__ == "__main__":
    print(merge_sort([20, 31, 11, 2, 45, 44, 100]))
