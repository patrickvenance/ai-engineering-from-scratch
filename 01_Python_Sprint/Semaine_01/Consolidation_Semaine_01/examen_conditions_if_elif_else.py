# ============================================================================================================================================
# EXAMEN DE CONSOLIDATION : Conditions (if, elif & else)
# Enoncé / Objectif : Réunir les notions :  if, elif, else, and, or & les comparaisons
# ============================================================================================================================================

note = int(input("Entrez la note : "))

if note < 0 or note > 20:
    appreciation = "Note invalide"
elif note >= 16:
    appreciation = "Très bien"
elif note >= 10:
    appreciation = "Admis"
else:
    appreciation = "Échec"

print(f"Appréciation = {appreciation}")
