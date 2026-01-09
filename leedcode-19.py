# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        # 1. JOKER ELEMAN (DUMMY)
        # Listenin en başına sahte bir '0' ekliyoruz.
        # Böylece head silinse bile prev bu '0' düğümü olur, hata vermez.
        dummy = ListNode(0)
        dummy.next = head
        
        # İşaretçilerimizi jokerden başlatıyoruz
        fast = dummy
        slow = dummy
        
        # 2. ARADAKİ FARKI AÇ (n + 1 adım)
        # Neden n+1? Çünkü dummy'den başladık, farkı korumalıyız.
        for i in range(n + 1):
            fast = fast.next
        
        # 3. KAYDIRMA
        # fast sona gelene kadar ikisini de ilerlet
        while fast != None:
            slow = slow.next
            fast = fast.next
            
        # 4. SİLME
        # slow şu an silinecek düğümün BİR ÖNCESİNDE (prev görevinde).
        # slow.next'i atlayarak bağla.
        slow.next = slow.next.next
        
        # 5. SONUÇ
        # Jokerin arkasındakileri (gerçek listeyi) döndür.
        return dummy.next