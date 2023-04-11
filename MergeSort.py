''' Merge Sort
 divide and conquer algorithm 
 define an array 
 define left subarray and right subarray 
 divide the array each time using recursion 
 Check first , merge second 
 handle the cases where nothing need to be checked '''

# defining an array to be sorted 
list = [2,6,5,1,7,4,3]
# function to sort in ascending order 
def merge_sort(list):
    # Condition length greater than 1 , if it less then it is sorted 
    if len(list) > 1 :
        left_sub  = list[:len(list)//2] # [0,length -1) , [2,6,5]
        right_sub = list[len(list)//2:] # [length//2 , ) , [1,7,4,3]
        # recursion (division part)
        merge_sort(left_sub)
        merge_sort(right_sub)
        # merge (by comparing the left most element of the two sub arrays)
        i = 0 # left most array index
        j = 0 # right most array index 
        k = 0 # merged array index
        while i < len(left_sub) and j < len(right_sub):
            if left_sub[i] < right_sub[j]:
                list[k] = left_sub[i]
                i+=1
            else :
                # when they are equal or the right sub is less 
                list[k] = right_sub[j]
                j+=1
            k+=1
        while i < len(left_sub):
            list[k] = left_sub[i]
            i+=1
            k+=1
        while j < len(right_sub):
            list[k] = right_sub[j]
            j+=1
            k+=1

# before sorting 
print(list)   
# merge     
merge_sort(list)
# after sorting 
print(list)        

