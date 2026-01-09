# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root):
        if root == None:
            return True
        # Kökü ikiye bölüp yardımcıya gönderiyoruz (Sol parça, Sağ parça)
        return self.ayna_mi(root.left, root.right)

    def ayna_mi(self, t1, t2):
        # 1. İkisi de yoksa simetriktir (True)
        if t1 == None and t2 == None:
            return True
        
        # 2. Biri var biri yoksa simetrik değildir (False)
        if t1 == None or t2 == None:
            return False
            
        # 3. Değerler farklıysa simetrik değildir (False)
        if t1.val != t2.val:
            return False
            
        # 4. ÇAPRAZ KONTROL (İşte sihir burada!)
        # t1'in SOLU ile t2'nin SAĞI (Dışlar)
        dis_taraf = self.ayna_mi(t1.left, t2.right)
        
        # t1'in SAĞI ile t2'nin SOLU (İçler)
        ic_taraf = self.ayna_mi(t1.right, t2.left)
        
        return dis_taraf and ic_taraf