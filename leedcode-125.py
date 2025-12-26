def tersten_oku(s):
    s=s.lower()
    yeni_metin=""
    for i in s :
        if i.isalnum():
            yeni_metin =yeni_metin + i
    print(yeni_metin)
    tersi=yeni_metin[::-1]
    print(tersi)
    if yeni_metin==tersi:
        return True
    else:
        return False
        


