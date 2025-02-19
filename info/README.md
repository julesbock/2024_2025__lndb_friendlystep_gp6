Créer une IHM   qui permet d'accéder aux données de l'utilisateur et le comparer à d'autres utilsateurs (de data sur internet) et à d'autres users plus precis (amis, a travers un echange ..)



<!-- Notes sur le projet 2 :
⦁	créer une application de comparaison de données de santé entre 2 utilisateurs
⦁	Des différentes données:
I.	Des données de la qualité du sommeil/de sa durée
II.	du nombres de pas
III.	kilomètres parcourus
IV.	du nombre de kcal brulées
V.	rythme cardiaque au repos
Comparaison entre les différents utilisateurs de l'application    -->












Quand on lance -> une page -> sur tout l'écran, sortir page avec echap
Page : 
    texte : Bienvenue !;
    Utilisateur : Entrée *  -> page actualisation : Bienvenue + "user" !
    * arrive sur une page qui lui demande taille, age, poids
    apres redirection
    Bouton -> page pour entrer données
        Page -> données qui sont entrées : placer sur fichier csv(pt txt) spécifique à l'utilsateur

        fichiers -> Users

        Qd on clicke sur le bouton check user :
            si fichier pas déja existant :
                fonction(le fichier)
            sinon : 
                créer le fichier à son nom
                fonction(le fichier)

            sur le fichier, jour, data
            données : jour, semaine, mois, l annee, depuis debut

                date->bouton/ligne qui déroule:jour en mois en années depuis début
                Calendrier de la valeur entrée (un peux comme calendrier windows)


            fonction(arg1):
                check la date
                si jour meme:
                    data jour meme
                sinon:
                    créer le jour et data

        GUI avec données a rentrer
            données ->
                nombre de pas 
                durée de sommeil (en h et min)
                distance parcourue (en km)
                calorie totale
                ...



dossier users
    dossier user
        2 fichiers:
            1er : données perso
                personnal_data={    
                    "name"
                    "surname"
                    "user_name"
                    "mail"#pas obligatoire payant pour pas de pub#
                    "mdp"
                    "date_of_birth"
                    "sexe"
                    "weight"
                    "height"
                    "nationality"
                    }

            2eme : données rentrées
                user_data{
                    year{
                        janvier {
                            1{
                                pas:
                                distance:
                                calories:
                                durée de sommeil:
                                qualité de sommeil:(entre 1 et 10)                             
                            }
                            2{}
                            3{}
                            4{}
                            5{}
                            6{}
                            7{}
                            8{}
                            9{}
                            10{}
                            11{}
                            12{}
                            13{}
                            14{}
                            15{}
                            16{}
                            17{}
                            18{}
                            19{}
                            20{}
                            21{}
                            22{}
                            23{}
                            24{}
                            25{}
                            26{}
                            27{}
                            28{}
                            29{}
                            30{}
                            31{}
                        }
                        fevrier{}
                        mars{}

                        }
                    }
                }

            



            1 bouton : pour donner les données




6 janvier 2025 : 

    On a fait:

        Un site fonctionnel dans lequel une petite interface générale et un peu de CSS (et java)
        Sur ce site, nous avons une page de connexion, depuis laquelle on peux accéder à la page sign up(fonctionnelle), un bouton déconnexion(si connecté, fonctionnel).
        Une petite page d'accueil, et une page formulaire que l'on peux remplir et avec laquelle on peux envoyer et sauvegarder les données dans les dossiers personnels (fonctionnel)
        Structure de data fonctionnel (un tout petit point à revoir)
        Structure :
        {
            année: {
                mois: {
                    jour: {}
                }
            }
        }

        - Chaque jour est une clé avec un dictionnaire vide comme valeur.
        - Les années passées incluent tous les mois et jours.
        - L'année en cours inclut uniquement les mois jusqu'au mois actuel et les jours jusqu'au jour actuel.
        

    Il reste à faire : 

        Profil pour povoir modifier les donnees personnelles (sur la page mais désactivé)
        Interface montrant et résumant les données (ajd, 7 derniers jours, dernier mois, derniere année, n importe quel jour)
        Permettre la création de groupe entre users (que l'on choisit en mettant 1 username et enverra une demande(notif)) et la comparaison de données dans ce meme groupe (classement)
        Faire en sorte qu on ne puisse ajouter de données si pas co
        


    Bonus : 
        Envoi de mail de rappel
        Mail recap
        L'utilisateur peux choisir la semaine, mois ou annee qu il veut regarder
        Adaptation de la page
        Regarder par rapport à la sécurité
        Meilleur CSS
        business (vente des données aux grosses boîtes)
        Régler le probleme de la création de 2 comptes en meme temps
        ...
        dans les infos : date de fin (dans 2 jorus : ex)
        groupe de tournois
        valeur de base pour les graphics (pour les ordres de grandeurs/axes)

    Pourcentage d'avancement du projet : 50,2%

notification : demande pour rejoindre un tournoi, (demande d'ami), rappel de debut de tournoi

expeditaire, object, la date, le destinataire, subject

Amis quand creation de tournoi comme whatsapp pour creation de groupe ?

You are invited to a tournament!
Tournament entry request
New friend request