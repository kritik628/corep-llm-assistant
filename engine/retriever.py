import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data")

def load_documents():
    docs = {}
    for filename in ["pra_rules.txt", "corep_instructions.txt"]:
        with open(os.path.join(DATA_PATH, filename), "r", encoding="utf-8") as f:
            docs[filename] = f.read()
    return docs

def simple_retrieve(query: str):
    """
    Very basic keyword-based retrieval for prototype.
    Returns relevant rule paragraphs.
    """
    docs = load_documents()
    results = []

    for name, text in docs.items():
        paragraphs = text.split("\n\n")
        for para in paragraphs:
            if any(word.lower() in para.lower() for word in query.split()):
                results.append(para.strip())

    return results
