import matplotlib.pyplot as plt
import numpy as np

# Données pour les pas et les calories
labels = ['Jour 1', 'Jour 2', 'Jour 3', 'Jour 4', 'Jour 5']
pas = [15000, 12000, 18000, 16000, 14000]  # En pas
calories = [300, 250, 350, 300, 275]  # En calories

# Création de la figure et de l'axe
fig, ax1 = plt.subplots()

# Tracer les barres pour les pas sur l'axe principal (ax1)
ax1.bar(labels, pas, color='skyblue', label='Pas', alpha=0.7)
ax1.set_xlabel('Jours')
ax1.set_ylabel('Pas', color='skyblue')
ax1.tick_params(axis='y', labelcolor='skyblue')

# Créer un second axe pour les calories
ax2 = ax1.twinx()

# Tracer les barres pour les calories sur le second axe (ax2)
ax2.bar(labels, calories, color='orange', label='Calories', alpha=0.7)
ax2.set_ylabel('Calories', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

# Ajouter un titre
plt.title('Comparaison des Pas et Calories par Jour')

# Afficher le graphique
plt.tight_layout()
plt.show()