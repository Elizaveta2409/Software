def permute_iterative(nums):
    result = [[]]
    
    for num in nums:
        new_perms = []
        for perm in result:
            for i in range(len(perm) + 1):
                new_perm = perm[:i] + [num] + perm[i:]
                new_perms.append(new_perm)
        result = new_perms
    
    return result