import Commandes as roverCommandes
import obstacle

# initialisation d'un rover à la position (0,0) et orienté vers le Nord
monRover = roverCommandes.AllCommandes.RoverCommandes("N", 0, 0)
print("Rover ("+ str(monRover.posX) +","+ str(monRover.posY) +") dirigé vers le : " + monRover.orientation)

# TODO initalisation du ou des obstacles


                # (0,0)     N
tableau_des_actions = [
    "avancer",  # (0,1)     N
    "avancer",  # (0,2)     N
    "avancer",  # (0,3)     N
    "droite",   # (0,3)     E
    "avancer",  # (1,3)     E
    "avancer",  # (2,3)     E
    "gauche",   # (2,3)     N
    "avancer",  # (2,4)     N
    "avancer",  # (2,5)     N
    "gauche",   # (2,5)     O
    "avancer",  # (1,5)     O
    "avancer",  # (0,5)     O
    "avancer",  # (-1,5)    O
    "droite",   # (-1,5)    N
    "avancer",  # (-1,6)    N
    "avancer",  # (-1,7)    N
    "droite",   # (-1,7)    E
    "droite",   # (-1,7)    S
    "droite",   # (-1,7)    O
    "avancer",  # (-2,7)    O
    "gauche",   # (-2,7)    S
    "avancer",  # (-2,6)    S
]

# On parcourt le tableau d'actions
for action in tableau_des_actions:
    # en fonction de l'action (avancer, trouner a gauche ou tourner a droite) on met à jour la position et l'orientation de monRover
    match action:
        case "avancer":
            roverCommandes.RoverAvancer.avancer(monRover)
        case "gauche":
            roverCommandes.RoverTourneAGauche.TourneAGauche(monRover)
        case "droite":
            roverCommandes.RoverTourneADroite.TourneADroite(monRover)
        case _:
            print("error")
            exit()
    # on affiche à chaque fois la position du rover
    print("Rover ("+ str(monRover.posX) +","+ str(monRover.posY) +") dirigé vers le : " + monRover.orientation)

