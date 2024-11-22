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
            



def book_allocation(arr,students):
    n = len(arr)
    maxi = max(arr)
    sum_ = sum(arr)
    for i in range(maxi,sum_ + 1):
        cnt_std = func(arr,i)
        if cnt_std == students:
            return i




arr = [25,46,28,49,24]
students = 4
print(book_allocation(arr,students))

# TC - O(sum - max(arr)) + O(n)
# SC - O(1)


# binary search

def book_allocation(arr,students):
    low = max(arr)
    high = sum(arr)

    while low<=high:
        mid = (low + high)//2
        no_of_stds = func(arr,mid)
        if no_of_stds > students:
            low = mid + 1
        else:
            high = mid - 1

    return low


arr = [25,46,28,49,24]
students = 4
print(book_allocation(arr,students))

# TC - O(log2(sum - max + 1))
# Sc - O(1)