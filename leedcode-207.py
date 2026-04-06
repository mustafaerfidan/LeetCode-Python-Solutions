class Solution:
    def canFinish(self, numCourses, prerequisites):
        graf = [[] for _ in range(numCourses)]
        for ders, on_kosul in prerequisites:
            graf[on_kosul].append(ders)
            
        durum = [0] * numCourses

        def dongu_var_mi(su_anki_ders):
            if durum[su_anki_ders] == 1: return True
            if durum[su_anki_ders] == 2: return False

            durum[su_anki_ders] = 1
            for sonraki_ders in graf[su_anki_ders]:
                if dongu_var_mi(sonraki_ders):
                    return True
            
            durum[su_anki_ders] = 2
            return False

        # Her bir ders için kontrol başlat (Çünkü bazı dersler bağımsız olabilir)
        for i in range(numCourses):
            if dongu_var_mi(i):
                return False # Bir tane bile döngü varsa dersler bitmez
                
        return True # Hiç döngü yoksa True