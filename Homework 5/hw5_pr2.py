# Subproblem - The subproblem is to add all other indexes other than the current index
# After add to possible sums that can be achieved using a subset of nums

# Relation - each new sum is formed by either including the current number or excluding it
# (e.g. newDP.add(t + num) and newDP.add(t))

# Topological Order - the topological order is increasing for i in nums array

# Base - dp.add(0)

# Original - partition_iter(nums)

# Time - O(n * s)
def partition_iter(nums: [int]):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    dp = set()
    dp.add(0)
    
    target = total_sum // 2
    
    for num in nums:
        newDP = set()
        for t in dp:
            if ( t + num == target ):
                return True
            newDP.add(t + num)
            newDP.add(t)
        dp = newDP
    return True if target in dp else False

def partition_rec(nums: [int]):
    n = len(nums)
    totalSum = sum(nums)
    if totalSum % 2 != 0:
        return False
    def helper(idx: int, sum: int, arr:[int]) -> bool:
        if ( sum == 0 ):
            return False
        if ( idx == 0 ):
            return sum == nums[idx]
        return helper(idx-1, sum, nums) or helper(idx-1, sum - nums[idx], nums)
    
    return helper(n-1, totalSum, nums)
    

if __name__ == "__main__":
    nums = [1, 5, 11, 5, 1]
    print(partition_iter(nums))
    print(partition_rec(nums))

    