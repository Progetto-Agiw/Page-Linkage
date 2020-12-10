

class Algoritmo1:
    
    SOGLIA_MINIMA_INTERSEZIONE = 1
    
    def faiLaMagia(self,dict_first_source,dict_second_source):
        
        coppie = []

        for i in range(0,len(dict_first_source)):
    
            d1 = dict_first_source[i]
            cardinality_list = []
    
            high_values_list_1 = self.get_high_values(d1, 0.11)
    
            for j in range(0,len(dict_second_source)):
                
                d2 = dict_second_source[j]
                high_values_list_2 = self.get_high_values(d2, 0.11)
                cardinality_list.append(self.intersect_cardinality(high_values_list_1, high_values_list_2))
             
            maxx = max(cardinality_list)
            if (maxx > self.SOGLIA_MINIMA_INTERSEZIONE):
                coppie.append((i, cardinality_list.index(maxx)))
            
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
    
    
    def index_max_cardinality(self,cardinality_list, soglia_minima):
        
        maxx = max(cardinality_list)
        if (maxx >= soglia_minima):
            return cardinality_list.index(maxx)
        else:
            return -1
           
    
    
    
    
                    
                    
                    