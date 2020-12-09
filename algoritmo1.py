

class Algoritmo1:
    
    def faiLaMagia(self,dict_first_source,dict_second_source):
        
        coppie = []

        for i in range(0,len(dict_first_source)):
    
            d1 = dict_first_source[i]
            l1 = []
            maxx = 0
            temp = []
    
            for k,v in d1.items():
                if(d1[k]>0.13):
                    l1.append(k)
    
            for j in range(0,len(dict_second_source)):
                d2 = dict_second_source[j]
                l2=[]
                cont = 0
                for k,v in d2.items():
                    if(d2[k]>0.13):
                        l2.append(k)
      
                for elem1 in l1:
                    for elem2 in l2:
                        if(elem1 == elem2):
                            cont += 1
              
                if(cont > maxx):
                    temp.insert(0,i)
                    temp.insert(1,j)
                    maxx = cont
            if (not temp):
                ##non aggiungere nessuna coppia visto che non hai trovato nemmeno un termine in comune
                pass
            else:
                coppie.append((temp[0],temp[1]))
            
        return coppie