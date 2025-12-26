class MyQueue:
    def __init__(self):
        self.duz = []   # Giriş (Input)
        self.ters = []  # Çıkış (Output)

    def push(self, x):
        # 1. HATA DÜZELTİLDİ: Sadece giriş kutusuna ekliyoruz.
        self.duz.append(x)

    def pop(self):
        # Önce peek'i çağırıyoruz ki aktarma işlemi (varsa) yapılsın.
        self.peek()
        # Şimdi ters kutunun tepesindekini (aslında en eski elemanı) atıyoruz.
        return self.ters.pop()

    def peek(self):
        # İŞİN BEYNİ BURASI! 🧠
        # Eğer çıkış kutusu (ters) boşsa, giriştekileri oraya boşalt.
        if not self.ters:
            while self.duz:
                # Düz'den pop yapıp (sondan alıp), Ters'e append yapıyoruz.
                # Bu işlem sırayı tam tersine çevirir!
                elem = self.duz.pop()
                self.ters.append(elem)
        
        # Artık ters kutunun ucunda en eski eleman var.
        return self.ters[-1]

    def empty(self):
        # İkisi de boşsa kuyruk boştur.
        return len(self.duz) == 0 and len(self.ters) == 0