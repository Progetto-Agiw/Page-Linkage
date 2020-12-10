

class Algoritmo1:
    
    def faiLaMagia(self,dict_first_source,dict_second_source):
        
        coppie = []

        for i in range(0,len(dict_first_source)):
    
            d1 = dict_first_source[i]
            maxx = 0
            couple_temp = []
    
            high_values_list_1 = self.get_high_values(d1, 0.11)
    
            for j in range(0,len(dict_second_source)):
                
                d2 = dict_second_source[j]
                high_values_list_2 = self.get_high_values(d2, 0.11)
                cardinality = self.intersect_cardinality(high_values_list_1, high_values_list_2)
    
                if(cardinality > maxx and cardinality > 1):
                    couple_temp.insert(0,i)
                    couple_temp.insert(1,j)
                    maxx = cardinality
                    
            if (not couple_temp):
                ##non aggiungere nessuna coppia visto che non hai trovato almeno due termini in comune
                pass
            else:
                coppie.append((couple_temp[0],couple_temp[1]))
            
        return coppie
    
    
    
    def intersect_cardinality(self,lista_termini_1,lista_termini_2):
            
        cardinality = 0
        for elem1 in lista_termini_1:
            for elem2 in lista_termini_2:
                if(elem1 == elem2):
                    cardinality += 1            
        
        return cardinality
    
    
    
    def get_high_values(self,dictionary,soglia):
        
        high_values_list = []
        for k,_ in dictionary.items():
            if(dictionary[k] > soglia):
                high_values_list.append(k)
                
        return high_values_list
                    
                    
                    