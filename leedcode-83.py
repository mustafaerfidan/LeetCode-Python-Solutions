def deleteDuplicates(head):
    temp=head
    while temp != None and temp.next!= None :
        if temp.val == temp.next.val:
            temp.next=temp.next.next
        else:
            temp=temp.next
    return head

              
        

        
        
        
    


