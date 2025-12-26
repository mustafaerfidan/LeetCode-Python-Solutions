def coklu_anagram(strs):
    gruplar = {} # Boş bir sözlük (Kutularımız)
    
    for kelime in strs:
        # 1. ADIM: Kelimeyi sırala ve kilitli hale getir (tuple)
        # sorted("eat") -> ['a', 'e', 't'] verir.
        # tuple(['a', 'e', 't']) -> ('a', 'e', 't') olur.
        anahtar = tuple(sorted(kelime))
        
        # 2. ADIM: Bu anahtar (etiket) daha önce sözlükte var mı?
        if anahtar in gruplar:
            # Varsa, o kutunun listesine bu kelimeyi ekle
            gruplar[anahtar].append(kelime)
        else:
            # Yoksa, o anahtarla yeni bir liste başlat ve kelimeyi koy
            gruplar[anahtar] = [kelime]
            
    # 3. ADIM: Sadece grupları (sözlüğün değerlerini) döndür
    return list(gruplar.values())