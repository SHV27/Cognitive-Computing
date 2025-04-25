import re


text = (
    "Artificial intelligence (AI) refers to the ability of machines to perform "
    "tasks that typically require human intelligence, such as learning, problem-solving, "
    "and decision-making. It's a broad field encompassing various technologies, "
    "including machine learning, deep learning, and natural language processing. "
    "AI systems can analyze data, identify patterns, make predictions, "
    "and even generate creative content."
)

patterns = {
    "Words ≥6 letters":      r"\b\w{6,}\b",
    "Numbers":               r"\b\d+\b",
    "Capitalized Words":     r"\b[A-Z][a-z]*\b",
    "ALL-CAPS ABBREVS":      r"\b[A-Z]{2,}\b",
    "Alphabetic Only":       r"\b[a-zA-Z]+\b",
    "Starts with Vowel":     r"\b[AEIOUaeiou]\w*\b",
    "Hyphenated Words":      r"\b\w+(?:-\w+)+\b",
}


compiled = {name: re.compile(pat) for name, pat in patterns.items()}


def extract_all(text, comp_dict):
    results = {}
    for name, regex in comp_dict.items():
        matches = regex.findall(text)
        results[name] = matches
    return results

results = extract_all(text, compiled)

for label, items in results.items():
    print(f"{label:20s} ({len(items)} found): {items}")
