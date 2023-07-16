def good_sequences(n: int):
    a_count = 1
    b_count = 1
    
    for i in range(2, n + 1):
        new_a_count = a_count + b_count
        new_b_count = a_count
        
        a_count = new_a_count
        b_count = new_b_count
    return a_count + b_count
    

if __name__ == "__main__":
    print(good_sequences(4))
    
# This solution works because of the variables that calculate counts baes on the previous 
# length. a_count + b_count is assigned to new_a_count because we know we can append a 
# "a" or "b" to the end of a sequence that has "a" as the last character.
# Only a_count is assigned to new_b_count because we can only append "a" to a sequence
# that ends with "b"