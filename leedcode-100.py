
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:




    def isSameTree(self,p,q):

        if p==None and q==None:
            return True
        elif p==None and q != None:
            return False
        elif p != None and q==None:
            return False
            



        left1=p.left
        right1=p.right
        val1=p.val

        left2=q.left
        right2=q.right
        val2=q.val

        
        
        
        if val1 != val2:
            return False
        
        
        self.isSameTree(left1,left2)
        self.isSameTree(right1,right2)

        if self.isSameTree(left1,left2)==True and self.isSameTree(right1,right2) == True :
            return True 
        else:
            return False



