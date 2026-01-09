def hasPathSum(root,targetSum):
    if root == None:
        return False

    targetSum= targetSum - root.val
    if targetSum == 0 and root.right == None and root.left == None :
        return True 
    else:
        left = hasPathSum(root.left,targetSum)
        right = hasPathSum(root.right,targetSum)

        if left == True or right == True :
            return True
        else:
            return False

