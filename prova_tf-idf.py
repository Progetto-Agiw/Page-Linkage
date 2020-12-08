import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from lxml import html

#Lista di liste contenente tutti gli url delle sorgenti
#urls_basket = [["https://www.nba.com/player/1630173/precious-achiuwa/","https://www.nba.com/player/1629121/jaylen-adams/",
#           "https://www.nba.com/player/203500/steven-adams/"],["https://basketball.realgm.com//player/Precious-Achiuwa/Summary/107977",
#                                                               "https://basketball.realgm.com//player/Jaylen-Adams/Summary/80385",
#                                                               "https://basketball.realgm.com//player/Steven-Adams/Summary/27993"]]
   
  #Lista di liste contenente tutti gli url delle sorgenti caricata dai due file con tutti gli URL già estratti                                                          
#########################################################################
#Prima sorgente
nba_file = open("url_nba.txt","r")
content_nba= nba_file.read()
content_list_nba = content_nba.split(",")
#print(content_list_nba)

#Seconda sorgente
realm_file = open("url_realm.txt","r")
content_realm= realm_file.read()
content_list_realm = content_realm.split(",")
#print(content_list_realm)

#Lista di liste di url
urls_basket = [content_list_nba, content_list_realm]

#########################################################################
html_first_source = []
html_second_source = []
#Creazione lista con pagine html ripulite da tutto il rumore e 
#ricostruite come concatenazione dei soli testi contenuti nelle foglie

#######Lista pagine prima sorgente################
for url in urls_basket[0]:
    if(url == ''):
        break
    print("Scaricando HTML del seguente url: "+ url + "     della prima sorgente\n")
    dom_tree = html.fromstring(requests.get(url).text)
    all_leaves = dom_tree.xpath("//body//*[text()[not(normalize-space()='')]][not(self::script or self::style or self::meta or self::noscript)]/text()")
    page = ""
    for elem in all_leaves:
        page = page + " "+ elem
    html_first_source.append(page)

#######Lista seconda sorgente################   
for url in urls_basket[1]:
    if(url == ''):
        break
    print("Scaricando HTML del seguente url: "+ url + "     della seconda sorgente\n")
    dom_tree = html.fromstring(requests.get(url).text)
    all_leaves = dom_tree.xpath("//body//*[text()[not(normalize-space()='')]][not(self::script or self::style or self::meta or self::noscript)]/text()")
    page = ""
    for elem in all_leaves:
        page = page + " "+ elem
    html_second_source.append(page)
    

########Calcolo tf-idf sulla prima sorgente#################
vectorizer = TfidfVectorizer(stop_words="english")
print("Comincio il calcolo del TF-IDF relativo alla prima sorgente\n")
vectors = vectorizer.fit_transform(html_first_source)
print("Finito il calcolo del TF-IDF relativo alla prima sorgente\n")
########Costruzione lista di dizionari del tipo {Termine : Valore tf-idf associato}, per ogni pagina della prima sorgente########

###N.B. come corpus sono state prese tutte le pagine della stessa sorgente

dict_first_source = []
print("Inizio trasformazione in un bel dizionario Termine : Valore TF-IDF\n")
for i in range(0,len(html_first_source)):
    document = vectors.getrow(i).tocoo()
    dict_first_source.append({k:v for k,v in zip(document.col, document.data)})

for i in range(0,len(dict_first_source)):
    for k,v in vectorizer.vocabulary_.items():
        if(v in dict_first_source[i].keys()):
            d = dict_first_source[i]
            d[k] = d[v]
            del d[v]
            dict_first_source[i] = d

for i in range(0,len(dict_first_source)):
    d = dict_first_source[i]
    d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse = True)}
    dict_first_source[i] = d
    
########Calcolo tf-idf sulla seconda sorgente#################
vectorizer = TfidfVectorizer(stop_words="english")
print("Comincio il calcolo del TF-IDF relativo alla seconda sorgente\n")
vectors = vectorizer.fit_transform(html_second_source)
print("Finito il calcolo del TF-IDF relativo alla seconda sorgente\n")
########Costruzione lista di dizionari del tipo {Termine : Valore tf-idf associato}, per ogni pagina della seconda sorgente########

###N.B. come corpus sono state prese tutte le pagine della stessa sorgente

dict_second_source = []
print("Inizio trasformazione in un bel dizionario Termine : Valore TF-IDF\n")
for i in range(0,len(html_second_source)):
    document = vectors.getrow(i).tocoo()
    dict_second_source.append({k:v for k,v in zip(document.col, document.data)})

for i in range(0,len(dict_second_source)):
    for k,v in vectorizer.vocabulary_.items():
        if(v in dict_second_source[i].keys()):
            d = dict_second_source[i]
            d[k] = d[v]
            del d[v]
            dict_second_source[i] = d

for i in range(0,len(dict_second_source)):
    d = dict_second_source[i]
    d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse = True)}
    dict_second_source[i] = d
    
#######################################################################

coppie = []

for i in range(0,len(dict_first_source)):
    
    d1 = dict_first_source[i]
    l1 = []
    maxx = 0
    temp = []
    
    for k,v in d1.items():
        if(d1[k]>0.13):
            l1.append(k)
    #print("Termini sorgente " + str(i) + " "  + str(l1) + "\n")
    
    for j in range(0,len(dict_second_source)):
        d2 = dict_second_source[j]
        l2=[]
        cont = 0
        for k,v in d2.items():
            if(d2[k]>0.13):
                l2.append(k)
        #print("Termini sorgente " + str(j) + " "  + str(l2) + "\n")
        for elem1 in l1:
            for elem2 in l2:
                if(elem1 == elem2):
                    cont += 1
        #print("Pagina " + str(i) + "con pagina " + str(j) + "contatore = " + str(cont) + "\n")
        
        if(cont > maxx):
            #print("il contatore era: " + str(cont))
            temp.insert(0,i)
            temp.insert(1,j)
            maxx = cont
            #print("il max è diventato: "+ str(maxx))
    if (not temp):
        ##non aggiungere nessuna coppia visto che non hai trovato nemmeno un termine in comune
        print("Pagina " + str(i) + " non accoppiata" + "\n")
    else:
        coppie.append((temp[0],temp[1]))

############# Stampa risultati accoppiamenti #############
num = 0
den = len(coppie)
for coppia in coppie:
    print("Pagina " + str(coppia[0]) + " accoppiata con pagina " + str(coppia[1]) + " \n")
    if(coppia[0] == coppia[1]):
        num += 1

############# Calcolo precision e recall #################

precision = num/den
print("\n\n La precision del sistema è " + str(precision) + "\n\n")

recall = num/len(dict_first_source)
print("La recall del sistema è " + str(recall) + "\n\n")

######## Stampa per la seconda sorgente #########
#print("Inizio stampa dei dizionari relativi a tutte le pagine\n\n")
#for i in range(0,len(dict_second_source)):
#    print("Dizionario n°"+ str(i) +" della seconda sorgente\n")
#    print(dict_second_source[i])
#    print("\n\n")



   
    


