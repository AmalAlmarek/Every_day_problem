# define an array 
list_numbers = [2,8,0,6,5]
print(list_numbers)
# arrange it! HOW??
# Simply bubble the bigger numbers at the end and you will have the lowest at the begining 
# how to bubble them up ? CHECK next to you if bigger than her SWAP !
# the inner loop must skip the element where bubbled up 
#range(stop)
for i in range(len(list_numbers)-1):
    # range(start , stop)
    for j in range(len(list_numbers)-1-i):
        if list_numbers[j]>list_numbers[j+1]:
            list_numbers[j],list_numbers[j+1] = list_numbers[j+1],list_numbers[j]
print(list_numbers)

