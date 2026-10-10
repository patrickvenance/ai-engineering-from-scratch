# Jour 02 - Opérations et Expressions

## Énoncés des Exercices

### Exercice 1 : Application Directe
> Avec `a = 17` et `b = 5`, affiche chaque résultat avec une *f-string*, exactement dans ce format :
> `Addition : 22`
> `Soustraction : 12`
> `Multiplication : 85`
> 'Division : 3.4`
> `Quotient entier : 3`
> `Reste : 2`
> `Puissance : 1419857`

### Exercice 2 : Problème Combiné
> Écris un programme qui demande un nombre total de secondes (entier). Le programme doit pouvoir le convertir en heures, en minutes et en secondes. Indique si la durée dépasse une heure. Avec 3725, la sortie finale doit être :
> `3725 secondes = 1 h 2 min 5 s`
> `Plus d'une heure ? True`

---

## 🛠️ Analyse du Refactoring

### Exercice 1
- **Code initial (Pydroid 3) :**
  ```python
  a = 17
  b = 5

  print(f"Addition : {a + b}")
  print(f"Soustraction : {a - b}")
  print(f"Multiplication : {a * b}")
  print(f"Division : {a / b}")
  print(f"Quotient entier : {a // b}")
  print(f"Reste : {a % b}")
  print(f"Puissance : {a ** b}")
  ```
  
- **Ce qui a été amélioré (version retenue dans main.py)**
- Simplification de l'affichage avec un seul `print()` et utilisation de `\n` pour l'alignement progressif des lignes dans la `f-string f"..."`.

### Exercice 2
- **Code initial (Pydroid 3) :**
  ```python
  secondes = int(input("Nombre de secondes : "))

  print(
      f"{secondes} secondes = {secondes // 3600} h {(secondes % 3600) // 60} min {((secondes % 3600) % 60)} s\n"
      f"Plus d'une heure ? {secondes > 3600}"
       )
  ```

- **Ce qui a été amélioré (version retenue dans main.py)**
- Création de variables intermédiaires aux noms explicites (`heures`, `minutes`, `reste_secondes`, `plus_dune_heure`).
- Séparation nette de la logique de calcul et de la logique d'affichage : le `print()` ne fait désormais plus que restituer le résultat.
- j'ai écrit la version complète avec les variables créées.

## 🔤 Tech English du jour
- **Operator** : opérateur. "The `+` operator adds two numbers."
- **Operand** : opérande. "In `3 + 4`, the operands are `3` and `4`."
- **Remainder** : reste. "The remainder of `17 divided by 5` is `2`."
- **Floor division** : division entière. "Floor division drops the decimal part."
- **Boolean expression** : expression booléenne. "A boolean expression evaluates to `True` or `False`."

 
 ## 💡 Notes & Apprentissages
- `//` donne le **quotient entier**.
- `%` donne le **reste** (**modulo**).
- Une **comparaison** (`>`, `==`, `=<`) renvoie `True` ou `False`.
- `=` **range** une valeur et `==` **compare**.

### 📋 Checklist du Jour 02 :
- [x] Distinguer les types de données (`int`, `str`, `float`, `bool`)
- [x] Maîtriser la conversion explicite de types (ex: `int(input())`)
- [x] Écrire des structures conditionnelles simples (`if`, `elif`, `else`)
- [x] Tester mon code avec différentes valeurs pour valider la logique
- [x] Rédiger le journal de bord et structurer le README sur GitHub
