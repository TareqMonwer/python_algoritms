def binSearch(collection, item):
    start = 0
    end = len(collection) - 1
    mid = (start + end)//2

    while item != collection[mid] and start <= end:
        if item > collection[mid]:
            start = mid + 1
        else:
            end = mid - 1
        mid = (start + end)//2

    if item == collection[mid]:
        print('item: {} index: {}'.format(item, mid))
    else:
        print('Item not found!')

binSearch([12,13,14,15], 14)
