# ================================================================================
# SPRINT PYTHON 28 JOURS – JOUR 04
# Concept : Boucle (for et range)
# ================================================================================

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# EXERCICE 1 : Application Directe
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
n = int(input("Entrez le nombre entier n : "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
#EXERCICE 2 : Problème Combiné
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
n = int(input("Entrez le nombre entier : "))
somme = 0
nombre_pairs = 0

for i in range(2, n + 1, 2):
    somme += i
    nombre_pairs += 1

print(
    f"Somme des nombres pairs : {somme}\n"
    f"Nombre de nombres pairs : {nombre_pairs}"
     )
