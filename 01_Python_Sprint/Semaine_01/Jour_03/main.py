
# ================================================================================
# SPRINT PYTHON 28 JOURS – JOUR 03
# Concept : Les conditions (if, elif, else)
# ================================================================================

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# EXERCICE 1 : Application Directe
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
note = int(input("La note sur 20 : "))

if note < 10:
    mention = "Insuffisant"
elif note <= 11:
    mention = "Passable"
elif note <= 13:
    mention = "Assez bien"
elif note <= 15:
    mention = "Bien"
else:
    mention = "Très bien"

print(f"Mention : {mention}")


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
#EXERCICE 2 : Problème Combiné
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
annee = int(input("Entrez l'année : "))

est_bissextile = (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0

if est_bissextile:
    print(f"{annee} est bissextile")
else:
    print(f"{annee} n'est pas bissextile")
