def func(arr,pages):
    std = 1
    pagesStudent = 0

    for i in range(len(arr)):
        if pagesStudent + arr[i] <= pages:
            pagesStudent += arr[i]
        else:
            std += 1
            pagesStudent = arr[i]
    return std


def painters(arr,k):
    low = max(arr)
    high = sum(arr)

    while low<=high:
        mid = (low + high)//2
        no_of_stds = func(arr,mid)
        if no_of_stds > k:
            low = mid + 1
        else:
            high = mid - 1

    return low


arr = [10,20,30,40]
k = 2
print(painters(arr,k))