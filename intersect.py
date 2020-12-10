
class Intersect:
    
    
    def intersect_cardinality(self,lista_termini_1,lista_termini_2):
            
        cardinality = 0
        for elem1 in lista_termini_1:
            for elem2 in lista_termini_2:
                if(elem1 == elem2):
                    cardinality += 1            
        
        return cardinality