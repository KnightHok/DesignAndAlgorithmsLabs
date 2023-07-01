def intersect(arr1, arr2):
    map = {}
    new_arr = []
    for val in arr1:
        if not(val in map):
            map[val] = 0
        map[val] = map[val] + 1
    for val in arr2:
        if ( val in map and map[val] > 0 ):
            new_arr.append(val)
            map[val] = map[val] - 1
    return(new_arr)

def intersect2(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    
    i, j = 0 , 0
    
    new_arr = []
    
    while ( i < len(arr1) and j < len(arr2) ): # goes until the largest len()
        if ( arr1[i] < arr2[j] ):
            i += 1
        elif ( arr1[i] > arr2[j] ):
            j += 1
        else:
            new_arr.append(arr1[i])
            i += 1
            j += 1
    return new_arr

if __name__ == "__main__":
    arr1 = [3,7,2,6,6,9,5,1,1]
    arr2 = [9,4,9,8,6,1,0,6,6]
    
    print(intersect(arr1, arr2))