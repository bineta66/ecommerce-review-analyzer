# Importe pipeline depuis Hugging Face
from transformers import pipeline


# Importe le nom du modèle depuis la configuration
from .config import SENTIMENT_MODEL



# Variable globale contenant le modèle
sentiment_classifier = None



def get_sentiment_model():

    global sentiment_classifier

    if sentiment_classifier is None:

        try:
            print("Chargement du modèle sentiment...")

            sentiment_classifier = pipeline(
                task="sentiment-analysis",
                model=SENTIMENT_MODEL
            )

            print("Modèle sentiment prêt")

        except Exception as e:

            print(
                f"Erreur chargement modèle : {e}"
            )

            raise e

    return sentiment_classifier