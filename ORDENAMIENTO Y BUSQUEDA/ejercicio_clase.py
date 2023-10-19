
#BUBBLE SORT 
arr=[3,70,2,53,6,48,95,31,1]
finish=False

while finish==False:
    finish=True
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            assistant=arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=assistant
            finish=False

print(arr)

#SELECTION SORT 
    #De menor a mayor
arr=[3,70,2,53,6,48,95,31,1]

for i in range(len(arr)):
    minimum=i
    for j in range(i+1, len(arr)):
        if arr[minimum]>arr[j]:
            minimum=j

    assistant=arr[i]
    arr[i]=arr[minimum]
    arr[minimum]=assistant

print(arr)

    #De mayor a menor
arr=[3,70,2,53,6,48,95,31,1]

for i in range(len(arr)):
    maximum=i
    for j in range(i+1, len(arr)):
        if arr[maximum]<arr[j]:
            maximum=j
    assistant=arr[maximum]
    arr[maximum]=arr[i]
    arr[i]=assistant

print(arr)

#INSERTION SORT 
arr=[3,70,2,53,6,48,95,31,1]

for i in range(1,len(arr)):
    key=arr[i]
    
    j=i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j=j-1
        arr[j+1]=key

print(arr)


#MERGE SORT
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Dividir la lista en dos mitades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Ordenar recursivamente cada mitad
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Combinar las mitades ordenadas
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Ejemplo de uso
arr =[3,70,2,53,6,48,95,31,1]
sorted_arr = merge_sort(arr)
print(sorted_arr)
