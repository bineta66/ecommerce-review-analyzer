# ecommerce-review-analyzer

## Description du projet

**AI E-commerce Review Analyzer** est un micro-service intelligent développé avec **FastAPI** permettant d'analyser automatiquement les avis clients d'une plateforme e-commerce.

Une plateforme de vente en ligne reçoit chaque jour plusieurs commentaires. L'équipe support doit identifier rapidement :

- les clients satisfaits ;
- les clients mécontents ;
- les cas urgents (litiges, fraudes, remboursements, problèmes graves).

L'objectif de cette API est d'automatiser cette tâche grâce à l'intelligence artificielle.

---

# Fonctionnalités

L'API permet de :

analyser automatiquement un avis client ;  
déterminer le sentiment du client ;  
classer l'avis en :

- Positive
- Neutral
- Negative

détecter les situations urgentes :

- fraude ;
- litige ;
- problème grave ;
- demande de remboursement.

---

#  Architecture du projet

```
ecommerce-review-analyzer/

│
├── app/
│   │
│   ├── main.py              # API FastAPI
│   ├── config.py            # Gestion variables environnement
│   ├── schemas.py           # Validation des données
│   ├── model.py             # Chargement modèle sentiment
│   ├── sentiment.py         # Analyse sentiment
│   ├── urgency_model.py     # Chargement modèle urgence
│   ├── urgency.py           # Détection urgence
│   └── __init__.py
│
├── models_evaluation.md     # Evaluation des modèles IA
├── requirements.txt         # Dépendances Python
├── .env.example             # Exemple configuration
├── .gitignore
└── README.md

```

---

# Modèles IA utilisés

## 1. Analyse du sentiment

### Modèle utilisé

```
cardiffnlp/twitter-xlm-roberta-base-sentiment
```

Lien :

https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment


### Rôle

Analyser l'opinion du client et retourner :

```
Positive
Neutral
Negative
```


### Pourquoi ce modèle ?

- Excellent support du français ;
- Multilingue ;
- Licence MIT ;
- Compatible avec un usage commercial ;
- Retour direct des trois catégories demandées.


---

## 2. Détection d'urgence

### Modèle utilisé

```
facebook/bart-large-mnli
```

Type :

```
Zero-Shot Classification
```


### Rôle

Déterminer si un avis correspond à :

```
urgent customer complaint

normal customer review
```


Exemple :

Avis :

```
J'ai payé mais je n'ai jamais reçu ma commande.
Je veux porter plainte.
```

Résultat :

```
urgent customer complaint
```


---

# Installation locale


## 1. Cloner le projet

```bash
git clone https://github.com/votre-utilisateur/ecommerce-review-analyzer.git
```

Entrer dans le projet :

```bash
cd ecommerce-review-analyzer
```

---

# 2. Créer un environnement virtuel


Linux :

```bash
python3 -m venv .venv
```


Activation :

```bash
source .venv/bin/activate
```


Windows :

```bash
.venv\Scripts\activate
```

---

# 3. Installer les dépendances


```bash
pip install -r requirements.txt
```


Les principales dépendances :

```
FastAPI
Uvicorn
Transformers
PyTorch
Python-dotenv
SentencePiece
```

---

# Configuration des variables d'environnement


Créer le fichier `.env` :

```bash
cp .env.example .env
```


Contenu :

```env
HF_TOKEN=

SENTIMENT_MODEL=cardiffnlp/twitter-xlm-roberta-base-sentiment

URGENCY_MODEL=facebook/bart-large-mnli

MAX_TEXT_LENGTH=1000

URGENCY_THRESHOLD=0.80
```


Le fichier `.env` ne doit jamais être envoyé sur GitHub.


---

# ▶Lancer le serveur


Depuis la racine du projet :

```bash
uvicorn app.main:app --reload
```


Si tout fonctionne :

```
INFO: Application startup complete.

Uvicorn running on http://127.0.0.1:8000
```

---

# Documentation Swagger


FastAPI génère automatiquement une documentation interactive.


Accès :

```
http://127.0.0.1:8000/docs
```

---

# Endpoint API


## POST /analyze-review


### URL

```
http://127.0.0.1:8000/analyze-review
```


### Body JSON


```json
{
    "text": "Excellent produit, livraison rapide"
}
```


---

# Exemple 1 : Avis positif


Requête :

```json
{
    "text": "Excellent produit, je recommande ce vendeur."
}
```


Réponse :

```json
{
    "sentiment": "positive",
    "sentiment_confidence": 0.98,
    "is_urgent": false,
    "urgency_category": "normal customer review",
    "urgency_confidence": 0.95
}
```

---

# Exemple 2 : Avis urgent


Requête :

```json
{
    "text": "Arnaque ! J'ai payé mais je n'ai jamais reçu ma commande. Je veux porter plainte."
}
```


Réponse :

```json
{
    "sentiment": "negative",
    "sentiment_confidence": 0.97,
    "is_urgent": true,
    "urgency_category": "urgent customer complaint",
    "urgency_confidence": 0.92
}
```

---

# Tester avec Postman


Créer une requête :

```
POST
http://127.0.0.1:8000/analyze-review
```


Ajouter dans Headers :

```
Content-Type : application/json
```


Dans Body :

```json
{
    "text":"Produit excellent, je recommande"
}
```

Cliquer sur **Send**.


---

#  Optimisation du modèle


Le projet utilise un mécanisme Singleton.

Le modèle IA est chargé une seule fois.


Sans optimisation :

```
Requête 1 → Chargement modèle

Requête 2 → Chargement modèle

Requête 3 → Chargement modèle
```


Avec Singleton :

```
Première requête → Chargement modèle

Autres requêtes → Modèle déjà en mémoire

voici le code qui gere ca 

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
```


Avantages :

- meilleure rapidité ;
- moins de consommation mémoire ;
- meilleure expérience utilisateur.

---

#  Sécurité et robustesse


Le projet possède :

Gestion des variables sensibles avec `.env` ;  
Validation des entrées avec Pydantic ;  
Limitation de taille des textes ;  
Gestion des erreurs HTTP ;  
Protection contre le rechargement inutile des modèles.


---

# Dépendances principales


```
fastapi
uvicorn
transformers
torch
python-dotenv
pydantic
sentencepiece
```


Installation :

```bash
pip install -r requirements.txt
```




---

# 👥 Atelier 33

## Le Filtre Intelligent et Sécurisé d'Avis E-commerce

### Technologies utilisées

- Python
- FastAPI
- Hugging Face Transformers
- PyTorch
- NLP
- Machine Learning


---

# Améliorations futures

Possibilités d'évolution :

- Ajouter une base PostgreSQL ;
- Créer un dashboard support ;
- Ajouter une authentification JWT ;
- Déployer l'API sur un serveur cloud ;
- Entraîner un modèle spécialisé sur les avis e-commerce locaux.


---

# Conclusion

Cette solution permet à une plateforme e-commerce de transformer automatiquement les avis clients en informations exploitables.

Grâce à l'intelligence artificielle, l'équipe support peut :

- comprendre rapidement la satisfaction client ;
- détecter les problèmes importants ;
- traiter les urgences en priorité.