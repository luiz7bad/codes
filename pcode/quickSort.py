def quickSort(data, first, last):
	if first < last:
		split = partition(data, first, last)
		quickSort(data, split + 1, last)
		quickSort(data, first, split - 1)
def partition(data, first, last):
	pivot = first
	left = first + 1
	right = last
	done = False
	while not done:
		while left <= right and data[left] <= data[pivot]:
			left = left + 1
		while right >= left and data[right] >= data[pivot]:
			right = right - 1
		if left > right:
			done = True
		else:
			temp = data[left]
			data[left] = data[right]
			data[right] = temp
	temp = data[first]
	data[first] = data[right]
	data[right] = temp

	return right

data = [15,2,3,14,16,20,9,98,28,5,1,20,8,6,78,10]
quickSort(data, 0, len(data)-1)
print data
