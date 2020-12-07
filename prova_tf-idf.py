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
content_list_realm = content_realm.split("\n")
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
    print("Scaricando HTML del seguente url: "+ url + "     della prima sorgente\n")
    dom_tree = html.fromstring(requests.get(url).text)
    all_leaves = dom_tree.xpath("//body//*[text()[not(normalize-space()='')]][not(self::script or self::style or self::meta or self::noscript)]/text()")
    page = ""
    for elem in all_leaves:
        page = page + " "+ elem
    html_first_source.append(page)

#######Lista seconda sorgente################   
for url in urls_basket[1]:
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

######## Stampa per la prima sorgente #########
print("Inizio stampa dei dizionari relativi a tutte le pagine\n\n")
for i in range(0,len(dict_first_source)):
    print("Dizionario n°"+i+" della prima sorgente\n")
    print(dict_first_source[i])
    print("\n\n")

###Per ora non ho raggiunto il risultato sperato, mi aspettavo di avere come termini più significativi il nome, cognome, squadra etc
###invece c'è molto rumore, forse è perchè il corpus è veramente molto piccolo (solo 3 documenti)

###TODO: provare con un corpus più ampio prima di abbandonare o proseguire per questa strada    
    


