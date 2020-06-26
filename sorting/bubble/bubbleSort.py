<<<<<<< HEAD:sorting/bubble/bubbleSort.py
def bubble_it(arr):
	''' Sort an array/list by smallest number '''

	for i in range(len(arr)-1, 0, -1):
		''' accessing 2nd item to last item '''
		for j in range(i):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

# apply
mylist = [7,5,1,4,3]
bubble_it(mylist)
print(mylist)



''' Test This Code For Better Understanding '''
arr = [10,9,7,8,4,6]
for check_item in range(len(arr)-1, 0, -1):
	# here arr[check_item] will be 9, 7,...

	for j in range(check_item):
		if arr[j] > arr[j+1]:
			arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)
=======
def bubble_it(arr):
	''' Sort an array/list by small '''

	for i in range(len(arr)-1, 0, -1):
		''' accessing 2nd item to last item '''

		for j in range(i):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

# apply
mylist = [7,5,1,4,3]
bubble_it(mylist)
print(mylist)



''' Test This Code For Better Understanding '''
arr = [10,9,7,8,4,6]
for check_item in range(len(arr)-1, 0, -1):
	# here arr[check_item] will be 9, 7,...

	for j in range(check_item):
		if arr[j] > arr[j+1]:
			arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)
>>>>>>> 1312bd05e7409623b975087289c2a084808808bd:sorting/bubble/bubbleSort.py
