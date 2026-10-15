# ============================================================================================================================================
# EXAMEN DE CONSOLIDATION : Boucles for & range
# Enoncé / Objectif : Combiner les notions : range(), if, le modulo, le compteur & l’accumulation.
# ============================================================================================================================================

compteur = 0
somme = 0

for nombre in range(11, 99):
    if nombre % 2 != 0:
        compteur += 1
        somme += nombre

print(
    f"Compteur = {compteur}\n"
    f"Somme = {somme}"
)
