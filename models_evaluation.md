# Évaluation des modèles IA - Filtre Intelligent d'Avis E-commerce

## 1. Contexte du projet

Une plateforme e-commerce reçoit chaque jour plusieurs centaines d'avis clients. 
L'équipe support doit identifier rapidement :

- les clients satisfaits ;
- les clients mécontents ;
- les situations urgentes (litiges, fraudes, demandes de remboursement, problèmes graves).

L'objectif est de créer une API FastAPI capable de :

- analyser automatiquement le sentiment d'un avis ;
- classer l'avis en **Positive, Neutral ou Negative** ;
- détecter les avis nécessitant une intervention urgente.

---

# 2. Modèle candidat 1 (Modèle retenu)

## CardiffNLP Twitter XLM-RoBERTa Sentiment

### Nom sur Hugging Face

### Lien Hugging Face

https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment


## Informations techniques

| Critère | Valeur |
|---|---|
| Architecture | XLM-RoBERTa |
| Type de tâche | Analyse de sentiment |
| Langues supportées | Multilingue |
| Adaptation au français | Excellente |
| Taille approximative | ≈ 1 Go |
| Licence | MIT |
| Usage commercial | Autorisé |


## Sortie du modèle

Le modèle retourne directement trois catégories :
Positive
Neutral
Negative


## Avantages

- Très bonne compréhension du français.
- Supporte plusieurs langues.
- Retourne directement les trois classes demandées.
- Pas besoin d'une étape de conversion.
- Facile à utiliser avec la bibliothèque Hugging Face Transformers.
- Licence MIT compatible avec un projet commercial.


## Inconvénients

- Taille du modèle relativement importante.
- Consomme plus de mémoire qu'un modèle léger comme DistilBERT.


---

# 3. Modèle candidat 2

## NLPTown Multilingual Sentiment Analysis


### Nom sur Hugging Face
nlptown/bert-base-multilingual-uncased-sentiment


### Lien Hugging Face

https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment


## Informations techniques

| Critère | Valeur |
|---|---|
| Architecture | Multilingual BERT |
| Type de tâche | Analyse de sentiment |
| Langues supportées | Multilingue |
| Adaptation au français | Bonne |
| Taille approximative | ≈ 1 Go |
| Licence | Apache 2.0 |
| Usage commercial | Autorisé |


## Sortie du modèle

Le modèle retourne une note de satisfaction entre 1 et 5 étoiles :
1 star
2 stars
3 stars
4 stars
5 stars

Une conversion est nécessaire :

1-2 étoiles → Negative

3 étoiles → Neutral

4-5 étoiles → Positive



## Avantages

- Compatible avec plusieurs langues.
- Bonne performance sur les avis clients.
- Licence Apache 2.0 compatible avec un usage commercial.


## Inconvénients

- Ne retourne pas directement Positive/Neutral/Negative.
- Nécessite une logique supplémentaire de conversion.
- Moins pratique pour notre API.


---

# 4. Comparaison des deux modèles


| Critère | CardiffNLP XLM-R | NLPTown BERT |
|---|---|---|
| Français |  Excellent |  Bon |
| Multilingue | Oui | Oui |
| Taille | ≈ 1 Go | ≈ 1 Go |
| Licence | MIT | Apache 2.0 |
| Sortie | Positive / Neutral / Negative | 1 à 5 étoiles |
| Conversion nécessaire | Non | Oui |
| Facilité d'intégration | Très facile | Moyenne |


---

# 5. Choix final pour l'analyse sentiment


Le modèle choisi est :

cardiffnlp/twitter-xlm-roberta-base-sentiment



## Justification du choix

Ce modèle a été retenu car :

- il répond directement au besoin métier ;
- il classe automatiquement les avis en trois catégories ;
- il possède une excellente adaptation au français ;
- il est multilingue ;
- sa licence MIT autorise un usage commercial ;
- son intégration avec FastAPI et Transformers est simple.


---

# 6. Modèle utilisé pour la détection d'urgence


Pour identifier les avis urgents, nous utilisons un second modèle :

facebook/bart-large-mnli


## Type
 Zero-Shot Classification



## Fonctionnement

Le modèle compare l'avis client avec des catégories définies :

urgent customer complaint

normal customer review

Exemple :

Avis :


J'ai payé mais je n'ai jamais reçu mon produit, je veux porter plainte.



Résultat :

urgent customer complaint


Avis :

Le produit est arrivé avec un léger retard.


Résultat :

normal customer review



---

# 7. Architecture finale des modèles


| Fonction | Modèle utilisé |
|---|---|
| Analyse sentiment | CardiffNLP XLM-RoBERTa |
| Détection urgence | Facebook BART-MNLI |


---

# Conclusion

La combinaison de ces deux modèles permet de construire un filtre intelligent capable de :

- analyser automatiquement les avis clients ;
- détecter l'état émotionnel du client ;
- identifier les situations urgentes ;
- aider l'équipe support à prioriser les demandes importantes.

