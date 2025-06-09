from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Reutiliza el índice ya guardado
_embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
_db = FAISS.load_local("app/resospy_index", _embeddings, allow_dangerous_deserialization=True)

def search_rag(query: str, k: int = 3):
    docs = _db.similarity_search(query, k=k)
    results = []
    for doc in docs:
        results.append({
            "file_name": doc.metadata.get("file_name", ""),
            "manufacturer": doc.metadata.get("manufacturer", ""),
            "path": doc.metadata.get("path", ""),
            "fragment": doc.page_content[:1000]
        })
    return results