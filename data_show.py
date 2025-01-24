import matplotlib.pyplot as plt
import numpy as np
import os
import glob

# Données pour les pas et les calories
labels = ['Jour 1', 'Jour 2', 'Jour 3', 'Jour 4', 'Jour 5', 'Jour 6', 'Jour 7']
pas = [15000, 12000, 18000, 16000, 14000, 20000, 30000]  # En pas
calories = [300, 250, 350, 300, 275]  # En calories

# Création de la figure et de l'axe
fig, ax1 = plt.subplots()

# Tracer les barres pour les pas sur l'axe principal (ax1)
ax1.bar(labels, pas, color='skyblue', label='Pas', alpha=0.7)
ax1.set_xlabel('Jours')
ax1.set_ylabel('Pas', color='skyblue')
ax1.tick_params(axis='y', labelcolor='skyblue')

# Ajouter un titre
plt.title('7 derniers jours')

# Enregistrer le graphique
plt.tight_layout()

# Assurez-vous que le dossier 'images' existe
images_dir = 'images'
if not os.path.exists(images_dir):
    os.makedirs(images_dir)

# Vider le dossier 'images'
files = glob.glob(os.path.join(images_dir, '*'))
for f in files:
    os.remove(f)

# Enregistrer le graphique dans le dossier 'images'
plt.savefig(os.path.join(images_dir, 'graphique.png'))
print(f"Graphique enregistré à : {os.path.abspath(os.path.join(images_dir, 'graphique.png'))}")

# Afficher le graphique
plt.show()