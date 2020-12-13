from loader import Loader
import sys
from vectorizer import Vectorizer
from algoritmo1 import Algoritmo1

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
html_first_source = loader.load_pages_leaves(dataset_folder, "REALGM_pages", max_page)
html_second_source = loader.load_pages_leaves(dataset_folder, "ROTOWORLD_pages", max_page)
html_first_source2 = loader.load_pages_leaves(dataset_folder, "NBA_pages", max_page)
html_second_source2 = loader.load_pages_leaves(dataset_folder, "ROTOWORLD_pages", max_page)
html_first_source3 = loader.load_pages_leaves(dataset_folder, "NBA_pages", max_page)
html_second_source3 = loader.load_pages_leaves(dataset_folder, "REALGM_pages", max_page)
### Calcolo tf-idf e creazione dizionario {Termine : Tf_idf_associato} #####
vectorizer = Vectorizer()
dict_first_source = vectorizer.fit_transform(html_first_source)
dict_second_source = vectorizer.fit_transform(html_second_source)
dict_first_source2 = vectorizer.fit_transform(html_first_source2)
dict_second_source2 = vectorizer.fit_transform(html_second_source2)
dict_first_source3 = vectorizer.fit_transform(html_first_source3)
dict_second_source3 = vectorizer.fit_transform(html_second_source3)

############## Algoritmo 1########################
algoritmo1 = Algoritmo1()

coppie1 = algoritmo1.faiLaMagia(dict_first_source,dict_second_source)
coppie2 = algoritmo1.faiLaMagia(dict_first_source2,dict_second_source2)
coppie3 = algoritmo1.faiLaMagia(dict_first_source3,dict_second_source3)

num = 0
den = len(coppie1)
for coppia in coppie1:
    if(coppia[0] == coppia[1]):
        num += 1

precision = num/den
print("\n\n La precision del sistema REALGM VS ROTOWORLD è " + str(precision) + "\n\n")

recall = num/75
print("La recall del sistema REALGM VS ROTOWORLD è " + str(recall) + "\n\n")

f_measure = 2*(recall*precision)/(recall+precision)
print("La f1 measure del sistema REALGM VS ROTOWORLD è " + str(f_measure) + "\n\n")

num = 0
den = len(coppie2)
for coppia in coppie2:
    if(coppia[0] == coppia[1]):
        num += 1

precision = num/den
print("\n\n La precision del sistema NBA VS ROTOWORLD è " + str(precision) + "\n\n")

recall = num/75
print("La recall del sistema NBA VS ROTOWORLD è " + str(recall) + "\n\n")

f_measure = 2*(recall*precision)/(recall+precision)
print("La f1 measure del sistema NBA VS ROTOWORLD è " + str(f_measure) + "\n\n")

num = 0
den = len(coppie3)
for coppia in coppie3:
    if(coppia[0] == coppia[1]):
        num += 1

precision = num/den
print("\n\n La precision del sistema NBA VS REALGM è " + str(precision) + "\n\n")

recall = num/75
print("La recall del sistema NBA VS REALGM è " + str(recall) + "\n\n")

f_measure = 2*(recall*precision)/(recall+precision)
print("La f1 measure del sistema NBA VS REALGM è " + str(f_measure) + "\n\n")



######## Stampa per la seconda sorgente #########
#print("Inizio stampa dei dizionari relativi a tutte le pagine\n\n")
#for i in range(0,len(dict_first_source)):
#    print("Dizionario n°"+ str(i) +" della seconda sorgente\n")
#    print(dict_first_source[i])
#    print("\n\n")


