from intersect import Intersect

class Algoritmo1:
    
    SOGLIA_MINIMA_INTERSEZIONE = 1
    
    def faiLaMagia(self,dict_first_source,dict_second_source):
        
        coppie = []
        
        intersect = Intersect()

        for i in range(0,len(dict_first_source)):
    
            d1 = dict_first_source[i]
            cardinality_list = []
    
            high_values_list_1 = self.get_high_values(d1, 0.11)
    
            for j in range(0,len(dict_second_source)):
                
                d2 = dict_second_source[j]
                high_values_list_2 = self.get_high_values(d2, 0.11)
                cardinality_list.append(intersect.intersect_cardinality(high_values_list_1, high_values_list_2))
             
            maxx = max(cardinality_list)
            if (maxx > self.SOGLIA_MINIMA_INTERSEZIONE):
                coppie.append((i, cardinality_list.index(maxx)))
            
        return coppie
        
    
    def get_high_values(self,dictionary,soglia):
        
        high_values_list = []
        for k,_ in dictionary.items():
            if(dictionary[k] > soglia):
                high_values_list.append(k)
                
        return high_values_list
    
           
    
    
    
    
                    
                    
                    