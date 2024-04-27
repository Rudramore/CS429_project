# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
import nltk
from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
import pickle
import re
import json

from itemadapter import ItemAdapter
from collections import defaultdict

class HtmlscraperPipeline:

    def open_spider(self, spider):
        # Initialize lists to store seperate values
        self.text =[]
        self.url = []   
        self.title = [] 

    def process_item(self, item, spider):
        #use items to keep track of text
        item_adap = ItemAdapter(item)
        self.title.append(item_adap['title'])
        if 'text' in item_adap:
            preprocessed_text = preprocess(item_adap['text'])
            # print("Stemmed in process function:",preprocessed_text)
            # print("Lemmatized in process function:", preprocessed_text)
            if preprocessed_text:  # Ensure there is content after preprocessing
                self.text.append(preprocessed_text)
                self.url.append(item_adap['url'])
            else:
                spider.logger.debug(f"Preprocessed text was empty for URL {item_adap['url']}")
        return item
    
    def close_spider(self,spider):
        #build vectors for tf-idf values for each term
        self.vectors = TfidfVectorizer()

        tf_idf_vec = self.vectors.fit_transform(self.text)

        # building the inverted idx with tfidf values
        feature_names = self.vectors.get_feature_names_out()
        inverted_ind = {feature: [] for feature in feature_names}

        for i, doc_vector in enumerate(tf_idf_vec):
            row = doc_vector.toarray().flatten()
            for j, tfidf_score in enumerate(row):
                if tfidf_score > 0:  # Only store terms with non-zero tf-idf scores
                    inverted_ind[feature_names[j]].append((self.url[i], tfidf_score))
                # if url_index < len(self.url):
                #     inverted_ind[feature].append((self.url[url_index], tf_score))
                # else:
                #     print(f"Index out of range: {url_index} for URL")
               # inverted_i nd[feature].append((self.url[url_index],tf_score))

                # Extract IDF values
#         idf_values = dict(zip(self.vectors.get_feature_names_out(), self.vectors.idf_))
# # --------------------tf values --------------------------------------------#
#         # Initialize TF matrix calculation
#         tf_vectorizer = TfidfVectorizer(use_idf=False)
#         tf_matrix = tf_vectorizer.fit_transform(self.text)

#         # Construct term frequency dictionary
#         tf_values = {url: {} for url in self.url}
#         feature_names = tf_vectorizer.get_feature_names_out()

#         for i, doc_vector in enumerate(tf_matrix):
#             row = doc_vector.toarray().flatten()
#             for j, tf in enumerate(row):
#                 if tf > 0:  # Only store terms with non-zero frequencies
#                     tf_values[self.url[i]][feature_names[j]] = tf

#         # Store TF and IDF values in a JSON document
#         with open('tf_idf_values.json', 'w') as f:
#             json.dump({
#                 'tf_values': tf_values,
#                 'idf_values': idf_values
#             }, f, indent=4)

        # mapping the URL to the title of the webpage
        url_to_title = {url: title for url, title in zip(self.url, self.title)}

        with open('inverted_index.pkl', 'wb')as f:
            pickle.dump(inverted_ind, f)

        with open('urls_title.pkl', 'wb')as url_type:
            pickle.dump(url_to_title, url_type)

        with open('vector_tranform_matrix','wb') as vt:
            pickle.dump(self.vectors, vt)

stop_words = set(stopwords.words('english'))

def preprocess(strings_test):
    # print("Original:", strings_test)

    # Remove new line special characters between the strings
    strings_m = strings_test.replace('\n', ' ')
    # print("No newlines:", strings_m)

    # Remove any additional unicode characters between the strings
    strings_m = re.sub(r'[^\x00-\x7F]+', ' ', strings_m)
    # print("ASCII only:", strings_m)

    # Remove all stop words
    string_t = strings_m.split()
    string_t = [str_test for str_test in string_t if str_test.lower() not in stop_words]
    # print("No stop words:", string_t)

    # Apply stemming
    # ps = PorterStemmer()
    # stemmed_string = [ps.stem(word) for word in string_t]

    # Apply lemmatization
    lz = WordNetLemmatizer()
    lemmatized_words = [lz.lemmatize(word) for word in string_t]
    # print("Lemmatized in preprocess:", lemmatized_words)

    processed_text = ' '.join(lemmatized_words)
    return processed_text







