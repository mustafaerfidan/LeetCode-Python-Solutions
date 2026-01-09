def countStudents(students, sandwiches):
    # 'count' değişkeni üst üste kaç öğrencinin sandviçi reddettiğini sayar [cite: 1829]
    count = 0 
    
    while len(students) > 0:
        if students[0] == sandwiches[0]:
            sandwiches.pop(0) # Sandviç yığınının tepesinden gider [cite: 1831, 1832]
            students.pop(0)
            count = 0 # Birisi yemek yediği için sayacı sıfırlıyoruz [cite: 1834]
        else:
            # Eşleşme yoksa öğrenci sona geçer [cite: 1835, 1836]
            gecici = students.pop(0)
            students.append(gecici)
            count += 1 # Reddeden öğrenci sayısını artır [cite: 1838]

        # EĞER reddeden sayısı mevcut öğrenci sayısına ulaşmışsa, 
        # kuyruktaki hiç kimse en üstteki sandviçi istemiyor demektir [cite: 1749, 1817, 1830]
        if count == len(students):
            break
            
    return len(students) # Kalan (aç kalan) öğrencileri döndür [cite: 1839]