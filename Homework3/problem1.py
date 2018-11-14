list_of_nums = list(map(int, input('Enter integers separated by spaces: ').split()))

def find_diff(newlist):
	minimum = maximum = newlist[0]
	for i in range(1, len(newlist)):
		if newlist[i] < minimum:
			minimum = newlist[i]
		elif newlist[i] > maximum:
			maximum = newlist[i]
	difference = maximum - minimum
	return difference

print(find_diff(list_of_nums))

