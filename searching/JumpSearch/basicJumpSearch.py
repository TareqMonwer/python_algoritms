import math

arr = [12, 133, 244, 246, 455, 567, 677, 788]
val = 455

start = 0
pos = 0
last = len(arr)
block = math.sqrt(last)

while val != arr[int(pos)]:
    if val > arr[int(pos)]:
        pos -= block
        while val != arr[int(pos)]:
            pos += 1

        
    elif val < arr[int(pos)]:
        pos += block

if val == arr[int(pos)]:
    print('%d found in index: %d' %(arr[int(pos)], pos))
else:
    print(-1)
