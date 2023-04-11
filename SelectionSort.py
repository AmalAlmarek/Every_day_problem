# sorting problems 
# selection sort 

# define an array 
numbers = [2,5,1,7,9]
# SET the minmum index to the first element in the array
# BECAUSE it is the first thing you know it is the minmum 
# CHECK all adjacent are they less than u? , 
# if it is the case REMEMBER the index and keep looking 
# SWAP after each coulmn vector
for i in range(len(numbers)):
    # SET 
    idx_min = i
    for j in range(i+1 ,len(numbers)):
        # CHECK
        if(numbers[j] < numbers[idx_min]):
            # REMEMBER 
            idx_min = j
    # SWAP
    numbers[i],numbers[idx_min] = numbers[idx_min],numbers[i]
# REPEAT , the process for each element in the array but with i+1 


print(numbers)


