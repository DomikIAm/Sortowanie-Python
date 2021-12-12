while True:
    try:
        a = int(input("Wpisz liczbe nr 1: "))
        b = int(input("Wpisz liczbe nr 2: "))
        c = int(input("Wpisz liczbe nr 3: "))
        d = int(input("Wpisz liczbe nr 4: "))
        e = int(input("Wpisz liczbe nr 5: "))
        f = int(input("Wpisz liczbe nr 6: "))
        break
    except ValueError:
        print("Wpisales zla liczbe! Musisz wpisac liczbe calkowita by program zadzialal!")
        

def partition(arr, low, high):
    i = (low-1)         
    pivot = arr[high]     
 
    for j in range(low, high):
 

        if arr[j] <= pivot:
 

            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 
 
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
 

        pi = partition(arr, low, high)
 
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
 
arr = [a, b, c, d, e, f]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])
