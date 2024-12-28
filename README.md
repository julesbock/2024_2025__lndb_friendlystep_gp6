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
