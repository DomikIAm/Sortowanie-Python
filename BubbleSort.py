def bubbleSort(arr):
    n = len(arr)
 
    for i in range(n-1):
   
 

        for j in range(0, n-i-1):

            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
 
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
        

arr = [a, b, c, d, e, f]
 
bubbleSort(arr)
 
print ("Sorted array is:")
for i in range(len(arr)):
    print ("% d" % arr[i]),
