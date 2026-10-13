# Jour 05 - Boucle `While`

## Énoncés des Exercices

### Exercice 1 : Application Directe
> Demande un entier `n` (supposé supérieur ou égal à 1). Avec une boucle `while` (pas `for`), fais un compte à rebours de `n` jusqu'à `1`, puis affiche `Décollage !`.
> Avec `3`, la sortie finale est :  
> `3`  
> `2`  
> `1`  
> `Décollage !`
> Avec `1` :  
> `1`  
> `Décollage !`

### Exercice 2 : Problème combiné
> Écris un jeu « Devine le nombre ».
> Le nombre secret est 7, rangé dans une variable `secret`. Le programme demande un nombre tant que le joueur n'a pas trouvé, et compte les essais :
> - si le nombre proposé est trop petit, afficher `Trop petit`
> - s'il est trop grand, afficher `Trop grand`
> - quand le joueur trouve : `Bravo ! Trouvé en X essais`
> Avec les propositions `3`, `9`, `7`, la fin de l'écran doit être :  
> `Trop petit`  
> `Trop grand`  
> `Bravo ! Trouvé en 3 essais`
> Avec la proposition `7` du premier coup :  
> `Bravo ! Trouvé en 1 essais`

> **Contrainte** : tout nom de variable clair, et le message final affiché après la boucle, avec un seul `print()`.

---

## 🛠️ Analyse du Refactoring

### Exercice 1
- **Code initial (Pydroid 3) :**
  ```python
  n = int(input("Entrez l'entier : "))

  compteur = n

  while compteur >= 1:
      print(compteur)
      compteur -= 1

  print("Décollage !")
  ```

  
- **Ce qui a été amélioré (version retenue dans main.py)**
- Implantation propre du compteur initialisé avec la valeur de départ.
- Utilisation de l'opérateur de décrémentation `-= 1` pour assurer la condition de sortie et éviter la boucle infinie.

### Exercice 2
- **Code initial (Pydroid 3) :**
  
```Python
secret = 7
essais = 1
proposition = int(input("Devine le nombre : "))

if proposition < secret:
        print("Trop petit")
elif proposition > secret:
    print("Trop grand")

while proposition < secret or proposition > secret:
    proposition = int(input("Un autre nombre : "))
    essais += 1
    if proposition < secret:
        print("Trop petit")
    elif proposition > secret:
        print("Trop grand")
else:     
    print(f"Bravo ! Trouvé en {essais} essais")

  ```

- **Ce qui a été amélioré (version retenue dans main.py)**
- Suppression de la duplication du code de test en dehors de la boucle.
- Utilisation de la condition simple `proposition != secret` dans le `while` au lieu d'un `or` lourd.
- Suppression du bloc `else` inutile associé au `while` au profit d'un affichage direct après la boucle.
- Initialisation correcte des variables de configuration avant l'appel des entrées utilisateur.

## 🔤 Tech English du jour
- **Infinite loop** : boucle infinie. *"A missing increment causes an infinite loop."*
- **Loop condition** : condition de boucle. *"The loop condition is checked before each iteration."*
- **Increment** : incrémenter (ajouter 1). *"We increment the counter at each turn."*
- **To terminate** : se terminer. *"The loop terminates when the condition becomes false."*
- **Input validation** : validation de saisie. *"A while loop is useful for input validation."*

 
## 💡 Notes & Apprentissages
- `while` répète **tant qu'une condition est vraie** : on l'utilise quand le nombre de tours est inconnu
- Trois éléments obligatoires : préparer la variable **avant**, une condition, la changer **dans** la boucle
- Sans modification de la variable dans la boucle : c'est la boucle infinie.
- On peut imbriquer des `if`, `for`, `and`, `or` et `not` dans un `while`
- Attention au niveau d'indentation : une ligne exécutée au mauvais endroit (comme un compteur ou une réinitialisation) peut bloquer ou casser toute la logique.
- Ne pas mettre dans une branche `else` des lignes qui doivent s'exécuter à chaque tour : le compteur n'avancera plus et la boucle ne s'arrêtera jamais.

### 📋 Checklist du Jour 05 :
Dans la version finale :
- [x] Aucune valeur en dur : les comparaisons utilisent `secret`
- [x] Noms clairs : `secret`, `essais`, `proposition`
- [x] Calculs avant le `print` : tout est géré dans la boucle
- [x] Le print de victoire s'exécute bien après la sortie de la boucle
- [x] Format identique à l'énoncé : `Bravo ! Trouvé en 3 essais`

Pièges identifiés en chemin :
- [x] Éviter la duplication inutile de code (les `if`/`elif` répétés)
- [x] Ne pas utiliser de `else` inutile sur une boucle `while`
- [x] Bien placer *l'incrémentation* des essais pour ne pas fausser le score final
