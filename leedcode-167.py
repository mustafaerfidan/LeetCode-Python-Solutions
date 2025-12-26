def sıralı_dizi(numbers,target):

    sol=0
    sağ=len(numbers)-1
    while sol<sağ:
        if numbers[sol]+numbers[sağ]==target:
            return [sol+1,sağ+1]
        elif numbers[sol]+numbers[sağ]<target:
            sol+=1
        else:
            sağ-=1
