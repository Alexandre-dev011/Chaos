import os

# Nombre de fichiers à créer
nombre_fichiers = 50000  # Tu peux augmenter ce nombre si t'es chaud

# Dossier où les fichiers seront créés (ou sur le bureau si t'es flemmard)
dossier = "chaos_total"
if not os.path.exists(dossier):
    os.makedirs(dossier)

# Boucle pour créer les fichiers
for i in range(nombre_fichiers):
    nom_fichier = os.path.join(dossier, f"fichier_malin_{i+1}.txt")
    with open(nom_fichier, "w") as f:
        f.write(f"Fichier numéro {i+1} - Tu t'attendais pas à ça, hein ?")

print(f"Boom ! {nombre_fichiers} fichiers ont été créés dans '{dossier}'. Amuse-toi bien !")
