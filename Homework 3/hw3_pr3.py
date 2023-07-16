def remove_overlapping_intervals(intervals, weights):
    # take each interval start time and finish time and weight and 
    # put it in a tuple with weight and index e.g (2, 4, 7, 0)
    combined = [(start, end, weights[i], i) for i, (start, end) in enumerate(intervals)]
    
    # sort the combined intervals based on finish time (in ascending order), then by
    # start time (in decending order)
    combined.sort(key=lambda x: (x[1], -x[0]))
    
    compatible_intervals = []
    
    for interval in combined:
        # if compatible_intervals is empty or the last tuple in compatible_intervals'
        # finish time is less than the start time
        if not(compatible_intervals) or interval[0] >= compatible_intervals[-1][1]:
            compatible_intervals.append(interval)
        
    # sort the compatible_intervals by thier weight
    sorted_indices = sorted([interval[3] for interval in compatible_intervals])
    
    removed_intervals = [intervals[i] for i in range(len(intervals)) if i not in sorted_indices]
    
    return removed_intervals
    
if __name__ == "__main__":
    intervals = [(1, 2), (2, 3), (3, 4), (1, 3)]
    weights = [2, 2, 2, 2]
    
    print(remove_overlapping_intervals(intervals, weights))