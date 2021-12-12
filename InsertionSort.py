def insertionSort(arr):
    
    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


        
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
    
    
arr = [a,b,c,d,e,f]
print("Twoja lista do posortowania: ",arr)

insertionSort(arr)
print("Lista posortowana:")
for i in range(len(arr)):
    print("%d" % arr[i])