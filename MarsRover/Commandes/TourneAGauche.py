from . import RoverCommandes

class RoverTourneAGauche(RoverCommandes):
    def __init__(self, orientation, posX, posY):
        RoverCommandes.__init__(self,orientation, posX, posY)

    def TourneAGauche(self):
        match self.orientation:
            case "N":
                self.orientation = "O"
            case "S":
                self.orientation = "E"
            case "O":
                self.orientation = "S"
            case "E":
                self.orientation = "N"
            case _:
                print("error de d'orientation vers la gauche")