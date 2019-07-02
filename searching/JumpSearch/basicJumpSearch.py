arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
val = 55

block = 4
start = 0
pos = 0
last = len(arr) - 1

while val != arr[pos]:
    if val > arr[pos]:
        pos -= block
        while val != arr[pos]:
            pos += 1

        
    elif val < arr[pos]:
        pos += block

if val == arr[pos]:
    print('%d found in index: %d' %(arr[pos], pos))
else:
    print(-1)
