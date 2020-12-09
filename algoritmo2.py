
class Algoritmo2:
    
    def faiLaMagia(self,html_first_source,dict_second_source):
        
        coppie = []

        for i in range(0,len(html_first_source)):
    
            l1 = html_first_source[i]
            maxx = 0
            temp = []
   
            for j in range(0,len(dict_second_source)):
                d2 = dict_second_source[j]
                l2=[]
                cont = 0
                for k,v in d2.items():
                    if(d2[k]>0.07):
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