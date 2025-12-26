def invertTree(self,root):
    if root == None:
        return root
    
    geçici=None
    geçici=root.left
    root.left=root.right
    root.right=geçici
    self.invertTree(root.left)
    self.invertTree(root.right)
    
    
    return root



    