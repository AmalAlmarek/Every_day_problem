# insertion sort 
array = [2,6,5,1,3,4]
def insertion_sort(arr):
    for i in range(1,len(array)):
        j = i
        while array[j-1] > array[j] and j > 0 :
            array[j-1], array[j] = array[j],array[j-1]
            j-=1

    print(array)

# calling function 
insertion_sort(array)

    
