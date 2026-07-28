# Importe la fonction qui charge le modèle Hugging Face.
# Cette fonction contient le pipeline sentiment-analysis.
from .sentiment_model import get_sentiment_model


# Importe la limite maximale de caractères autorisés.
# Cette valeur vient du fichier config.py
# Exemple dans .env :
# MAX_TEXT_LENGTH=1000
from .config import MAX_TEXT_LENGTH



# Variable globale qui va stocker le modèle chargé.
#
# Au début :
# classifier = None
#
# Après le premier appel :
# classifier contient le modèle Hugging Face en mémoire.
classifier = None



# Fonction qui analyse le sentiment d'un avis client.
#
# Entrée :
# text = avis du client
#
# Exemple :
# "Très bon produit, livraison rapide"
#
# Sortie :
# {
#   "sentiment": "positive",
#   "confidence": 0.98
# }
def analyze_sentiment(text):


    # Permet de modifier la variable globale classifier
    # à l'intérieur de cette fonction.
    global classifier



    # Vérifie si le modèle n'est pas encore chargé.
    #
    # Premier appel :
    # classifier = None
    #
    # Le modèle sera chargé.
    #
    # Appels suivants :
    # classifier contient déjà le modèle.
    if classifier is None:


        # Affichage dans le terminal
        # pour suivre le chargement.
        print("Chargement modèle sentiment...")



        # Appelle la fonction qui crée le pipeline Hugging Face.
        #
        # Exemple :
        # CardiffNLP XLM-RoBERTa
        #
        # Le modèle est ensuite gardé en mémoire.
        classifier = get_sentiment_model()



        # Confirmation que le modèle est prêt.
        print("Modèle sentiment chargé")



    # Protection contre les textes trop longs.
    #
    # Exemple :
    # MAX_TEXT_LENGTH = 1000
    #
    # Si un utilisateur envoie 5000 caractères,
    # seulement les 1000 premiers seront analysés.
    text = text[:MAX_TEXT_LENGTH]



    # Envoie le texte au modèle IA.
    #
    # Le modèle retourne une liste :
    #
    # [
    #   {
    #       "label": "positive",
    #       "score": 0.98
    #   }
    # ]
    result = classifier(text)



    # Récupère la classe prédite.
    #
    # Exemple :
    # positive
    # negative
    # neutral
    label = result[0]["label"]



    # Récupère le niveau de confiance du modèle.
    #
    # Exemple :
    # 0.98 signifie que le modèle est sûr à 98%.
    confidence = result[0]["score"]



    # Vérification de la confiance.
    #
    # Si le modèle a un score inférieur à 60%,
    # la prédiction est considérée comme incertaine.
    #
    # Exemple :
    # score = 0.45
    # Le modèle hésite.
    if confidence < 0.60:


        # On force la catégorie neutre.
        #
        # Cela évite de donner une mauvaise décision
        # quand le modèle n'est pas assez sûr.
        label = "neutral"



    # Retourne un dictionnaire JSON exploitable par FastAPI.
    return {


        # Sentiment détecté.
        "sentiment": label,


        # Score de confiance arrondi à 3 chiffres.
        #
        # Exemple :
        # 0.987654 devient 0.988
        "confidence": round(
            confidence,
            3
        )

    }