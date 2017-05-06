# Radix sort, personal favorite, very simple, intutive and efficient however requires
# large auxillary space, making it impractical in certian situations


# basic radix sort function, works for list of integer strings of equal length
def radix_sort_integer(list):
    #check if all items are of equal length
    for item in list:
        if len(item) != len(list[0]):
            print("Not all items in list of equal length")
            return False

    for radix in range(len(list[0])-1,-1,-1):
        radixBucket = [[],[],[],[],[],[],[],[],[],[]]
        for item in range(len(list)):
            radixBucket[int(list[item][radix])].append(list[item])
        list = []
        for set in range(len(radixBucket)):
            list.extend(radixBucket[set])
    return list

print(radix_sort_integer(["123","132","721","121","912","012"]))
