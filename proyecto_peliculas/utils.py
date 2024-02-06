from gensim.models import Word2Vec
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
from dotenv import load_dotenv
from openai import OpenAI
import os
import AstraDB
from sentence_transformers import SentenceTransformer

secret_string = os.getenv("OPENAI_API_KEY")

# Configurar el motor de OpenAI
engine = "gpt-4"
embeddings = OpenAIEmbeddings(api_key=secret_string, model="text-embedding-3-large")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_embedding_GPT(text):
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    # Obtener el embedding del primer elemento de la respuesta
    embedding = response.data[0].embedding
    return embedding
def get_embeding_BERT(text):
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    return model.encode(text)

def get_embedding_w2v_tfidf(text, model, corpus):
    tokens = word_tokenize(text.lower())  # Assuming you want to lowercase the tokens

    # Create a TF-IDF vectorizer and fit on the provided corpus
    tfidf_vectorizer = TfidfVectorizer(tokenizer=word_tokenize)
    tfidf_vectorizer.fit(corpus)

    # Calculate TF-IDF values for the tokens in the input text
    tfidf_values = tfidf_vectorizer.transform([' '.join(tokens)]).toarray()

    # Calculate the weighted sum of word vectors based on TF-IDF values
    weighted_sum = sum(tfidf_values[0, i] * model.wv[word] for i, word in enumerate(tokens) if word in model.wv)

    # If no words from the input text are in the vocabulary, return None
    if weighted_sum.shape == (0,):
        return None

    # Return the normalized vector
    return weighted_sum / tfidf_values.sum()


def get_embedding(text):
    query_result = embeddings.embed_query(text)
    print(query_result)
    return query_result

def get_similarity(movie_description,N):
    db = AstraDB(token=os.getenv("ASTRA_DB_APPLICATION_TOKEN"), api_endpoint=os.getenv("ASTRA_DB_API_ENDPOINT"))
    collection = db.collection(collection_name="vector_movies")
    vector_embedding = get_embedding(movie_description)
    list_vec = collection.vector_find(
        vector=vector_embedding,
        limit=10
    )

    # Extract the movie titles from the 'text' values in the list
    titles = [item['text'].split(':')[0].strip('\"') for item in list_vec]

    return titles[1:(N+1)]

