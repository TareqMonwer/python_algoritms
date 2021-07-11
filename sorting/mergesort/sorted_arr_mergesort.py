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


if __name__ == "__main__":
    arr1 = [10, 15, 20]
    arr2 = [12, 18, 22]
    print(merge_sorted_lists(arr1, arr2))
