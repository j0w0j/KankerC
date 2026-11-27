from pathlib import Path
import re

def load_docs_per_line(filepath : str | Path):
    """Leest een txt. file in en geeft elk document (elke regel) als item in een lijst terug """
    path =  Path(filepath)
    with path.open('r', encoding='utf-8') as f:
        documents = []
        for line in f:
            line_without_enter = line.rstrip("\r\n")
            # skip empty lines
            if line_without_enter.strip():
                documents.append(line_without_enter)
        return documents

def load_multiple_files(*filepaths):
    """Leest meerdere txt. files in en bewaar de documenten per file naam"""
    result = {}
    for path in filepaths:
        result[path] = load_docs_per_line(path)
    return result

def basic_tokenize(text : str):
    """Zet tekst om naar kleine letters en haalt losse woorden/leestekens op"""
    text = text.lower()
    # pakt hele woorden/cijfers of losse leestekens spaties doen hier niet mee
    return re.findall(r"\w+|[^\w\s]",text, flags=re.UNICODE)

def count_tokens(tokens: list[str]):
    """telt hoevaak elk token in 1 document voorkomt"""
    counts : dict[str,int]= {}
    for token in tokens:
        counts[token] = counts.get(token,0)+1
    return counts

def build_vocab(tokenized_docs: list[list[str]]):
    """Maakt een vaste mapping van token -> kolom-index."""
    vocab: dict[str, int] = {}
    for tokens in tokenized_docs:
        for token in tokens:
            if token not in vocab:
                vocab[token] = len(vocab)
    return vocab

def main():
    docs_per_file = load_multiple_files("KankerC/Input/test.txt", "KankerC/Input/test2.txt")
    all_tokenized_docs = []

    for filename, docs in docs_per_file.items():
        print(f"\nPath= {filename}")
        for i, doc in enumerate(docs, start=1):
            tokens = basic_tokenize(doc)
            all_tokenized_docs.append(tokens)
            counts = count_tokens(tokens)
            top_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:5]
            print(f"  doc {i} ({len(tokens)} tokens): {tokens}")
            print(f"  doc {i} top counts: {top_counts}")

    vocab = build_vocab(all_tokenized_docs)
    print(f"\n=== Vocab ({len(vocab)} unieke tokens) ===")
    for token, idx in vocab.items():
        print(f"{idx}: {token}")

if __name__ == "__main__":
    main()