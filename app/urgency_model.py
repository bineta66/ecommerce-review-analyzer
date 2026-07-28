# Importe la fonction pipeline de la bibliothèque Transformers.
# Cette fonction permet de charger facilement un modèle
# d'intelligence artificielle prêt à être utilisé.
from transformers import pipeline

# Importe le nom du modèle de détection d'urgence
# défini dans le fichier config.py.
# Exemple :
# URGENCY_MODEL = "facebook/bart-large-mnli"
from .config import URGENCY_MODEL


# Variable globale qui contiendra le pipeline Hugging Face.
# Au démarrage, aucun modèle n'est chargé.
urgency_classifier = None


# Fonction qui charge et retourne le modèle de détection d'urgence.
def get_urgency_model():

    # Indique que l'on souhaite utiliser la variable globale
    # urgency_classifier et non créer une variable locale.
    global urgency_classifier

    # Vérifie si le modèle est déjà chargé.
    # Si la variable vaut None, cela signifie que
    # le modèle n'a jamais été chargé.
    if urgency_classifier is None:

        # Message affiché dans le terminal pour informer
        # que le chargement du modèle commence.
        print("Chargement modèle urgence...")

        # Création du pipeline Hugging Face.
        urgency_classifier = pipeline(

            # Type de tâche à réaliser.
            # Le modèle devra choisir le label
            # qui correspond le mieux au texte fourni.
            task="zero-shot-classification",

            # Nom du modèle à télécharger et charger.
            # Exemple : facebook/bart-large-mnli
            model=URGENCY_MODEL

        )

        # Message indiquant que le modèle est maintenant
        # chargé en mémoire et prêt à être utilisé.
        print("Modèle urgence chargé")

    # Retourne le pipeline chargé.
    # Si le modèle était déjà en mémoire,
    # cette ligne le renvoie directement sans
    # effectuer un nouveau chargement.
    return urgency_classifier