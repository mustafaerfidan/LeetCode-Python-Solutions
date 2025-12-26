def binary_search(nums,target):
    sol=0
    sag=len(nums)-1
    while sol <= sag :
        index=(sag+sol)//2
        if nums[index]==target:
            return index
        elif nums[index] < target:
            sol=index+1
        else:
            sag=index-1
    return -1


