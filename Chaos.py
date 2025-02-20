
import os
import random

# Dossier où les fichiers seront créés
dossier = "apocalypse_stockage"
if not os.path.exists(dossier):
    os.makedirs(dossier)

# Nombre de fichiers à créer
nombre_fichiers = 2 # Tu peux en mettre plus si t'es chaud

# Taille de chaque fichier en Go (oui, en gigaoctets !)
taille_fichier_go = 1  # 1 Go par fichier, mais tu peux augmenter

# Créer les fichiers
for i in range(nombre_fichiers):
    nom_fichier = os.path.join(dossier, f"monstre_{i+1}.bin")
    with open(nom_fichier, "wb") as f:
        # Remplir le fichier avec des données aléatoires
        f.write(os.urandom(taille_fichier_go * 1024 * 1024 * 1024))  # Convertir en octets

print(f"{nombre_fichiers} fichiers de {taille_fichier_go} Go ont été créés dans '{dossier}'. Ton stockage va souffrir !")
