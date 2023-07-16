def max_value_in_knapsack_iter(max_size, values, sizes):
    n = len(values)

    Kn = {(-1, s): 0 for s in range(max_size+1)}
    Kn |= {(i, 0): 0 for i in range(n+1)}
    
    included = [[False] * (max_size + 1) for _ in range(n + 1)]

    for i in range(n):
        for s in range(max_size+1):
            if sizes[i] > s:
                Kn[i, s] = Kn[i-1, s]
            else:
                Kn[i, s] = max(values[i] + Kn[i-1, s - sizes[i]], Kn[i-1, s]) if s >= sizes[i] else Kn[i-1, s]
                if Kn[i, s] == values[i] + Kn[i-1, s - sizes[i]]:
                    included[i][s] = True
                
    max_profit = Kn[n-1, max_size]
    selected_items = []
    
    i = n
    j = max_size
    while i >= 0 and j >= 0:
        if included[i][j]:
            selected_items.append(sizes[i])
            j -= sizes[i]
        i -= 1
    return max_profit, selected_items
    
    
    
    

if __name__ == "__main__":
    
    print(max_value_in_knapsack_iter(max_size=6, values=[4, 2, 5, 1], sizes=[3, 4, 3, 1]))                
    values = [505, 352, 458, 220, 354, 414, 498, 545, 473, 543]
    sizes = [23, 26, 20, 18, 32, 27, 29, 26, 30, 27]
    
    print(max_value_in_knapsack_iter(max_size=67, values=values, sizes=sizes))
