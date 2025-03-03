Créer une IHM   qui permet d'accéder aux données de l'utilisateur et le comparer à d'autres utilsateurs (de data sur internet) et à d'autres users plus precis (amis, a travers un echange ..)



Nous voulions créer un site internet qui permet aux utilisateurs de rentrer leurs données de santé afin d'obtenir un suivi. En effet, les utilisateurs ont la possibilité de rentrer les données suivantes : Pas/distance/calories brulées/durée du sommeil/ qualité du sommeil/nombre d'étages gravis.
Notre site intitulé Friendlysteps, se compose de différentes pages parmi lesquelles : Accueil/Ajouter des données/Compétitions/Profil/Social/Aide

En premier lieu, l'accueil est personnalisé et permet à l'utilisateur de visualiser ces données quotidiennes et d'approfondir ces données en cliquant pour obtenir les graphiques associés.

L'utilisateur peut entrer ces données lorsqu'ils le désirent et les modifier au cours de la journée. De plus, ces informations sont enregistrées dans un fichier JSON.

La page Compétitions quant à elle, permet aux utilisateurs de visualiser les compétitions en cours, à venir ou terminées et lui donne la posibilité de rejoindre les compétitions par le biais d'un ID, de 11 caractères, généré automatiquement.
Les données comparées dans la compétition sont choisis par le créateur.

Par ailleurs, 

Réflexion sur l'avancement du 6 janvier 2025 : 

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
        notification : demande pour rejoindre un tournoi, (demande d'ami), rappel de debut de tournoi
        expeditaire, object, la date, le destinataire, subject
        Amis quand creation de tournoi comme whatsapp pour creation de groupe ?
        dans les infos : date de fin (dans 2 jorus : ex)
        groupe de tournois
        valeur de base pour les graphics (pour les ordres de grandeurs/axes)

    Pourcentage d'avancement du projet : 50% au 6 janvier

PPT presentation link :
https://lndb92-my.sharepoint.com/:p:/g/personal/jul_bock_lndb_eu/ETgns_8an-xAlx1nEa9DkA0BlE0EBs1jzOFmBim5nxSVWQ?e=gcX4tC
