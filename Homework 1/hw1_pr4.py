def next_greater_element(nums1, nums2):
    map = {}
    stack = []
    for num in nums2:
        while not(len(stack) <= 0) and stack[-1] < num:
            map[stack.pop()] = num
        stack.append(num)
    # O(n)
    for i in range(len(nums1)):
        nums1[i] = map[nums1[i]] if nums1[i] in map.keys() else -1
    # O(m)
    return nums1
# Time Complexity: O(n+m)

if __name__ == "__main__":
    nums1 = [2,4]
    nums2 = [1,2,3,4]
    answer = next_greater_element(nums1, nums2)
    print(answer)