def time_for_tickets(tickets, k):
    time = 0
    idx = 0
    while tickets[k] != 0:
        if tickets[idx] > 0:
            tickets[idx] = tickets[idx] - 1
            time += 1
        idx += 1
        if idx == len(tickets):
            idx = 0
    return time

if __name__ == "__main__":
    my_list1 = [2,3,2]
    k1 = 2
    print(time_for_tickets(my_list1, k1))
    
    my_list2 = [5,1,1,1]
    k2 = 0
    print(time_for_tickets(my_list2, k2))
        