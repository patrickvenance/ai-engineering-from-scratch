# ================================================================================
# SPRINT PYTHON 28 JOURS – JOUR 01
# Concept : Les Variables et Types de Données (int, float, str, bool)
# ================================================================================

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# EXERCICE 1 : Application Directe
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
prenom = "Lefirst"
age = 20
taille = 1.74
etudiant = True

print(f"Prénom : {prenom} | type : {type(prenom)}")
print(f"Âge : {age} ans | type : {type(age)}")
print(f"Taille : {taille} m | type : {type(taille)}")
print(f"Étudiant : {etudiant} | type : {type(etudiant)}")


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
EXERCICE 2 : Problème Combiné
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
produit = input("Nom du produit : ")
prix_unitaire = float(input("Prix unitaire : ")
quantite = int(input("Quantité : "))

total = prix_unitaire * quantite

print(f"Produit : {produit}\nTotal : {quantite} x {prix_unitaire} = {total} FCFA")
