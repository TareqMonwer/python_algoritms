arr = [1,3,4,5,6,7]
item = 8
s = 0
e = len(arr) - 1

while s < e:
    if item == arr[s]:
        print('found in index {}'.format(s))
    s += 1

if item != arr[s] - 1:
    print('Not Found!')
    
    
