def maximum_task(arr: list, t: int):
    sorted_arr = sorted(arr)


    total_time = 0
    numOfTask = 0

    for task in sorted_arr:
        if ( total_time + task <= t ):
            total_time += task
            numOfTask += 1
        
    return numOfTask

if __name__ == "__main__":
    input_arr =  [23, 17, 9, 4, 28, 13, 6, 19, 26, 11, 3, 15, 7, 25, 2, 20, 10, 14, 8, 16, 18, 1, 29, 12, 22, 27, 5, 30, 21, 24]
    print(maximum_task(input_arr, 99))
