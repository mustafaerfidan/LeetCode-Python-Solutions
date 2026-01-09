import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # 1. Hile: Max Heap simülasyonu için sayıları negatife çevir
        # Örnek: [2, 7, 4, 1, 8, 1]  -->  [-2, -7, -4, -1, -8, -1]
        max_heap = [-s for s in stones]
        
        # 2. Listeyi Heap düzenine sok (O(N) sürede)
        heapq.heapify(max_heap)
        
        # 3. Torbada 1'den fazla taş olduğu sürece dövüştür
        while len(max_heap) > 1:
            # En küçükleri (yani aslında en ağır negatifleri) çek
            t1 = -heapq.heappop(max_heap) # En ağır (Örn: 8)
            t2 = -heapq.heappop(max_heap) # İkinci ağır (Örn: 7)
            
            # Taşlar eşit değilse, farkını geri at
            if t1 != t2:
                kalan = t1 - t2
                heapq.heappush(max_heap, -kalan) # Yine negatif atıyoruz!
        
        # 4. Sonuç: Taş kaldıysa ağırlığını, kalmadıysa 0 döndür
        if len(max_heap) == 0:
            return 0
        else:
            return -max_heap[0]