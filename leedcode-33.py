def search(nums, target):
    sol = 0
    sag = len(nums) - 1
    
    while sol <= sag:
        # Ortayı bul
        orta = (sol + sag) // 2
        
        # Hedef bulundu mu?
        if nums[orta] == target:
            return orta
        
        # --- HANGİ TARAF DÜZGÜN? ---
        
        # 1. DURUM: SOL taraf sıralı mı?
        # (Sol baştaki sayı, ortadakinden küçükse sol taraf düzgündür)
        if nums[sol] <= nums[orta]:
            # Hedef bu sıralı sol bölgede mi?
            if nums[sol] <= target and target < nums[orta]:
                sag = orta - 1  # Evet burada, sağ tarafı at.
            else:
                sol = orta + 1  # Hayır burada değil, sağ tarafa bak.
                
        # 2. DURUM: SAĞ taraf sıralı
        # (Sol bozuksa, mecburen sağ taraf düzgündür)
        else:
            # Hedef bu sıralı sağ bölgede mi?
            if nums[orta] < target and target <= nums[sag]:
                sol = orta + 1  # Evet burada, sol tarafı at.
            else:
                sag = orta - 1  # Hayır burada değil, sol tarafa bak.
                
    return -1