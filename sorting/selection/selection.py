def selection_sort(arr):
	print()
	print('{} <= main array'.format(arr))
	print()

	# main part
	for i in range(len(arr)):
		min_index = i

		for j in range(i+1, len(arr)):
			if arr[min_index] > arr[j]:
				min_index = j
				arr[i], arr[min_index] = arr[min_index], arr[i]
		print(array)

array = [6,4,2,4,1]
selection_sort(array)
