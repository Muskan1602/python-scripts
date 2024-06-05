# TC is O(logn) -- soreted array

def binary_search(arr, x):
	i = 0
	j = len(arr) - 1
	mid = 0

	while i <= j:

		mid = (i + j) // 2

		# If x is greater, ignore left half
		if arr[mid] < x:
			i = mid + 1

		# If x is smaller, ignore right half
		elif arr[mid] > x:
			j = mid - 1

		# means x is present at mid
		else:
			return arr[mid]

	# If we reach here, then the element was not present
	return -1


# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 2
# Function call
result = binary_search(arr, x)
print("Searching element is:", str(result))


