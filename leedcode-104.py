def maxDepth(root):
    if root==None:
        return 0
    
    sol_yükseklik=maxDepth(root.left)
    sag_yükseklik=maxDepth(root.right)

    if sol_yükseklik<sag_yükseklik:
        return sag_yükseklik+1
    else:
        return sol_yükseklik+1
    

   
        

