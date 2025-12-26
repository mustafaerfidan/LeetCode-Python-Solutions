def en_kucuk(nums):
    sol=0
    sağ=len(nums)-1
    while sol<sağ:
        orta=(sol+sağ)//2
        if nums[orta]>nums[sağ]:
            sol=orta+1
        else:
            if nums[orta]<nums[orta-1]:
                return nums[orta]
            sağ=orta
    return nums[sol]
            