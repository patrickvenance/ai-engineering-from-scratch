# ================================================================================
# SPRINT PYTHON 28 JOURS – JOUR 02
# Concept : Opérations Arithmétiques, Logiques et Expressions
# ================================================================================

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# EXERCICE 1 : Application Directe
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
a = 17
b = 5

print(
    f"Addition : {a + b}\n"
    f"Soustraction : {a - b}\n"
    f"Multiplication : {a * b}\n"
    f"Division : {a / b}\n"
    f"Quotient entier : {a // b}\n"
    f"Reste : {a % b}\n"
    f"Puissance : {a ** b}"
)


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
#EXERCICE 2 : Problème Combiné
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
secondes = int(input("Nombre de secondes : "))

heures = secondes // 3600
minutes = (secondes % 3600) // 60
secondes_restantes = secondes % 60
plus_dune_heure = secondes > 3600

print(
    f"{secondes} secondes = {heures} h {minutes} min {secondes_restantes} s\n"
    f"Plus d'une heure ? {plus_dune_heure}"
)
