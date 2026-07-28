# Importe la classe FastAPI qui permet de créer une API REST
# et HTTPException qui permet de gérer les erreurs HTTP.
from fastapi import FastAPI, HTTPException


# Importe les schémas (modèles de données) définis avec Pydantic.
# ReviewRequest : structure des données envoyées par le client.
# ReviewResponse : structure des données renvoyées par l'API.
from .schemas import ( ReviewRequest,ReviewResponse
)

# Importe la fonction qui analyse le sentiment d'un avis.
from .sentiment import analyze_sentiment

# Importe la fonction qui détecte si un avis est urgent.
from .urgency import detect_urgency


# Création de l'application FastAPI.
# Les informations fournies seront visibles dans
# la documentation automatique (/docs).
app = FastAPI(

    # Nom de l'API
    title="AI E-commerce Review Filter",

    # Description affichée dans Swagger UI
    description="Analyse sentiment et urgence des avis clients"

)


# Route GET "/"
# Cette route sert simplement à vérifier que l'API fonctionne.

@app.get("/")
def home():

    # Retourne un message au format JSON.
    return {

        "message":
        "API Filtre intelligent des avis"

    }


# Route POST "/analyze-review"
# Cette route reçoit un avis client et effectue les analyses.

@app.post(

    # URL de l'endpoint
    "/analyze-review",

    # Modèle utilisé pour valider la réponse renvoyée.
    response_model=ReviewResponse

)
def analyze_review(

    # review représente les données envoyées par le client.
    # Elles sont automatiquement validées grâce à Pydantic.
    review: ReviewRequest

):

    # Bloc permettant de capturer les erreurs éventuelles.
    try:

        # ----------------------------------------------------------
        # Vérifie que le texte n'est pas vide.
        # strip() supprime les espaces au début et à la fin.
       
        if not review.text.strip():

            # Retourne une erreur HTTP 400
            # (Bad Request) si le texte est vide.
            raise HTTPException(

                status_code=400,

                detail="Texte vide"

            )

        # Analyse du sentiment
        #
        # Cette fonction retourne par exemple :
        #
        # {
        #     "sentiment": "POSITIVE",
        #     "confidence": 0.985
        # }
       
        sentiment = analyze_sentiment(

            review.text

        )

        # Analyse de l'urgence
        #
        # Cette fonction retourne par exemple :
        #
        # {
        #     "is_urgent": True,
        #     "category": "urgent customer complaint",
        #     "confidence": 0.964
        # }
      
        urgency = detect_urgency(

            review.text

        )

        
        # Construction de la réponse finale envoyée au client.
        
        return {

            # Sentiment détecté
            "sentiment":
            sentiment["sentiment"],

            # Score de confiance du sentiment
            "sentiment_confidence":
            sentiment["confidence"],

            # Indique si l'avis est urgent
            "is_urgent":
            urgency["is_urgent"],

            # Catégorie d'urgence détectée
            "urgency_category":
            urgency["category"],

            # Score de confiance de l'urgence
            "urgency_confidence":
            urgency["confidence"]

        }

  
    # Capture toutes les erreurs inattendues.
   
    except Exception as e:

        # Retourne une erreur HTTP 500
        # (Internal Server Error).
        raise HTTPException(

            status_code=500,

            detail=str(e)

        )