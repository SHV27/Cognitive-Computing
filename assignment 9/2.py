import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords, wordnet
from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer


for pkg in ('punkt', 'stopwords', 'wordnet', 'averaged_perceptron_tagger'):
    nltk.download(pkg, quiet=True)


text = (
    "Artificial intelligence (AI) refers to the ability of machines to perform tasks "
    "that typically require human intelligence, such as learning, problem-solving, "
    "and decision-making. It's a broad field encompassing various technologies, "
    "including machine learning, deep learning, and natural language processing. "
    "AI systems can analyze data, identify patterns, make predictions, and even generate creative content."
)


def preprocess(t):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(t.lower())
    stops = set(stopwords.words('english'))
    return [tok for tok in tokens if tok not in stops]

def get_wordnet_pos(tag):
    if tag.startswith('J'): return wordnet.ADJ
    if tag.startswith('V'): return wordnet.VERB
    if tag.startswith('N'): return wordnet.NOUN
    if tag.startswith('R'): return wordnet.ADV
    return wordnet.NOUN


def stem_and_lemma(tokens):
    stemmers = {
        'porter': PorterStemmer(),
        'lancaster': LancasterStemmer(),
        'snowball': SnowballStemmer('english'),
    }
    results = {}
    for name, stemmer in stemmers.items():
        results[name] = [stemmer.stem(tok) for tok in tokens]


    lemmatizer = WordNetLemmatizer()
    pos_tags = nltk.pos_tag(tokens)
    results['lemmatized'] = [
        lemmatizer.lemmatize(tok, pos=get_wordnet_pos(tag))
        for tok, tag in pos_tags
    ]
    return results


def top_bigrams(tokens, n=5):
    bigrams = list(nltk.bigrams(tokens))
    freq = nltk.FreqDist(bigrams)
    return freq.most_common(n)


tokens = preprocess(text)
results = stem_and_lemma(tokens)
bigrams = top_bigrams(tokens)


for method, toks in results.items():
    print(f"{method.title():10s} → {toks}\n")

print("Top 5 Bigrams:", bigrams)
