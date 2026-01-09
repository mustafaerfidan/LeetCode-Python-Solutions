def searchBST(self,root,val):
    if root is None :
        return  None
    
    elif root.val<val:
        return self.searchBST(root.right,val)
    elif root.val>val:
        return self.searchBST(root.left,val)
    else:
        return root

    
        
        


