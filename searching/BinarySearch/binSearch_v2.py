arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 16]
item = 2
left = 0
right = len(arr) - 1

mid = (left + right)//2
print('Initial mid is: %d and item %d' %(mid, arr[mid]))
cycle = 1
while item != arr[mid] and left <= right:
    if item > arr[mid]:
        left = mid + 1 #which is currently item 4
    elif item < arr[mid]:
        right = mid - 1 #which is currently item 2

    mid = (left + right)//2
    print('%d cycles mid is: %d and item %d' %(cycle, mid, arr[mid]))
    cycle += 1

if item == arr[mid]:
    print('%d LOC in array is %d' %(item, mid+1))
    print('found in cycle number: %d' %cycle)
else:
    print('Item not found')


