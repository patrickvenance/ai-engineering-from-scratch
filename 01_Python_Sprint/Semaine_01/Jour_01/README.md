# Jour 01 - Variables et Types de données

## Énoncés des Exercices

### Exercice 1 : Application Directe
> Crée 4 variables : ton prénom (`str`), ton âge (`int`), ta taille en mètres (`float`), et un statut étudiant (`bool`). Affiche chaque variable avec son type en utilisant une *f-string* :
> `Prénom : Patrick | type : <class 'str'>`

### Exercice 2 : Problème combiné
> Écris un programme qui définit le nom d'un produit, son prix unitaire (`float`) et la quantité (`int`), puis calcule le total. Affiche le résultat sous cette forme :
> `Produit : Cahier | Total : 3 x 250.0 = 750.0 FCFA`

---

## 🛠️ Analyse du Refactoring

### Exercice 1
- **Code initial (Pydroid 3) :**
  ```python
  prenom = "Lefirst"
  age = 20
  taille = 1.74
  etudiant = True

  print("prenom :", f"{prenom}", "|", "type :", (type(prenom)))
  print("age :", f"{age} ans", "|", "type :", (type(age)))
  print("taille :", f"{taille} m", "|", "type :", (type(taille)))
  print("etudiant :", f"{etudiant}", "|", "type :", (type(etudiant)))
  ```
  
> **Ce qui a été amélioré (version retenue dans main.py)**
- Simplification de l'affichage avec une seule f-string pure au lieu de mélanger virgules et f-strings.
- Ajout des majuscules et accents pour une meilleure présentation.

### Exercice 2
- **Code initial (Pydroid 3) :**
  ```python
  produit = input("Quel est le nom de ce produit ?")
  prix_unitaire = float(input("Quel est le prix unitaire ?"))
  quantite = int(input("Quelle est la quantité ?"))
  total = quantite*prix_unitaire
  print(f" Produit : {produit}\n Total : {quantite} x {prix_unitaire} = {total} FCFA")
  ```

> **Ce qui a été amélioré (version retenue dans main.py)** 
- Prompts d'entrée plus concis avec un espace (: ) pour la clarté.
- Respect de la norme PEP 8 (espaces autour des opérateurs de calcul).

## 🔤 Tech English du jour
- **Variable** : Variable. "Assign a value to a variable."
- **Assignment** : Affectation. "The = operator performs the assignment."
- **String** : Chaîne de caractères. "A string is text enclosed in quotes."
- **Integer** : Nombre entier. "An integer has no decimal part."
- **Type casting** : Conversion de type. "Type casting converts a string into an integer."

 
 ## 💡 Notes & Apprentissages
- Utilisation des f-strings (**f"..."**) pour insérer des variables et des retours à la ligne (**\n**).
- Utilisation de la fonction intégrée **type()** pour vérifier le type dynamique d'une donnée.
- **input()** renvoie toujours du texte (**str**), il faut donc convertir explicitement avec **int()** ou **float()**.
- Respect de la convention de nommage **snake_case** pour les variables en Python.
