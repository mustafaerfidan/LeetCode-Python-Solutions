def tekrar_ediyormu(nums):
    nums.sort()
    result=False
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]:
            result=True
            break
        
            
    return result


    