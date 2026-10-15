# ===========================================================================================================================
# EXAMEN DE CONSOLIDATION : Opérateurs & Expressions
# Enoncé / Objectif : combiner les opérateurs arithmétiques, les affectations, les comparaisons et les opérateurs logiques.
# ===========================================================================================================================

prix_unitaire = 12
quantite = 5
budget = 50

prix_total = prix_unitaire * quantite
reste = 0
reste += prix_total % 7
comparaison_1 = prix_total <= budget
comparaison_2 = prix_total > 40 and reste != 0

print(
    f"Prix total = {prix_total}\n"
    f"Reste = {reste}\n"
    f"Comparaison 1 = {comparaison_1}\n"
    f"Comparaison 2 = {comparaison_2}"
)
