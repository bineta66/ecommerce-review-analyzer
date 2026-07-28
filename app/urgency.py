# Importe la fonction permettant de charger le modèle de détection
# d'urgence depuis le fichier urgency_model.py.
from .urgency_model import get_urgency_model

# Importe les constantes de configuration :
# - MAX_TEXT_LENGTH : longueur maximale du texte à analyser.
# - URGENCY_THRESHOLD : seuil minimal de confiance pour considérer
#   qu'un avis est réellement urgent.
from .config import (
    MAX_TEXT_LENGTH,
    URGENCY_THRESHOLD
)


# Fonction qui détecte si un texte est urgent ou non.
# Elle reçoit un texte (chaîne de caractères) en paramètre.
def detect_urgency(text):

    # Charge le modèle de classification Zero-Shot.
    # Ce modèle est capable de classer un texte
    # selon les catégories que nous lui fournissons.
    model = get_urgency_model()

    # Limite la longueur du texte afin d'éviter
    # d'envoyer un texte trop long au modèle.
    text = text[:MAX_TEXT_LENGTH]

    # Définition des catégories (labels) possibles.
    # Le modèle devra choisir celle qui correspond
    # le mieux au texte analysé.
    labels = [

        # Catégorie représentant une plainte urgente.
        "réclamation client urgente",

        # Catégorie représentant un avis normal.
        "avis client normal"

    ]

    # Analyse le texte avec le modèle Zero-Shot.
    #
    # Le modèle compare le texte avec les labels proposés
    # et calcule une probabilité pour chacun.
    result = model(
        text,
        candidate_labels=labels
    )

    # Exemple de résultat obtenu :
    #
    # {
    #     "sequence": "Mon colis n'est jamais arrivé.",
    #     "labels": [
    #         "urgent customer complaint",
    #         "normal customer review"
    #     ],
    #     "scores": [
    #         0.96,
    #         0.04
    #     ]
    # }

    # Récupère la catégorie ayant obtenu
    # le meilleur score.
    category = result["labels"][0]

    # Récupère le score de confiance
    # associé à cette catégorie.
    confidence = result["scores"][0]

    # Retourne les résultats sous forme
    # d'un dictionnaire.
    return {

        # Renvoie True uniquement si :
        # 1. la catégorie prédite est
        #    "urgent customer complaint"
        # ET
        # 2. le score est supérieur ou égal
        #    au seuil défini dans config.py.
        "is_urgent":
            category == "réclamation client urgente"
            and confidence >= URGENCY_THRESHOLD,

        # Nom de la catégorie prédite.
        "category":
            category,

        # Score de confiance arrondi
        # à trois décimales.
        "confidence": round(
            confidence,
            3
        )

    }