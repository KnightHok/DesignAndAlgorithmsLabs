def has_sequence(str1: list, str2: list):
    ptr1 = 0
    ptr2 = 0
    while ( ptr1 != len(str1) and ptr2 != len(str2) ):
        if ( str1[ptr1] == str2[ptr2] ):
            ptr1 += 1
            ptr2 += 1
        else:
            ptr1 += 1
    return ptr2 == len(str2)
    
    


if __name__ == "__main__":
    str1 = [1, 12, 4, 8, 10, 6]
    str2 = [12, 10, 6]
    
    str3 = [-2, 0, 4, 0, 2, 7]
    str4 = [0, 2, 4]
    
    print(has_sequence(str1, str2))
    print(has_sequence(str3, str4))
    