import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
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
    if number_of_days < 10:
        for i in range(number_of_days):
            date = today - datetime.timedelta(days=number_of_days - 1 - i)
            day = date.day
            if day == 1:
                extend = 'st'
            elif day == 2:
                extend = 'nd'
            elif day == 3:
                extend = 'rd'
            else:
                extend = 'th'
            # Format spécial pour le 1er du mois
            labels.append(f"{day}{extend} {calendar.month_name[date.month]} {date.year}")
            
    else : 
        for i in range (number_of_days):
            date = today - datetime.timedelta(days=number_of_days - 1 - i)
            day = date.day
            month = date.month
            labels.append(
                f"{'0' if (day) < 10 else ''}{day}"
                f"/{'0' if int(month) < 10 else ''}{month}"
            )     

    print(labels)
    plt.clf()

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
    create_x_days_graph(the_data_label, the_data_to_graph, 7)
    # Ajouter un titre
    plt.title('7 derniers jours')
    save_graph("seven_days_graph.png")
    
def create_month_graph(the_data_label, the_data_to_graph):
    today = datetime.datetime.now()
    number_of_days_in_month = today.day

    create_x_days_graph(the_data_label, the_data_to_graph, number_of_days_in_month)
    # Ajouter un titre
    plt.title('Ce mois-ci')
    save_graph("month_graph.png")
    
def create_year_graph(the_data_label, list_of_the_data_to_graph):
    labels = []
    today = datetime.datetime.now()
    current_month = today.month
    print(current_month)
    for i in range(current_month): # 12 mois
        print(i)
        labels.append(calendar.month_name[i+1])
    print(labels)
    print(list_of_the_data_to_graph)
    # Création de la figure et de l'axe
    plt.clf()
    fig, ax1 = plt.subplots()

    # Tracer les barres pour les pas sur l'axe principal (ax1)
    ax1.bar(labels, list_of_the_data_to_graph, color='skyblue', label=the_data_label, alpha=0.7, width=0.1)
    ax1.set_xlabel('Mois')
    ax1.set_ylabel(the_data_label)
    # Ajouter un titre
    plt.title('Cette année')
    save_graph("year_graph.png")

def category_name_convert_to_label(category):
    category_labels = {
        "step_data": "Pas",
        "distance_data": "Distance (km)",
        "calories_data": "Calories (kcal)",
        "floors_data": "Etages montés",
        "sleep_duration_data": "Durée de sommeil (minutes)",
    }
    
    # Si la catégorie existe dans le dictionnaire, on retourne son label
    return category_labels.get(category)

def create_tournament_graphic(all_player_data, category):
    label = category_name_convert_to_label(category)
    players = list(all_player_data.keys())
    print(players)
    players.reverse()
    scores = list(all_player_data.values())
    print(scores)

    scores.reverse()
    print(scores)
    print(players)
    # Créer un graphique à barres horizontal
    plt.clf()

    plt.barh(players, scores, color="skyblue", height=0.05)
    
    # Ajouter un titre et des labels
    plt.xlabel(label)
    plt.ylabel("Participants")
    save_graph('tournament_graph')
    
def save_graph(filename):
    print(filename)
    # Enregistrer le graphique
    plt.tight_layout()

    # Assurez-vous que le dossier 'images' existe
    images_dir = os.path.join(os.path.dirname(__file__), 'static', 'images')
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)
    path=os.path.join(images_dir, filename)
    # Vider le dossier 'images'
    if os.path.exists(path):
        os.remove(path)

    # Enregistrer le graphique dans le dossier 'images'
    plt.savefig(os.path.join(images_dir, filename))
    print(f"Graphique enregistré à : {os.path.abspath(os.path.join(images_dir, filename))}")

# Afficher le graphique
# plt.show()