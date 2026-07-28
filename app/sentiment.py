from .sentiment_model import get_sentiment_model
from .config import MAX_TEXT_LENGTH


# Variable globale qui contiendra le modèle chargé
classifier = None


def analyze_sentiment(text):

    global classifier

    # Chargement du modèle une seule fois
    if classifier is None:

        print("Chargement modèle sentiment...")

        classifier = get_sentiment_model()

        print("Modèle sentiment chargé")


    # Limiter la taille du texte
    text = text[:MAX_TEXT_LENGTH]


    # Analyse du texte avec Hugging Face
    result = classifier(text)


    # Récupération du label prédit
    label = result[0]["label"]

    # Récupération du score de confiance
    confidence = result[0]["score"]


    # Correction :
    # Si le modèle n'est pas suffisamment sûr,
    # on considère le texte comme neutre.
    if confidence < 0.60:

        label = "neutre"


    return {

        "sentiment": label,

        "confidence": round(
            confidence,
            3
        )

    }