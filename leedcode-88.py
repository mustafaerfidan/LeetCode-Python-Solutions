def merge(nums1,m,nums2,n):
    n1=m-1
    n2=n-1
    n_son=m+n-1
    
    while n1>=0 and n2>=0 :
        if nums1[n1]<nums2[n2]:
            nums1[n_son]=nums2[n2]
            n2-=1
        else:
            nums1[n_son]=nums1[n1]
            n1-=1
        n_son-=1
    
    while n2>=0:
        nums1[n_son]=nums2[n2]
        n2-=1
        n_son-=1    

    

