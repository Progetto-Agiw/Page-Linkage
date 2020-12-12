from vectorizer import Vectorizer
from algoritmo1 import Algoritmo1
from loader import Loader

def entity_linkage(dataset_folder, site_a, site_b, max_page = None):
	### Caricamento file html e pulizia da tutti i tag #####
	print("pages: " + str(max_page))
	loader = Loader()
	html_first_source = loader.load_pages_leaves(dataset_folder, site_a, max_page)
	html_second_source = loader.load_pages_leaves(dataset_folder, site_b, max_page)
	### Calcolo tf-idf e creazione dizionario {Termine : Tf_idf_associato} #####
	vectorizer = Vectorizer()
	dict_first_source = vectorizer.fit_transform(html_first_source)
	dict_second_source = vectorizer.fit_transform(html_second_source)

	############## Algoritmo 1########################
	algoritmo1 = Algoritmo1()

	coppie1 = algoritmo1.faiLaMagia(dict_first_source,dict_second_source)

	i = 1
	precisions = []
	recalls = []

	num = 0
	den = len(coppie1)

	ground_truth_size = max_page if max_page != None else 75

	for coppia in coppie1[:75]:
	    if(coppia[0] == coppia[1]):
	        num += 1
	    current_precision = num / i
	    current_recall = num / ground_truth_size
	    precisions.append(current_precision)
	    recalls.append(current_recall)
	    i += 1

	'''
	precision = num/den
	print("\n\n La precision del sistema rumoroso è " + str(precision) + "\n\n")

	recall = num/75
	print("La recall del sistema rumoroso è " + str(recall) + "\n\n")

	f_measure = 2*(recall*precision)/(recall+precision)
	print("La f1 measure del sistema rumoroso è " + str(f_measure) + "\n\n")
	
	print(precisions)
	print(recalls)
	'''
	######## Stampa per la seconda sorgente #########
	#print("Inizio stampa dei dizionari relativi a tutte le pagine\n\n")
	#for i in range(0,len(dict_first_source)):
	#    print("Dizionario n°"+ str(i) +" della seconda sorgente\n")
	#    print(dict_first_source[i])
	#    print("\n\n")
	return precisions, recalls