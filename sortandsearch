def BinarySearch(n,target,low,high,count):
    mid = (low+high)//2
    count += 1
    if n[mid] == target : return [mid,count]
    if low>high : return [-1,count]
    if n[mid]>target:
        return BinarySearch(n,target,low,mid-1,count)
    elif n[mid]<target:
        return BinarySearch(n,target,mid+1,high,count)
    
def insertionSort(n):
    for i in range(len(n)):
        for j in range(i):
            if n[j]>n[i]:
                n.insert(j,n[i])
                del n[i+1]
                break       
    return n

def bubbleSort(n):
    hasswap = True
    while hasswap:
        hasswap = False
        for i in range(len(n)-1):
            if n[i]>n[i+1]:
                n[i],n[i+1] = n[i+1],n[i]
                hasswap = True
    return n

def QuickSort(n):
    if len(n) == 0 or len(n)== 1:return n
    pivot = n[0]
    small = []
    large = []
    for element in n[1:]:
        if element < pivot:
            small.append(element)
        else:
            large.append(element)
    return QuickSort(small) + [pivot] + QuickSort(large)
