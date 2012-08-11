def insertion_sort(list):
	for key in range(1,len(list)):
		value = list[key]
		i = key - 1
		while i>=0:
			if value < list[i]:
				list[i+1] = list[i]
				list[i] = value
				i = i - 1
			else:
				break

a = [4,2,1,5,3]
insertion_sort(a)
print a raw_input
