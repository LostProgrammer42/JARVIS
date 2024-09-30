import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
df = pd.read_csv("Book2.csv", nrows=50,sep=",", encoding='cp1252')
vectorizer = TfidfVectorizer(max_features=1000)
vectors = vectorizer.fit_transform(df.Speech)


filename = 'intent.sav'
bayes_save = pickle.load(open(filename, 'rb'))
def findintent(uw):
    unknown=pd.DataFrame({'content': [uw]})
    unknown_vectors = vectorizer.transform(unknown.content)
    unknown_words_df = pd.DataFrame(unknown_vectors.toarray(), columns=vectorizer.get_feature_names_out())
    unknown_words_df.head()
    unknown['pred_logreg'] = bayes_save.predict(unknown_words_df)
    unknown['pred_logreg_proba'] = bayes_save.predict_proba(unknown_words_df)[:,1]
    #print(unknown)
    return(unknown['pred_logreg'].values)
if __name__ == "__main__":
    while True:
        uw=input("Enter Message:")
        print(findintent(uw))