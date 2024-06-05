# TC = O(n) unsorted array

def linearsearch(arr, searching_element, n):
    for i in range(n):
        print(arr[i])
        if arr[i] == searching_element:
            return arr[i]
    return -1

arr = [3,5,1,4,7,8]
n = len(arr)
searching_element = 7
result = linearsearch(arr,searching_element, n)
print("seraching element is :", result)
