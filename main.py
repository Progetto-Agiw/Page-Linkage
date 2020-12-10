from loader import Loader
import sys
from vectorizer import Vectorizer
from algoritmo1 import Algoritmo1
from algoritmo2 import Algoritmo2

if len(sys.argv) < 2:
	print("usage: entity-linkage <dataset-folder> <page-limit>")
	exit()

dataset_folder = sys.argv[1]

if len(sys.argv) >= 3:
	max_page = int(sys.argv[2])
else:
	max_page = None

### Caricamento file html e pulizia da tutti i tag #####
loader = Loader()
html_first_source = loader.load_pages_leaves(dataset_folder, "site-a", max_page)
html_first_source2 = loader.load_pages(dataset_folder, "site-a", max_page)
html_second_source = loader.load_pages_leaves(dataset_folder, "site-b", max_page)
### Calcolo tf-idf e creazione dizionario {Termine : Tf_idf_associato} #####
vectorizer = Vectorizer()
dict_first_source = vectorizer.fit_transform(html_first_source)
dict_second_source = vectorizer.fit_transform(html_second_source)

############## Algoritmo 1########################
algoritmo1 = Algoritmo1()

coppie1 = algoritmo1.faiLaMagia(dict_first_source,dict_second_source)

############## Algoritmo 2########################
algoritmo2 = Algoritmo2()

coppie2 = algoritmo2.faiLaMagia(html_first_source2,dict_second_source)

###### Stampa risultati 1##################
num = 0
den = len(coppie1)
for coppia in coppie1:
    #print("Pagina " + str(coppia[0]) + " accoppiata con pagina " + str(coppia[1]) + " \n")
    if(coppia[0] == coppia[1]):
        num += 1

precision = num/den
print("\n\n La precision del sistema numero 1 è " + str(precision) + "\n\n")

recall = num/len(dict_second_source)
print("La recall del sistema numero 1 è " + str(recall) + "\n\n")

###### Stampa risultati 2##################
#num = 0
#den = len(coppie2)
#for coppia in coppie2:
    #print("Pagina " + str(coppia[0]) + " accoppiata con pagina " + str(coppia[1]) + " \n")
#    if(coppia[0] == coppia[1]):
#        num += 1

#precision = num/den
#print("\n\n La precision del sistema numero 2 è " + str(precision) + "\n\n")

#recall = num/len(dict_second_source)
#print("La recall del sistema numero 2 è " + str(recall) + "\n\n")


######## Stampa per la seconda sorgente #########
#print("Inizio stampa dei dizionari relativi a tutte le pagine\n\n")
#for i in range(0,len(dict_first_source)):
#    print("Dizionario n°"+ str(i) +" della seconda sorgente\n")
#    print(dict_first_source[i])
#    print("\n\n")


