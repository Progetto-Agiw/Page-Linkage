from sklearn.feature_extraction.text import TfidfVectorizer

class Vectorizer:
    
    def Tf_idf(self, html_source):
        
        vectorizer = TfidfVectorizer(stop_words = "english")
        vectors = vectorizer.fit_transform(html_source)
        dict_source = []

        for i in range(0,len(html_source)):
            document = vectors.getrow(i).tocoo()
            dict_source.append({k:v for k,v in zip(document.col, document.data)})

        for i in range(0,len(dict_source)):
            for k,v in vectorizer.vocabulary_.items():
                if(v in dict_source[i].keys()):
                    d = dict_source[i]
                    d[k] = d[v]
                    del d[v]
                    dict_source[i] = d

        for i in range(0,len(dict_source)):
            d = dict_source[i]
            d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse = True)}
            dict_source[i] = d
        
        return dict_source
    
    