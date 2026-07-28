# Importe pipeline depuis Hugging Face
from transformers import pipeline


# Importe le nom du modèle depuis la configuration
from .config import SENTIMENT_MODEL



# Variable globale contenant le modèle
sentiment_classifier = None



# Fonction qui charge le modèle
def get_sentiment_model():

    global sentiment_classifier


    # Vérifie si le modèle est déjà chargé
    if sentiment_classifier is None:

        print("Chargement du modèle sentiment...")


        # Création du pipeline Hugging Face
        sentiment_classifier = pipeline(

            task="sentiment-analysis",

            model=SENTIMENT_MODEL

        )


        print("Modèle sentiment prêt")


    return sentiment_classifier