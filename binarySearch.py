count = 0
def binarySearch(data, k, first, last):
	global count
	split = partition(data, k, first, last)
	count = count + 1
	if k == data[split]:
		print 'Position '+str(split)
		print count
	if k < data[split]:
		binarySearch(data, k, first, split)
	if k > data[split]:
		binarySearch(data, k, split, last)


def partition(data, k, first, last):
	half = (first + last)/2
	print half
	if k == data[half]:
		mark = half
	if k < data[half]:
		mark = half - 1
	if k > data[half]:
		mark = half + 1
	return mark

data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
binarySearch(data, 17, 0, len(data) -1)
