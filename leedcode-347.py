def topKFrequent(nums, k):
    # 1. ADIM: Oyları Sayma (Sözlük Doldurma)
    # ---------------------------------------
    sozluk = {}  # Boş bir not defteri
    
    for sayi in nums:
        if sayi in sozluk:
            sozluk[sayi] += 1  # Varsa bir artır
        else:
            sozluk[sayi] = 1   # Yoksa 1 yazıp başlat

    # Şu an elimizde şöyle bir şey var: {1: 3, 2: 2, 3: 1}
    
    # 2. ADIM: En çok oy alan 'k' kişiyi bulma
    # ---------------------------------------
    sonuc = [] # Kazananları buraya atacağız
    
    # k kere döneceğiz (mesela 2 kazanan isteniyorsa 2 tur)
    for i in range(k):
        en_yuksek_adet = -1
        kazanan_sayi = None
        
        # Sözlüğü baştan sona gez, o anki en büyüğü bul
        for sayi in sozluk:
            adet = sozluk[sayi]
            
            # Eğer bu sayının oyu, şu ana kadar gördüğümden fazlaysa
            if adet > en_yuksek_adet:
                en_yuksek_adet = adet
                kazanan_sayi = sayi
        
        # En büyüğü bulduk! Listemize ekleyelim.
        sonuc.append(kazanan_sayi)
        
        # Bu sayıyı sözlükten silmeliyiz ki bir sonraki turda tekrar seçilmesin!
        del sozluk[kazanan_sayi]
        
    return sonuc