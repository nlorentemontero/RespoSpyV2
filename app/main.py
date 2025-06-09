from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
from app.rag_utils import search_rag

app = FastAPI(title="ResoSpy API")

@app.get("/search", summary="Buscar documentos relacionados", tags=["RAG"])
def search(query: str = Query(..., description="Consulta semántica en español")):
    results = search_rag(query)
    return {"results": results}