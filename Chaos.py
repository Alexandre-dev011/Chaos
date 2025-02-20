
import os
import random

# Dossier où les fichiers seront créés
dossier = "fichiers_lourds"
if not os.path.exists(dossier):
    os.makedirs(dossier)

# Nombre de fichiers à créer
nombre_fichiers = 10

# Taille de chaque fichier en Mo (exemple : 100 Mo)
taille_fichier_mo = 100

# Créer les fichiers
for i in range(nombre_fichiers):
    nom_fichier = os.path.join(dossier, f"fichier_lourd_{i+1}.txt")
    with open(nom_fichier, "wb") as f:
        # Écrire des données aléatoires pour remplir le fichier
        f.write(os.urandom(taille_fichier_mo * 1024 * 1024))  # Convertir en octets

print(f"{nombre_fichiers} fichiers de {taille_fichier_mo} Mo ont été créés dans '{dossier}'.")
