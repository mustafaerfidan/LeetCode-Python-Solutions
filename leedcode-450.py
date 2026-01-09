def deleteNode(root,key):
    if root==None:
        return None


    if root.val<key:
        root.right=deleteNode(root.right,key)
    elif root.val>key:
        root.left=deleteNode(root.left,key)
    else:
        if root.left==None and root.right==None:
            root=None
            return root
        elif root.left==None:
            temp=root.right
            root=None
            return temp
        elif root.right==None:
            temp=root.left
            root=None
            return temp
        else:
            min=root.right
            while min.left!=None:
                min=min.left
            
            root.val=min.val

            root.right = deleteNode(root.right,min.val)
    return root
            



