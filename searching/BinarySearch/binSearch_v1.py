li = [1,2,3,5,6,7,8,9]
item = 4 #try by 3,5,7 and others
start = 0
last = len(li)-1
mid = (start + last)//2

while start <= last and li[mid] != item:
    if item < mid:
        last = mid - 1
    else:
        start = mid + 1

    mid = (start + last)//2

if li[mid] == item:
    print('item found at', mid)
else:
    print('item not found!')
