# Move all negative numbers to beginning and positive to end with constant extra space
# Difficulty Level : Easy
# An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.

# Examples : 

# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5
# Note: Order of elements is not important here.


def rearrange(arr, n):
    j = 0
    for i in range(0, n):
        if arr[i] < 0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j += 1
    print(arr)


def rearrange2(arr, n):
    left, right = 0, n-1
    while left<=right:
        if arr[left] < 0 and arr[right] < 0:
            left += 1
        elif arr[left] > 0 and arr[right] < 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[left] > 0 and arr[right] > 0:
            right -= 1
        else:
            left+=1
            right-=1
    print(arr)

arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
n = len(arr)
rearrange2(arr, n)