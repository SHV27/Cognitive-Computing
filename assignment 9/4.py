import re


MASKS = [
    (r'\S+@\S+', '<EMAIL>'),
    (r'https?://\S+|www\.\S+', '<URL>'),
    (r'\+91[\s-]?\d{10}|\d{3}[-\s]\d{3}[-\s]\d{4}', '<PHONE>')
]


TOKEN_RE = re.compile(r"\b\w+(?:[-']\w+)*\b")

def clean_and_tokenize(text):
  
    for pattern, placeholder in MASKS:
        text = re.sub(pattern, placeholder, text, flags=re.IGNORECASE)

    text = text.lower()

    tokens = TOKEN_RE.findall(text)
    return text, tokens


text = (
    "Artificial intelligence (AI) refers to the ability of machines to perform tasks "
    "that typically require human intelligence, such as learning, problem-solving, "
    "and decision-making. It's a broad field encompassing various technologies, "
    "including machine learning, deep learning, and natural language processing. "
    "AI systems can analyze data, identify patterns, make predictions, and even generate creative content."
)

cleaned, tokens = clean_and_tokenize(text)

print("Processed Text:\n", cleaned)
print("\nTokens:\n", tokens)
