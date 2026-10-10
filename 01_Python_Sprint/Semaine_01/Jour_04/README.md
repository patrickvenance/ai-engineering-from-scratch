# Jour 04 - Boucle (for et range)

## Énoncés des Exercices

### Exercice 1 : Application Directe
> Demande un entier n et affiche sa table de multiplication de 1 à 10.  
> Avec 7, la sortie commence ainsi et se termine à la ligne 10 :  
> `7 x 1 = 7`  
> `7 x 2 = 14`  
> `...`  
> `7 x 10 = 70`

### Exercice 2 : Problème combiné
> Demande un entier n. De 1 à n inclus, calcule :  
> - la somme des nombres pairs  
> - le nombre de nombres pairs  
> Avec 10 :  
> `Somme des nombres pairs : 30`  
> `Nombre de nombres pairs : 5`  
> **Contrainte** : un seul `print()` final pour les 2 lignes, calculs faits avant l'affichage.

---

## 🛠️ Analyse du Refactoring

### Exercice 1
- **Code initial (Pydroid 3) :**
  ```python
  n = int(input("Entrez le nombre entier n : "))

  for i in range(1, 11):
      print(f"{n} x {i} = {n * i}")
  ```

  
- **Ce qui a été amélioré (version retenue dans main.py)**
- Conservation de la version épurée validée dans **main.py**

### Exercice 2
- **Code initial (Pydroid 3) :**
  ```python
     n = int(input("Entrez le nombre entier : "))
    somme = 0
    nombre_pairs = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            somme = somme + i
            nombre_pairs = nombre_pairs + (i % 2 == 0)

     print(
             f"Somme des nombres pairs :     {somme}\n"
             f"Nombre de nombres pairs : {nombre_pairs}"
             )
  ```

- **Ce qui a été amélioré (version retenue dans main.py)**
- Utilisation de `range(2, n + 1, 2)` pour cibler directement les pairs.
- Utilisation des opérateurs d'accumulation `+=` (`somme += i` et `nombre_pairs += 1`).
- Suppression de la condition `if`, ce qui simplifie la lecture et divise les tours de boucle par deux.

## 🔤 Tech English du jour
- **Loop** : boucle. "A `for` loop repeats a block of code."
- **Iteration** : itération (un tour de boucle). "The loop runs five iterations."
- **Range** : plage de valeurs. "`range(1, 4)` generates numbers from `1 to 3`."
- **Counter** : compteur. "The counter increases at each iteration."
- **Accumulator** : accumulateur. "The accumulator stores the running total."

 
## 💡 Notes & Apprentissages
- **range(début, fin, pas)** : la fin est exclue, d'où le `n + 1` pour inclure `n`
- Un **accumulateur** (`somme += i`) et un compteur (`nombre += 1`) se préparent toujours avant la boucle
- Un `if` dans une boucle teste le nombre en cours (`i`), pas un compteur
- Ne jamais replacer l'initialisation des variables (`= 0`) à l'intérieur de la boucle sous peine de perdre le total à chaque tour.

### 📋 Checklist du Jour 04 :
Dans la version finale :
- [x] Aucune valeur en dur : plus de `if n == 10`, tout dépend de `n`
- [x] Format identique à l'énoncé
- [x] Noms clairs : `somme`, `nombre_pairs`, `i`
- [x] Calculs avant le print : tout est calculé dans la boucle
- [x] Variables initialisées avant la boucle

Pièges identifiés en chemin :
- [x] Attention aux valeurs en dur (piège de débutant)
- [x] Rigueur sur le formatage des espaces et des chaînes (`\n`, `f-strings`)
- [x] Ne pas réinitialiser les compteurs à chaque itération
