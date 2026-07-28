# Importe le module os de Python.
# Il permet d'interagir avec les variables d'environnement
# du système et de récupérer les valeurs du fichier .env.
import os


# Importe la fonction load_dotenv depuis la bibliothèque python-dotenv.
# Elle permet de charger automatiquement les variables définies
# dans le fichier .env.
from dotenv import load_dotenv



# Charge les variables du fichier .env dans l'environnement Python.
#
# Exemple de fichier .env :
#
# SENTIMENT_MODEL=cardiffnlp/twitter-xlm-roberta-base-sentiment
# URGENCY_MODEL=facebook/bart-large-mnli
# MAX_TEXT_LENGTH=1000
# URGENCY_THRESHOLD=0.80
#
load_dotenv()



# -------------------------------------------------------
# Configuration du modèle de sentiment
# -------------------------------------------------------

# Récupère le nom du modèle Hugging Face utilisé
# pour analyser le sentiment.
#
# Exemple :
# SENTIMENT_MODEL=
# "cardiffnlp/twitter-xlm-roberta-base-sentiment"
#
SENTIMENT_MODEL = os.getenv(
    "SENTIMENT_MODEL"
)



# -------------------------------------------------------
# Configuration du modèle de détection d'urgence
# -------------------------------------------------------

# Récupère le nom du modèle Hugging Face utilisé
# pour détecter si un avis est urgent.
#
# Exemple :
# URGENCY_MODEL="facebook/bart-large-mnli"
#
URGENCY_MODEL = os.getenv(
    "URGENCY_MODEL"
)





# Récupère la longueur maximale d'un avis.
#
# os.getenv() retourne toujours une chaîne de caractères.
#
# Exemple :
# "1000"
#
# On utilise donc int() pour convertir en nombre entier :
#
# "1000"  --> 1000
#
# Si MAX_TEXT_LENGTH n'existe pas dans le fichier .env,
# la valeur par défaut sera 1000 caractères.
#
MAX_TEXT_LENGTH = int(
    os.getenv(
        "MAX_TEXT_LENGTH",
        1000
    )
)



# -------------------------------------------------------
# Seuil de confiance pour l'urgence
# -------------------------------------------------------

# Définit le niveau minimum de confiance nécessaire
# pour considérer un avis comme urgent.
#
# Exemple :
#
# Si le modèle retourne :
#
# confidence = 0.90
#
# et :
#
# URGENCY_THRESHOLD = 0.80
#
# alors l'avis sera considéré comme urgent.
#
# La fonction float() transforme :
#
# "0.80" --> 0.80
#
# La valeur par défaut est 0.80.
#
URGENCY_THRESHOLD = float(
    os.getenv(
        "URGENCY_THRESHOLD",
        0.80
    )
)