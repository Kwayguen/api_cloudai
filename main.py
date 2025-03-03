from fastapi import FastAPI
from pydantic import BaseModel

# 1) Importer la pipeline depuis transformers
from transformers import pipeline

app = FastAPI()

# 2) Charger le pipeline (ici pour le "summarization", comme exemple)
#    Cela télécharge le modèle la première fois (il doit y avoir une connexion internet).
#    Pour un usage hors-ligne, vous pourriez pré-télécharger et inclure le modèle dans votre conteneur Docker.
summarizer = pipeline("summarization")

# ----- Endpoints existants -----

@app.get("/")
def read_root():
    return {"message": "Hello depuis FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "description": f"Voici l'item numéro {item_id}"}


# 3) Définir un schéma de requête pour l'endpoint
class SummarizeRequest(BaseModel):
    text: str
    max_length: int = 50
    min_length: int = 5

# 4) Créer l'endpoint pour la transformation de texte
@app.post("/summarize")
def summarize_text(request: SummarizeRequest):

    # 5) Utiliser le pipeline pour transformer le texte
    summary = summarizer(
        request.text,
        max_length=request.max_length,
        min_length=request.min_length,
        do_sample=False
    )
    
    # Le pipeline retourne une liste de dict, ex: [{"summary_text": "..."}]
    return {"summary": summary[0]["summary_text"]}
