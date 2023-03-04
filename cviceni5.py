# sorted(iterable, key=key, reverse=reverse)
# Parameter	Description
# iterable	Required. The sequence to sort, list, dictionary, tuple etc.
# key	Optional. A Function to execute to decide the order. Default is None
# reverse	Optional. A Boolean. False will sort ascending, True will sort descending. Default is False
arr = [1,2,3,4,5]
arr1 = [5,1,4,2,8]
arr2 = [1,2,3,4,5]

if arr == arr2:
    print("stejne")
else: print("Nejsou stejne")
print(arr == sorted(arr))

#Bubblesort !!!!!!  zkusit sama napsat
arr =[5,1,4,2,8]
n= len(arr)
for i in range(n-1):
    print("0...",n-i-1)
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=  arr[j+1],arr[j]
            swapped=True
    if not swapped:
        break
        print(arr[j],arr[j+1])

#Insertion sort
arr=[85,12,59,45,72,51]

#ukladani sum hodnot
arr=[1,2,3,4]
n=len(arr)
soucet=0
sums=[]
for i in range(0,n):
    soucet+=i
    sums.append(soucet)
print(i, soucet)
print(sums)



