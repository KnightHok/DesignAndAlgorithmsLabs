def max_value_in_knapsack_rec(max_size, values, sizes):
    n = len(values)

    memo = {(-1, s): 0 for s in range(max_size+1)}
    memo |= {(i, 0): 0 for i in range(n)}

    def Kn(i, s):
        if (i, s) not in memo:
            memo[i, s] = max(values[i] + Kn(i-1, s - sizes[i]),
                             Kn(i-1, s)) if s >= sizes[i] else Kn(i-1, s)
        return memo[i, s]

    return Kn(n-1, max_size)


def max_value_in_knapsack_iter(max_size, values, sizes):
    n = len(values)

    Kn = {(-1, s): 0 for s in range(max_size+1)}
    Kn |= {(i, 0): 0 for i in range(n+1)}

    for i in range(n):
        for s in range(max_size+1):
            Kn[i, s] = max(values[i] + Kn[i-1, s - sizes[i]],
                           Kn[i-1, s]) if s >= sizes[i] else Kn[i-1, s]
    return Kn[n-1, max_size]


print(max_value_in_knapsack_rec(max_size=6,
      values=[4, 2, 5, 1], sizes=[3, 4, 3, 1]))
print(max_value_in_knapsack_iter(max_size=6,
      values=[4, 2, 5, 1], sizes=[3, 4, 3, 1]))

values = [505, 352, 458, 220, 354, 414, 498, 545, 473, 543]
sizes = [23, 26, 20, 18, 32, 27, 29, 26, 30, 27]

print(max_value_in_knapsack_rec(max_size=67, values=values, sizes=sizes))
print(max_value_in_knapsack_iter(max_size=67, values=values, sizes=sizes))
