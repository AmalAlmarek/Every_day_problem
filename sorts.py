# selection sort 
list = [2,6,5,1,3,4]

def selection_sort(arr): 
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]
    print('selection sort: ',arr)
# bubble sort
def bubble_sort(arr): 
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print('Bubble sort: ',arr)
# insertion sort 
def insertion_sort(arr): 
    for i in range(len(arr)):
        j = i
        while arr[j-1] > arr[j] and j > 0:
            arr[j-1],arr[j]= arr[j],arr[j]
    print('insertion sort: ',arr)
#merge sort 
def merge_sort(arr):
    if len(arr) > 1 :
        # define subs
        left_sub = arr[:len(arr)//2]
        right_sub = arr[len(arr)//2:]
        
        # divide 
        merge_sort(left_sub)
        merge_sort(right_sub)

        i = 0 # index left sub array
        j = 0 # index right sub array
        k = 0 # index of merged arrays
        
        # merge 
        while i < len(left_sub) and j < len(right_sub):
            if left_sub[i] < right_sub[j]:
                arr[k] = left_sub[i]
                i+=1
            else:
                arr[k] = right_sub[j]
                j+=1
            k+=1
        while i < len(left_sub):
            arr[k] = left_sub[i]
            i+=1
            k+=1
        while j < len(right_sub):
            arr[k] = right_sub[j]
            j+=1
            k+=1
        print('merge sort: ',arr)
    
        



selection_sort(list)
bubble_sort(list)
insertion_sort(list)
merge_sort(list)
    
