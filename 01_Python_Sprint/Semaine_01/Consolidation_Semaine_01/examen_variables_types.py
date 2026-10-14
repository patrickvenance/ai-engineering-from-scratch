# ============================================================================================================================================
# EXAMEN DE CONSOLIDATION : VARIABLES & TYPES
# Enoncé / Objectif : programme complet qui combine les notions du Jour_01 : variables, types, conversions, calculs, comparaisons et booléens.
# ============================================================================================================================================

prix = float(input("Entrez un prix : "))
quantite = int(input("Entrez une quantité : "))

prix_total = prix * quantite

superieur_a_50 = prix_total > 50
bool_0 = bool("0")

print(
    f"Prix = {prix} | Type = {type(prix)}\n"
    f"Quantité = {quantite} | Type = {type(quantite)}\n"
    f"Prix total = {prix_total} | Type = {type(prix_total)}\n"
    f"Total > 50 = {superieur_a_50}\n"
    f"Bool('0') = {bool_0}"
)
