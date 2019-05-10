li = [5,6,2,1,29]
n = len(li)

for i in range(n):
	# accessing all indexes

	for j in range(n-i-1):
		# accessing 0 to n-1 indexes
		if li[j] > li[j+1]:
			# comparing between pairs
			li[j], li[j+1] = li[j+1], li[j]
print(li)
