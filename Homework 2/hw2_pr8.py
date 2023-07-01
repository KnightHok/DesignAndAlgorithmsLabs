def Q_Eight(string):
    my_set = set([])
    max_size = 0
    for c in string:
        if c in my_set:
            my_set.clear()
        else:
            my_set.add(c)
            max_size = max(max_size, len(my_set))
    return max_size
            
        
if __name__ == "__main__":
    test_str = "pubwwkewsin"
    print(Q_Eight(test_str))
    