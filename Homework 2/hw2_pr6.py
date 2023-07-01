def max_k(arr):
    start = sorted([tup[0] for tup in arr])
    end = sorted([tup[1] for tup in arr])
    
    currEnd, currStart = 0, 0
    
    count, max_count = 0, 0
    
    while ( currStart < len(arr) ):
        if ( start[currStart] < end[currEnd] ):
            currStart += 1
            count +=1
        else:
            currEnd += 1
            count -= 1
        max_count = max(max_count,  count)
        
        
    return max_count
    
    
if __name__ == "__main__":
    meetings = [(-0.3, 2.7), (-1, 0.5), (2.5, 3.3), (-0.7, 2.3), (0.5, 1.7)]
    
    answer = max_k(meetings)
    print(answer)
    
# B) No this can not be solved in O(n). This is because to sort the start and end
# arrays a sorting algorithm must be used. Any that fastest sorting algorithms
# that can work with this problem have a time complexity of 0(n log(n))