# Jour 03 - Conditions (if, elif, else)

## Énoncés des Exercices

### Exercice 1 : Application Directe
> Demande une note sur 20 (entier) et affiche la mention :
>
> | Note | Mention |
> | :--- | :--- |
> | moins de 10 | Insuffisant |
> | de 10 à 11 | Passable |
> | de 12 à 13 | Assez bien |
> | de 14 à 15 | Bien |
> | 16 et plus | Très bien |
>
> Avec 15, la sortie finale doit être :
> `Mention : Bien`  
> Avec 8 :  
> `Mention : Insuffisant`

### Exercice 2 : Problème combiné
> Demande une année (entier) et indique si elle est bissextile.  
> **Règle :** une année est bissextile si elle est divisible par 4 et pas par 100, ou si elle est divisible par 400.  
> **Résultats attendus :**
> `2024 est bissextile`  
> `1900 n'est pas bissextile`  
> `2000 est bissextile`  
> `2023 n'est pas bissextile`

---

## 🛠️ Analyse du Refactoring

### Exercice 1
- **Code initial (Pydroid 3) :**
  ```python
  note = int(input("La note sur 20 : "))
  moins_de_10 = "Insuffisant"
  de_10_a_11 = "Passable"
  de_12_a_13 = "Assez bien"
  de_14_a_15 = "Bien"
  plus_ou_16 = "Très bien"

  if note < 10:
      print(f"Mention : {moins_de_10}")
  elif note <= 11:
      print(f"Mention : {de_10_a_11}")
  elif note <= 13:
      print(f"Mention : {de_12_a_13}")
  elif note <= 15:
      print(f"Mention : {de_14_a_15}")
  else:
      print(f"Mention : {plus_ou_16}")
  ```
  
- **Ce qui a été amélioré (version retenue dans main.py)**
- Nommage explicite : Remplacement des 5 variables de mentions par une seule variable dynamique mention.
- Factorisation de l'affichage : Un seul print() à la fin. Si le format d'affichage change, une seule ligne est à modifier au lieu de cinq.
- Principe fondamental : Décider de la valeur d'abord dans les structures conditionnelles, afficher le résultat ensuite.

### Exercice 2
- **Code initial (Pydroid 3) :**
  ```python
  annee = int(input("Entrez l'année : "))

  reste_1 = annee % 4
  reste_2 = annee % 100
  reste_3 = annee % 400

  if reste_2 == 0 and reste_3 != 0:
      sortie = "n'est pas bissextile"
  elif reste_1 == 0:
      sortie = "est bissextile"
  else:
      sortie = "n'est pas bissextile"

  print(f"{annee} {sortie}")
  ```

- **Ce qui a été amélioré (version retenue dans main.py)**
- Simplification de la logique : Remplacement des calculs de restes intermédiaires (reste_1, reste_2, etc.) par une expression booléenne directe est_bissextile.
- Clarté du code : Le **if est_bissextile:** se lit désormais comme une phrase en langage naturel.

## 🔤 Tech English du jour
- **Condition** : condition. "The if statement checks a condition."
- **Branch** : branche. "The program takes the else branch."
- **Indentation** : indentation. "Python uses indentation to group code."
- **Statement** : instruction. "An if statement controls the flow."
- **Nested** : imbriqué. "A nested if is an if inside another if."

 
## 💡 Notes & Apprentissages
- Ordre d'évaluation : Python teste les branches dans l'ordre et s'arrête dès qu'il rencontre la première condition vraie (**True**).
- Logique séquentielle : Un bloc **elif** n'a pas besoin de retester ce que les branches précédentes ont déjà éliminé (ex: si on arrive au **elif note <= 11**, on sait déjà que la note est **≥** 10).
- Syntaxe stricte : Les deux-points **:** en fin de ligne conditionnelle et l'**indentation de 4 espaces** sont obligatoires en Python.
