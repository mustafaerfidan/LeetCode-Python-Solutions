class MyHashMap:

    def __init__(self):
        self.size=1000
        self.tablo=[]
        for i in range(self.size):
            self.tablo.append([])

    def fonksyon(self,key):
        index=key%self.size
        return index
        
        

    def put(self, key, value):
            index=self.fonksyon(key)
            liste=self.tablo[index]
            for i in liste:
                 if i[0]==key:
                      i[1]=value
                      return
            self.tablo[index].append([key,value])


    def get(self, key):
         index=self.fonksyon(key)
         liste=self.tablo[index]
         for i in liste:
            if i[0]==key:
                 return i[1]
         return -1 


    def remove(self, key):
        
         index=self.fonksyon(key)
         liste=self.tablo[index]
         for i in liste:
              if i[0]==key:
                   liste.remove(i)
                   return 
        


    
         
        

        


