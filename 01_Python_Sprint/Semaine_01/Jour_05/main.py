# ================================================================================
# SPRINT PYTHON 28 JOURS – JOUR 05
# Concept : Boucle `While`
# ================================================================================

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# EXERCICE 1 : Application Directe
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
n = int(input("Entrez l'entier : "))

compteur = n

while compteur >= 1:
    print(compteur)
    compteur -= 1

print("Décollage !")


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
#EXERCICE 2 : Problème Combiné
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
secret = 7
essais = 1
proposition = int(input("Devine le nombre : "))

while proposition != secret:
    if proposition < secret:
        print("Trop petit")
    else:
        print("Trop grand")
    proposition = int(input("Un autre nombre : "))
    essais += 1
print(f"Bravo ! Trouvé en {essais} essais")
