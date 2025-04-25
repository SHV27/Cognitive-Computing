import re
import nltk
from nltk.tokenize import RegexpTokenizer, sent_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from textblob import TextBlob


nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)

text = """
Artificial intelligence (AI) refers to the ability of machines to perform tasks that 
typically require human intelligence, such as learning, problem-solving, and decision-making.
It's a broad field encompassing various technologies, including machine learning,
deep learning, and natural language processing. AI systems can analyze data,
identify patterns, make predictions, and even generate creative content.
"""


def clean_text(t):
    t = re.sub(r'\S+@\S+', '<EMAIL>', t)
    t = re.sub(r'https?://\S+|www\.\S+', '<URL>', t)
    t = re.sub(r'(\+91[\s-]?\d{10})|(\d{3}[-\s]\d{3}[-\s]\d{4})', '<PHONE>', t)
   
    t = re.sub(r'[^a-zA-Z0-9<> ]', ' ', t)
    return t.lower()

cleaned = clean_text(text)


sentences = sent_tokenize(text)
tokenizer = RegexpTokenizer(r'\w+')
words = tokenizer.tokenize(cleaned)


stops = set(stopwords.words('english'))
filtered = [w for w in words if w not in stops and len(w)>2]


stemmer = SnowballStemmer('english')
porter_stems = [stemmer.stem(w) for w in filtered]

lemmatizer = WordNetLemmatizer()
def get_wordnet_pos(tag):
   
    if tag.startswith('J'): return wordnet.ADJ
    if tag.startswith('V'): return wordnet.VERB
    if tag.startswith('N'): return wordnet.NOUN
    if tag.startswith('R'): return wordnet.ADV
    return wordnet.NOUN

pos_tags = nltk.pos_tag(filtered)
lemmas = [
    lemmatizer.lemmatize(word, pos=get_wordnet_pos(tag))
    for word, tag in pos_tags
]


tfidf = TfidfVectorizer(ngram_range=(1,2), max_features=10)
tfidf_matrix = tfidf.fit_transform([cleaned])
tfidf_scores = dict(zip(tfidf.get_feature_names_out(),
                        tfidf_matrix.toarray()[0]))


sent = TextBlob(text).sentiment


print("Sentences:", sentences)
print("\nFiltered tokens:", filtered)
print("\nSnowball stems:", porter_stems)
print("\nLemmas:", lemmas)
print("\nTop TF-IDF:", tfidf_scores)
print("\nSentiment (polarity, subjectivity):", sent)
