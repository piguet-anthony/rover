from . import RoverCommandes

class RoverTourneADroite(RoverCommandes):
    def __init__(self, orientation, posX, posY):
        RoverCommandes.__init__(self,orientation, posX, posY)

    def TourneADroite(self):
        match self.orientation:
            case "N":
                self.orientation = "E"
            case "S":
                self.orientation = "O"
            case "O":
                self.orientation = "N"
            case "E":
                self.orientation = "S"
            case _:
                print("error de d'orientation vers la droite")