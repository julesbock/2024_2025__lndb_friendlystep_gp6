import matplotlib.pyplot as plt
import numpy as np
import os
import glob
import datetime, calendar
def save_graph(filename):

    # Enregistrer le graphique
    plt.tight_layout()

    # Assurez-vous que le dossier 'images' existe
    images_dir = os.path.join(os.path.dirname(__file__), 'temporary', 'brouillon_adrien', 'main', 'static', 'images')
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    # Vider le dossier 'images'


    # Enregistrer le graphique dans le dossier 'images'
    plt.savefig(os.path.join(images_dir, filename))
    print(f"Graphique enregistré à : {os.path.abspath(os.path.join(images_dir, filename))}")
    
def create_x_days_graph(the_data_label, list_of_the_data_to_graph, number_of_days):
    labels = []
    today = datetime.datetime.now()
    day = today.day
    month = str(today.month)
    for i in range(number_of_days):
        labels.append(f"{i+1} {month}")

    # Création de la figure et de l'axe
    fig, ax1 = plt.subplots()

    # Tracer les barres pour les pas sur l'axe principal (ax1)
    ax1.bar(labels, list_of_the_data_to_graph, color='skyblue', label=the_data_label, alpha=0.7)
    ax1.set_xlabel('Jours')
    ax1.set_ylabel(the_data_label, color='skyblue')
    # Ajouter un titre
    return fig, ax1
    
    
def create_seven_days_graph(the_data_label, the_data_to_graph):
    fig, ax1 = create_x_days_graph(the_data_label, the_data_to_graph, 7)
    # Ajouter un titre
    plt.title('7 derniers jours')
    save_graph("seven_days_graph.png")
    
def create_month_graph(the_data_label, list_of_the_data_to_graph):
    today = datetime.datetime.now()
    number_of_days_in_month = calendar.monthrange(today.year, today.month)[1]
    fig, ax1 = create_x_days_graph(the_data_label, list_of_the_data_to_graph, number_of_days_in_month)
    # Ajouter un titre
    plt.title('Ce mois-ci')
    save_graph("month_graph.png")
    
list_of_the_data_to_graph=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
the_data_label="test"
create_month_graph(the_data_label, list_of_the_data_to_graph)




# Afficher le graphique
plt.show()