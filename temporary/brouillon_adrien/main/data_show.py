import matplotlib.pyplot as plt
import numpy as np
import os
import glob
import datetime
import calendar
# Données pour les pas et les calories
def create_x_days_graph(the_data_label, list_of_the_data_to_graph, number_of_days):
    labels = []
    today = datetime.datetime.now()
    day = today.day
    month = today.month
    month_name = calendar.month_name[today.month]
    if number_of_days < 10:
        for i in range(1, number_of_days+1):
            labels.append(f"{day-number_of_days+i} {month_name}")
    else:
        for i in range(1, number_of_days+1):
            labels.append(
                f"{'0' if (day - number_of_days + i) < 10 else ''}{day - number_of_days + i}"
                f"/{'0' if int(month) < 10 else ''}{month}"
            )

    # Création de la figure et de l'axe
    fig, ax1 = plt.subplots(figsize=(11.5, 5.75))

    # Tracer les barres pour les pas sur l'axe principal (ax1)
    if number_of_days<10:
        the_width_given = 1/number_of_days
    else:
        the_width_given = 1/(number_of_days//9)
        
    ax1.bar(labels, 
            list_of_the_data_to_graph, 
            color='skyblue',
            label=the_data_label, 
            alpha=0.7, 
            width=the_width_given)
    ax1.tick_params(axis='x', labelrotation=45)  # Optionnel : incliner les labels pour une meilleure lisibilité
    ax1.set_xlabel('Jours')
    ax1.set_ylabel(the_data_label)
    # Ajouter un titre
    return fig, ax1
    
    
def create_seven_days_graph(the_data_label, the_data_to_graph):
    fig, ax1 = create_x_days_graph(the_data_label, the_data_to_graph, 7)
    # Ajouter un titre
    plt.title('7 derniers jours')
    save_graph("seven_days_graph.png")
    
def create_month_graph(the_data_label, the_data_to_graph):
    today = datetime.datetime.now()
    number_of_days_in_month = today.day

    fig, ax1 = create_x_days_graph(the_data_label, the_data_to_graph, number_of_days_in_month)
    # Ajouter un titre
    plt.title('Ce mois-ci')
    save_graph("month_graph.png")
    
def create_year_graph(the_data_label, list_of_the_data_to_graph):
    labels = []

    for i in range(2): # 12 mois
        labels.append(calendar.month_name[i + 1])
    
    # Création de la figure et de l'axe
    fig, ax1 = plt.subplots()

    # Tracer les barres pour les pas sur l'axe principal (ax1)
    ax1.bar(labels, list_of_the_data_to_graph, color='skyblue', label=the_data_label, alpha=0.7, width=0.1)
    ax1.set_xlabel('Mois')
    ax1.set_ylabel(the_data_label)
    # Ajouter un titre
    plt.title('Cette année')
    save_graph("year_graph.png")


def save_graph(filename):

    # Enregistrer le graphique
    plt.tight_layout()

    # Assurez-vous que le dossier 'images' existe
    images_dir = os.path.join(os.path.dirname(__file__), 'static', 'images')
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    # Vider le dossier 'images'


    # Enregistrer le graphique dans le dossier 'images'
    plt.savefig(os.path.join(images_dir, filename))
    print(f"Graphique enregistré à : {os.path.abspath(os.path.join(images_dir, filename))}")

# Afficher le graphique
# plt.show()