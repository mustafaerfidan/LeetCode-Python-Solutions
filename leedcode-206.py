# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(head):
    prev = None   # En başta arkamız boş (None)
    curr = head   # İlk vagon (head) ile başlıyoruz
    
    while curr:   # Vagonlar bitene kadar dön
        # 1. ADIM: Bağlantıyı koparmadan önce sonrakini yedeğe al
        temp = curr.next 
        
        # 2. ADIM: Oku (next) geriye, yani prev'e çevir
        curr.next = prev
        
        # 3. ADIM: 'prev' artık şu anki düğüm olsun (bir ileri gel)
        prev = curr
        
        # 4. ADIM: 'curr' da yedeğe aldığımız yere geçsin (bir ileri git)
        curr = temp
        
    # Döngü bittiğinde 'curr' boşa düşer (None olur).
    # Yeni listenin başı 'prev' işaretçisinde kalır.
    return prev