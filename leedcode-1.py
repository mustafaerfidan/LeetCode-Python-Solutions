def two_sum(nums, target):
    onceki = {}
    for i, sayi in enumerate(nums):
        gerekli = target - sayi
        if gerekli in onceki:
            return [onceki[gerekli], i]
        onceki[sayi] = i
