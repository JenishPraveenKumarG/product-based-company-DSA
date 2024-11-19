def single_element(arr):
    low = 1
    high = len(arr)-2

    if arr[low] != arr[low-1]:
        return arr[low-1]

    if arr[high]!=arr[high+1]:
        return arr[high]
    
    while low <= high:
        mid = (low+high)//2

        if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid-1]:
            return arr[mid]
        elif mid %2 == 1 and arr[mid] == arr[mid-1] or mid%2 == 0 and arr[mid] == arr[mid+1]:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [1,1,2,2,3,3,4,5,5,6,6]
print(single_element(arr))