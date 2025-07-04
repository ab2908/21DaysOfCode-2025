def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr

inp = input("Enter integers separated by spaces: ")
arr = list(map(int, inp.strip().split()))

sortedArr = bubbleSort(arr)

print("Sorted array in ascending order:", sortedArr)
