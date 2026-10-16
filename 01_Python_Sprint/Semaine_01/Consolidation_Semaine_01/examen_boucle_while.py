# ============================================================================================================================================
# EXAMEN DE CONSOLIDATION : Boucle while
# Enoncé / Objectif : Combiner les notions : condition, compteur & accumulation.
# ============================================================================================================================================

nombre = 1
somme = 0
compteur = 0

while nombre <= 6:
    if nombre % 2 == 0:
        somme += nombre
        compteur += 1

    nombre += 1

print(somme)
print(compteur)
print(nombre)
