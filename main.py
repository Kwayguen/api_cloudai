from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

#    Par défaut, "bert-base-uncased" s'utilise souvent avec "[MASK]" comme token masqué.
fill_mask = pipeline("fill-mask", model="bert-base-uncased", tokenizer="bert-base-uncased")

class FillMaskRequest(BaseModel):
    text: str   # le texte avec un token [MASK] à remplir
    top_k: int = 5  # nombre de propositions à retourner

@app.post("/fill_mask")
def fill_mask_endpoint(request: FillMaskRequest):
    """
    Cette route reçoit un texte contenant un token [MASK],
    et utilise un modèle BERT pour proposer les meilleures options de remplissage.
    """
    # Utiliser le pipeline "fill-mask"
    results = fill_mask(request.text, top_k=request.top_k)

    # Le pipeline renvoie une liste d'objets de ce type :
    # [
    #   {
    #     'sequence': 'le texte modifié',
    #     'score': 0.051,
    #     'token': 1234,
    #     'token_str': 'Paris'
    #   },
    #   ...
    # ]
    return {"predictions": results}

@app.get("/")
def read_root():
    return {"message": "Hello depuis FastAPI & BERT!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
